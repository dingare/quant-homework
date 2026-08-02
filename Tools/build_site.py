#!/usr/bin/env python3
"""Build a lightweight mobile-friendly static site from Markdown notes."""

from __future__ import annotations

import argparse
import html
import re
import shutil
from pathlib import Path

import mistune


ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "_site"
REPO_URL = "https://github.com/dingare/quant-homework"
SITE_TITLE = "Buyside Quant Handbook"

CONTENT_PATTERNS = [
    "README.md",
    "INDEX.md",
    "Progress.md",
    "Connections/*.md",
    "Questions/**/*.md",
    "KnowledgeCards/**/*.md",
    "Templates/*.md",
]

MATH_FENCE_RE = re.compile(r"```math\n(.*?)\n```", re.DOTALL)
INLINE_MATH_RE = re.compile(r"(?<!\\)\$(?!\s)(.+?)(?<!\s)(?<!\\)\$")


def collect_markdown_files() -> list[Path]:
    files: list[Path] = []
    for pattern in CONTENT_PATTERNS:
        files.extend(ROOT.glob(pattern))
    return sorted(set(path for path in files if path.is_file()))


def page_output_path(markdown_path: Path) -> Path:
    relative = markdown_path.relative_to(ROOT)
    if relative == Path("README.md"):
        return SITE_DIR / "index.html"
    return SITE_DIR / relative.with_suffix(".html")


def html_href_for_markdown_link(current_markdown: Path, target: str) -> str:
    if "://" in target or target.startswith("#") or target.startswith("mailto:"):
        return target

    path_part, anchor = split_link_anchor(target)
    if not path_part.endswith(".md"):
        return target

    source_dir = current_markdown.relative_to(ROOT).parent
    target_markdown = (ROOT / source_dir / path_part).resolve()
    try:
        target_relative = target_markdown.relative_to(ROOT)
    except ValueError:
        return target

    target_output = page_output_path(ROOT / target_relative)
    current_output = page_output_path(current_markdown)
    rel_href = Path(
        relpath(target_output, current_output.parent)
    ).as_posix()
    return f"{rel_href}{anchor}"


def split_link_anchor(target: str) -> tuple[str, str]:
    for marker in ("#", "?"):
        if marker in target:
            base, suffix = target.split(marker, 1)
            return base, f"{marker}{suffix}"
    return target, ""


def relpath(target: Path, start: Path) -> str:
    return str(target.relative_to(start)) if target.is_relative_to(start) else __import__("os").path.relpath(target, start)


def protect_math(markdown_text: str) -> tuple[str, list[tuple[str, str]]]:
    fragments: list[tuple[str, str]] = []

    def stash(kind: str, content: str) -> str:
        fragments.append((kind, content))
        return f"@@MATH_{len(fragments) - 1}@@"

    protected = MATH_FENCE_RE.sub(lambda m: stash("display", m.group(1).strip()), markdown_text)
    protected = INLINE_MATH_RE.sub(lambda m: stash("inline", m.group(1)), protected)
    return protected, fragments


def restore_math(rendered_html: str, fragments: list[tuple[str, str]]) -> str:
    restored = rendered_html
    for index, (kind, content) in enumerate(fragments):
        escaped = html.escape(content, quote=False)
        placeholder = f"@@MATH_{index}@@"
        if kind == "display":
            block = f'<div class="math-display">\\[{escaped}\\]</div>'
            restored = restored.replace(f"<p>{placeholder}</p>", block)
            restored = restored.replace(placeholder, block)
        else:
            restored = restored.replace(placeholder, f'<span class="math-inline">\\({escaped}\\)</span>')
    return restored


