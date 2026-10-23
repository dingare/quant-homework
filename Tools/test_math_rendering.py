"""Regressions for failures observed on actual GitHub DailyTests pages."""

import unittest

from check_math_markdown import check_text, math_regions
from build_site import protect_math, restore_math


class MathRenderingTests(unittest.TestCase):
    def test_reject_blocked_macro_even_inside_math_fence(self):
        errors = check_text("```math\n\\operatorname{Var}(X)\n```\n")
        self.assertTrue(any("blocked macro" in e for e in errors))

    def test_detect_consumed_integral_spacing(self):
        errors = check_text("$$\n\\int_0^1u\\,du\n$$\n")
        self.assertTrue(any("punctuation escapes" in e for e in errors))

    def test_detect_unprotected_matrix_rows_and_percent(self):
        for expression in [r"\begin{pmatrix}1&0\\0&1\end{pmatrix}", r"68\%"]:
            with self.subTest(expression=expression):
                errors = check_text("$$\n" + expression + "\n$$\n")
                self.assertTrue(any("punctuation escapes" in e for e in errors))

    def test_accept_protected_spacing_and_literal_braces(self):
        text = "```math\n\\int_0^1u\\,du\n```\n\n$`\\lambda\\in\\{0,1\\}`$\n"
        self.assertEqual(check_text(text), [])

    def test_detect_malformed_delimiters_braces_and_environment(self):
        for text in ["$x", "```math\nx\n", "```math\n\\frac{1}{2\n```", "```math\n\\begin{pmatrix}1\n```"]:
            with self.subTest(text=text):
                self.assertTrue(check_text(text))

    def test_ignore_program_source(self):
        source = '```python\nprint("$x")\n# \\operatorname{Var}\n```\n'
        self.assertEqual(check_text(source), [])
        self.assertEqual(math_regions(source)[0], [])

    def test_reject_invisible_character_in_matrix_command(self):
        errors = check_text("```math\nw=\x08egin{pmatrix}1\\\\2\\end{pmatrix}\n```\n")
        self.assertTrue(any("control character" in e for e in errors))

    def test_environment_order_and_escaped_end(self):
        expressions = [
            r"\begin{aligned}\begin{pmatrix}1\end{aligned}\end{pmatrix}",
            r"\begin{pmatrix}1\\end{pmatrix}",
        ]
        for expression in expressions:
            with self.subTest(expression=expression):
                self.assertTrue(any("unmatched TeX environment" in e
                                    for e in check_text("```math\n" + expression + "\n```\n")))
        self.assertEqual(check_text("```math\n" +
                         r"w=\begin{pmatrix}0.4\\0.4\\0.2\end{pmatrix}" + "\n```\n"), [])
        self.assertEqual(check_text("```math\n" +
                         r"\begin{pmatrix}1\\\end{pmatrix}" + "\n```\n"), [])

    def test_pages_round_trip_keeps_integral_escapes(self):
        expression = r"\int_0^1 u\,du=\frac12"
        protected, fragments = protect_math("```math\n" + expression + "\n```\n")
        self.assertEqual(fragments, [("display", expression)])
        restored = restore_math("<p>" + protected.strip() + "</p>", fragments)
        self.assertIn(expression, restored)
        self.assertNotIn("@@MATH_", restored)

    def test_pages_removes_only_inline_wrapper_backticks(self):
        expression = r"\lambda\in\{0,1\}"
        protected, fragments = protect_math("Inline $`" + expression + "`$.")
        self.assertEqual(fragments, [("inline", expression)])
        restored = restore_math(protected, fragments)
        self.assertIn(expression, restored)
        self.assertNotIn("`", restored)


if __name__ == "__main__":
    unittest.main()
