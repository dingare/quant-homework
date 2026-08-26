#!/usr/bin/env python3
"""Check changed Markdown files for repository-specific GitHub math issues."""

from __future__ import annotations

import re
import sys
from pathlib import Path


FORBIDDEN = {
    r"\operatorname": "use simple notation such as Var or Cov",
    r"\#": "use set cardinality instead of the forbidden hash macro",
    r"\(": "use $...$ for inline math",
    r"\)": "use $...$ for inline math",
    r"\[": "use $$...$$ for display math",
    r"\]": "use $$...$$ for display math",
}

INLINE_MATH_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)")
STANDALONE_EQUALS_RE = re.compile(r"\s*=+\s*")


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


def standalone_equals_errors(start_line: int, expression: str) -> list[str]:
    """Flag display-math lines GitHub can misread as Setext headings."""
    errors: list[str] = []
    for offset, line in enumerate(expression.splitlines(), start=1):
        if STANDALONE_EQUALS_RE.fullmatch(line):
            errors.append(
                f"{start_line + offset}: standalone equals line inside display math; "
                "keep = with an operand or use aligned with &="
            )
    return errors


def math_regions(text: str) -> tuple[list[tuple[int, str, bool]], list[str]]:
    regions: list[tuple[int, str, bool]] = []
    errors: list[str] = []
    display_start: int | None = None
    display_lines: list[str] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "$$":
            if display_start is None:
                display_start = line_number
                display_lines = []
            else:
                regions.append((display_start, "\n".join(display_lines), True))
                display_start = None
                display_lines = []
            continue

        if display_start is not None:
            display_lines.append(line)
            continue

        for match in INLINE_MATH_RE.finditer(line):
            regions.append((line_number, match.group(1), False))

        if line.count("$") % 2:
            errors.append(f"{line_number}: unmatched inline dollar delimiter")

    if display_start is not None:
        errors.append(f"{display_start}: unmatched display $$ delimiter")

    return regions, errors


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    in_code_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "```math":
            errors.append(
                f"{line_number}: forbidden '```math'; "
                "use $$...$$ for display math in this repository"
            )
            in_code_fence = True
            continue
        if line.strip().startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        line_without_inline_code = re.sub(r"`[^`]*`", "", line)
        for token, guidance in FORBIDDEN.items():
            if token in line_without_inline_code:
                errors.append(f"{line_number}: forbidden {token!r}; {guidance}")

    regions, delimiter_errors = math_regions(text)
    errors.extend(delimiter_errors)

    for line_number, expression, is_display in regions:
        if is_display:
            errors.extend(standalone_equals_errors(line_number, expression))
        if "<" in expression or ">" in expression:
            errors.append(
                f"{line_number}: raw angle bracket in math; use \\lt or \\gt"
            )
        balance, early_close = braces_balance(expression)
        if balance != 0 or early_close:
            errors.append(
                f"{line_number}: unbalanced math braces "
                f"(balance={balance}, early_close={early_close})"
            )

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_math_markdown.py FILE.md [FILE.md ...]", file=sys.stderr)
        return 2

    failed = False
    for argument in sys.argv[1:]:
        path = Path(argument)
        errors = check_file(path)
        if errors:
            failed = True
            for error in errors:
                print(f"{path}:{error}")

    if not failed:
        print(f"Math Markdown check passed for {len(sys.argv) - 1} file(s).")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