def rewrite_markdown_links(rendered_html: str, current_markdown: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        href = html.unescape(match.group(1))
        rewritten = html_href_for_markdown_link(current_markdown, href)
        return f'href="{html.escape(rewritten, quote=True)}"'

    return re.sub(r'href="([^"]+)"', replace, rendered_html)


def markdown_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def render_markdown(markdown_path: Path) -> tuple[str, str]:
    markdown_text = markdown_path.read_text(encoding="utf-8")
    protected, math_fragments = protect_math(markdown_text)
    markdown = mistune.create_markdown(
        escape=False,
        plugins=["strikethrough", "table", "url"],
    )
    body = markdown(protected)
    body = restore_math(body, math_fragments)
    body = rewrite_markdown_links(body, markdown_path)
    return markdown_title(markdown_text, markdown_path.stem), body


def build_navigation(markdown_files: list[Path], current_markdown: Path) -> str:
    note_files = [
        path
        for path in markdown_files
        if "Questions" in path.parts or "KnowledgeCards" in path.parts
    ]
    links = []
    for path in note_files:
        title = markdown_title(path.read_text(encoding="utf-8"), path.stem)
        href = relpath(page_output_path(path), page_output_path(current_markdown).parent)
        links.append(f'<a href="{html.escape(href, quote=True)}">{html.escape(title)}</a>')
    return "\n".join(links)


def page_template(title: str, body: str, markdown_path: Path, markdown_files: list[Path]) -> str:
    current_output = page_output_path(markdown_path)
    root_href = relpath(SITE_DIR / "index.html", current_output.parent)
    index_href = relpath(SITE_DIR / "INDEX.html", current_output.parent)
    source_href = f"{REPO_URL}/blob/main/{markdown_path.relative_to(ROOT).as_posix()}"
    nav = build_navigation(markdown_files, markdown_path)
    escaped_title = html.escape(title)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escaped_title} · {SITE_TITLE}</title>
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['\\\\(', '\\\\)']],
        displayMath: [['\\\\[', '\\\\]']],
        processEscapes: true
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
  <style>
    :root {{
      color-scheme: light;
      --ink: #172033;
      --muted: #617089;
      --line: #dbe4f0;
      --paper: #ffffff;
      --wash: #f3f7fb;
      --accent: #0f6f8f;
      font-family: ui-serif, Georgia, "Times New Roman", serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        radial-gradient(circle at top left, rgba(15, 111, 143, 0.12), transparent 34rem),
        linear-gradient(180deg, #f8fbfd 0%, var(--wash) 100%);
      color: var(--ink);
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 10;
      display: flex;
      gap: 0.8rem;
      align-items: center;
      justify-content: space-between;
      padding: 0.85rem clamp(1rem, 4vw, 2rem);
      border-bottom: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(12px);
    }}
    header a {{ color: var(--accent); text-decoration: none; font-weight: 700; }}
    .layout {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) 18rem;
      gap: 1.2rem;
      width: min(100%, 1180px);
      margin: 0 auto;
      padding: clamp(1rem, 4vw, 2rem);
    }}
    main {{
      min-width: 0;
      padding: clamp(1.1rem, 4vw, 2.4rem);
      border: 1px solid var(--line);
      border-radius: 22px;
      background: var(--paper);
      box-shadow: 0 18px 50px rgba(23, 32, 51, 0.08);
    }}
    aside {{
      align-self: start;
      position: sticky;
      top: 4.7rem;
      max-height: calc(100vh - 6rem);
      overflow: auto;
      padding: 1rem;
      border: 1px solid var(--line);
      border-radius: 18px;
      background: rgba(255, 255, 255, 0.78);
    }}
    aside h2 {{ margin-top: 0; font-size: 1rem; color: var(--muted); }}
    aside a {{ display: block; margin: 0.55rem 0; color: var(--accent); text-decoration: none; }}
    h1 {{ margin-top: 0; font-size: clamp(2rem, 8vw, 3.4rem); line-height: 1.05; }}
    h2 {{ margin-top: 2.1rem; padding-bottom: 0.35rem; border-bottom: 1px solid var(--line); }}
    h3 {{ margin-top: 1.6rem; }}
    p, li {{ line-height: 1.75; font-size: 1.04rem; }}
    a {{ color: var(--accent); }}
    code {{
      padding: 0.12rem 0.32rem;
      border-radius: 6px;
      background: #edf3f8;
      font-size: 0.92em;
    }}
    pre {{
      overflow-x: auto;
      padding: 1rem;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: #f7fafc;
      color: #172033;
    }}
    table {{
      display: block;
      width: 100%;
      overflow-x: auto;
      border-collapse: collapse;
    }}
    th, td {{ padding: 0.65rem 0.8rem; border: 1px solid var(--line); }}
    blockquote {{
      margin-left: 0;
      padding-left: 1rem;
      border-left: 4px solid var(--accent);
      color: var(--muted);
    }}
    .math-display {{
      margin: 1.2rem 0;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 0.35rem 0;
      text-align: center;
    }}
    .math-inline {{ white-space: nowrap; }}
    .source-link {{
      display: inline-flex;
      margin-top: 2rem;
      color: var(--muted);
      font-size: 0.95rem;
    }}
    @media (max-width: 860px) {{
      .layout {{ display: block; padding: 0.8rem; }}
      main {{ border-radius: 16px; }}
      aside {{ position: static; margin-top: 1rem; max-height: none; }}
      header {{ align-items: flex-start; flex-direction: column; }}
    }}
  </style>
</head>
<body>
  <header>
    <a href="{html.escape(root_href, quote=True)}">{SITE_TITLE}</a>
    <nav>
      <a href="{html.escape(index_href, quote=True)}">Index</a>
      <span aria-hidden="true"> · </span>
      <a href="{source_href}">Source</a>
    </nav>
  </header>
  <div class="layout">
    <main>
      {body}
      <a class="source-link" href="{source_href}">View Markdown source on GitHub</a>
    </main>
    <aside>
      <h2>Notes</h2>
      {nav}
    </aside>
  </div>
</body>
</html>
"""


def build_site(output_dir: Path) -> None:
    markdown_files = collect_markdown_files()
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    for markdown_path in markdown_files:
        title, body = render_markdown(markdown_path)
        output_path = page_output_path(markdown_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(page_template(title, body, markdown_path, markdown_files), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SITE_DIR, help="Output directory, default: _site")
    args = parser.parse_args()
    build_site(args.output.resolve())


if __name__ == "__main__":
    main()
