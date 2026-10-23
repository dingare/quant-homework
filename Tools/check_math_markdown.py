#!/usr/bin/env python3
"""Check Markdown math for observed GitHub rendering failures.

Prefer fenced math blocks and GitHub's $`...`$ inline form. A syntax check
cannot establish mathematical correctness or replace checking rendered pages.
"""

from __future__ import annotations

import re
import string
import sys
from pathlib import Path

INLINE_RE = re.compile(r"\$`([^`\n]+)`\$|(?<![\\$])\$(?!\$)([^$\n]+)(?<!\\)\$(?!\$)")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
MARKDOWN_ESCAPES_RE = re.compile(r"\\[" + re.escape(string.punctuation) + r"]")
BLOCKED_MACROS = {
    "operatorname": "GitHub rejects this macro; use \\mathrm{Var}, \\mathrm{Cov}, or \\mathrm{plim}",
    "#": "GitHub rejects this macro; write set cardinality with vertical bars",
}


def braces_balance(expression: str) -> tuple[int, bool]:
    depth = 0
    early_close = False
    for index, char in enumerate(expression):
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and expression[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            early_close = early_close or depth < 0
    return depth, early_close


def math_regions(text: str) -> tuple[list[tuple[int, str, str]], list[str]]:
    regions = []
    errors = []
    fence = None
    dollar_start = None
    body = []
    for number, line in enumerate(text.split("\n"), start=1):
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", line):
            errors.append(f"{number}: invisible control character can corrupt a TeX command")
        marker = FENCE_RE.match(line)
        if fence is not None:
            char, width, kind, start = fence
            if marker and marker[1][0] == char and len(marker[1]) >= width and not marker[2].strip():
                if kind == "math":
                    regions.append((start, "\n".join(body), "fenced"))
                fence = None
                body = []
            elif kind == "math":
                body.append(line)
            continue
        if dollar_start is not None:
            if line.strip() == "$$":
                regions.append((dollar_start, "\n".join(body), "dollar-block"))
                dollar_start = None
                body = []
            else:
                body.append(line)
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]), marker[2].strip(), number)
            body = []
            continue
        if line.strip() == "$$":
            dollar_start = number
            body = []
            continue
        matches = list(INLINE_RE.finditer(line))
        for match in matches:
            protected = match[1] is not None
            regions.append((number, match[1] if protected else match[2], "protected-inline" if protected else "inline"))
        remainder = INLINE_RE.sub("", line)
        remainder = re.sub(r"(`+).*?\1", "", remainder)
        if re.search(r"(?<!\\)\$", remainder):
            errors.append(f"{number}: unmatched or unsupported dollar delimiter")
        if re.search(r"\\[()[\]]", remainder):
            errors.append(f"{number}: bare TeX delimiters do not render as math on GitHub")
    if fence is not None:
        errors.append(f"{fence[3]}: unclosed code/math fence")
    if dollar_start is not None:
        errors.append(f"{dollar_start}: unclosed $$ math block")
    return regions, errors


def check_text(text: str) -> list[str]:
    regions, errors = math_regions(text)
    for line, expression, kind in regions:
        for name, guidance in BLOCKED_MACROS.items():
            if re.search(r"\\" + re.escape(name) + (r"\b" if name.isalpha() else ""), expression):
                errors.append(f"{line}: blocked macro \\{name}; {guidance}")
        depth, early = braces_balance(expression)
        if depth or early:
            errors.append(f"{line}: unbalanced math braces (balance={depth}, early_close={early})")
        if kind in {"inline", "dollar-block"}:
            if MARKDOWN_ESCAPES_RE.search(expression):
                errors.append(f"{line}: Markdown can consume TeX punctuation escapes; use a math fence or $`...`$")
            if re.search(r"[<>]", expression):
                errors.append(f"{line}: raw angle brackets in unprotected math; use \\lt / \\gt")
            if kind == "dollar-block" and re.search(r"^\s*=+\s*$", expression, re.M):
                errors.append(f"{line}: standalone equals line can become a Markdown heading; use a math fence")
        environments = []
        invalid_environment = False
        for slashes, action, name in re.findall(r"(\\+)(begin|end)\{([^}]+)\}", expression):
            if len(slashes) % 2 == 0:
                continue
            if action == "begin":
                environments.append(name)
            elif not environments or environments.pop() != name:
                invalid_environment = True
        if environments or invalid_environment:
            errors.append(f"{line}: unmatched TeX environment")
    return errors


def check_file(path: Path) -> list[str]:
    return check_text(path.read_text(encoding="utf-8"))


def main() -> int:
    arguments = sys.argv[1:] or ["Questions", "DailyTests"]
    paths = []
    for argument in arguments:
        path = Path(argument)
        paths.extend(sorted(path.rglob("*.md")) if path.is_dir() else [path])
    failed = False
    for path in paths:
        for error in check_file(path):
            failed = True
            print(f"{path}:{error}")
    if not paths:
        print("No Markdown files found", file=sys.stderr)
        return 2
    if not failed:
        print(f"Math Markdown check passed for {len(paths)} file(s). Rendered-page and mathematical review are separate checks.")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
