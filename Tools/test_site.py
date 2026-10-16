"""Regressions for missing website pages, section links, and preview output."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_site as site


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        for name, value in (("ROOT", self.root), ("SITE_DIR", self.root / "_site")):
            patcher = patch.object(site, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def write(self, relative, content):
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def test_build_includes_linked_support_pages_and_uses_requested_output(self):
        self.write("README.md", "# Handbook\n\n"
                   "[Backlog](Backlog.md#ab-testing--review-to-do)\n\n"
                   "[Review](Recent_Quant_Prep_Review_2026-07-18.md)\n\n"
                   "[Math guide](Tools/MathMarkdownGuide.md)\n")
        self.write("INDEX.md", "# Index\n\n[Home](README.md)\n")
        self.write("Backlog.md", "# Backlog\n\n## A/B Testing — Review To-Do\n")
        self.write("Recent_Quant_Prep_Review_2026-07-18.md", "# Review\n")
        self.write("Tools/MathMarkdownGuide.md", "# Math guide\n\n[Home](../README.md)\n")
        output = self.root / "preview"
        site.build_site(output)
        for relative in ("index.html", "INDEX.html", "Backlog.html", "Recent_Quant_Prep_Review_2026-07-18.html",
                         "Tools/MathMarkdownGuide.html"):
            self.assertTrue((output / relative).is_file(), relative)
        self.assertFalse(site.SITE_DIR.exists())
        guide = (output / "Tools/MathMarkdownGuide.html").read_text()
        self.assertIn('href="../index.html"', guide)

    def test_heading_links_keep_punctuation_spacing_and_unique_ids(self):
        note = self.write("README.md", "# Handbook\n\n"
                          "## Interview Drill — Why Ridge Is Invertible\n\n"
                          "## **Review**\n\n## Review\n\n## Review-1\n")
        _, body = site.render_markdown(note)
        page = site.PageLinks()
        page.feed(body)
        self.assertEqual(page.ids, {"handbook", "interview-drill--why-ridge-is-invertible",
                                    "review", "review-1", "review-1-1"})
        self.assertEqual(site.render_markdown(note)[1], body)

    def test_math_in_heading_is_restored_without_corrupting_id(self):
        note = self.write("README.md", "# Review $`x^2`$\n")
        _, body = site.render_markdown(note)
        self.assertIn('id="review-x2"', body)
        self.assertIn(r"\(x^2\)", body)
        self.assertNotIn("@@MATH_", body)

    def test_link_check_accepts_nested_and_encoded_sections_and_external_links(self):
        self.write("preview/index.html", '<h1 id="home">Home</h1><a href="#home">Home</a>'
                   '<a href="notes/note%20one.html?q=1#%E5%A4%8D%E4%B9%A0">Note</a>'
                   '<a href="https://example.com/missing.html#section">External</a>')
        self.write("preview/notes/note one.html", '<h2 id="复习">Review</h2>'
                   '<a href="../index.html#home">Home</a>')
        site.check_site_links(self.root / "preview")

    def test_link_check_rejects_missing_pages(self):
        self.write("preview/index.html", '<a href="Backlog.html">Backlog</a>')
        with self.assertRaisesRegex(ValueError, "missing page Backlog.html"):
            site.check_site_links(self.root / "preview")

    def test_link_check_rejects_missing_sections(self):
        self.write("preview/index.html", '<a href="note.html#review">Review</a>')
        self.write("preview/note.html", '<h2>Review</h2>')
        with self.assertRaisesRegex(ValueError, "missing section note.html#review"):
            site.check_site_links(self.root / "preview")


if __name__ == "__main__":
    unittest.main()
