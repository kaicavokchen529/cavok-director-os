#!/usr/bin/env python3
"""Validate CAVOK package structure, references, isolation, and duplicate content."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
MAX_SKILL_LINES = 500

# These identifiers belong to audited external/legacy systems, not CAVOK.
# Scan Markdown only so this local denylist does not flag itself.
FOREIGN_MARKERS = (
    "manjun-laoli",
    "满军老李",
    "courenao-cg-director",
    "seedance-combat-prompt",
    "凑热闹 cg 对战导演系统",
)

ABSOLUTE_PATH_PATTERNS = (
    re.compile(r"[A-Za-z]:\\(?:Users|Documents|Desktop)\\"),
    re.compile(r"(?<![\w.])/(?:Users|home|workspace|root)/"),
)

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_frontmatter(errors: list[str]) -> None:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(errors, "SKILL.md: missing YAML frontmatter")
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(errors, "SKILL.md: unclosed YAML frontmatter")
        return
    keys = []
    for line in parts[1].splitlines():
        match = re.match(r"^([a-zA-Z0-9_-]+):", line)
        if match:
            keys.append(match.group(1))
    if keys != ["name", "description"]:
        fail(errors, f"SKILL.md: frontmatter keys must be name, description; found {keys}")
    name_match = re.search(r"(?m)^name:\s*(\S+)\s*$", parts[1])
    if not name_match or name_match.group(1) != ROOT.name:
        fail(errors, "SKILL.md: name must match the skill directory")


def check_size(errors: list[str]) -> None:
    count = len(SKILL.read_text(encoding="utf-8").splitlines())
    if count > MAX_SKILL_LINES:
        fail(errors, f"SKILL.md: {count} lines exceeds {MAX_SKILL_LINES}")


def check_links(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"{path.relative_to(ROOT)}: link escapes package: {raw}")
                continue
            if not resolved.exists():
                fail(errors, f"{path.relative_to(ROOT)}: dangling link: {raw}")


def check_isolation(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for marker in FOREIGN_MARKERS:
            if marker.lower() in lowered:
                fail(errors, f"{path.relative_to(ROOT)}: foreign marker found: {marker}")
        for pattern in ABSOLUTE_PATH_PATTERNS:
            if pattern.search(text):
                fail(errors, f"{path.relative_to(ROOT)}: machine-specific absolute path found")


def check_duplicates(errors: list[str]) -> None:
    seen: dict[str, Path] = {}
    for path in sorted(ROOT.rglob("*.md")):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest in seen:
            fail(
                errors,
                f"duplicate Markdown: {seen[digest].relative_to(ROOT)} == {path.relative_to(ROOT)}",
            )
        else:
            seen[digest] = path


def check_required_routes(errors: list[str]) -> None:
    skill_text = SKILL.read_text(encoding="utf-8")
    action_text = (ROOT / "references" / "action-direction.md").read_text(encoding="utf-8")
    required = (
        "references/combat-decision-engine.md",
        "references/cinematography-language-engine.md",
        "references/rule-authority-map.md",
        "references/isolation-contract.md",
    )
    for route in required:
        if route not in skill_text:
            fail(errors, f"SKILL.md: required route missing: {route}")
    if "combat-decision-engine.md" not in action_text:
        fail(errors, "action-direction.md: combat decision authority is not routed")


def main() -> int:
    errors: list[str] = []
    if not SKILL.exists():
        print("ERROR: SKILL.md not found")
        return 1
    check_frontmatter(errors)
    check_size(errors)
    check_links(errors)
    check_isolation(errors)
    check_duplicates(errors)
    check_required_routes(errors)
    if errors:
        print(f"CAVOK validation failed: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    markdown_count = sum(1 for _ in ROOT.rglob("*.md"))
    print(f"CAVOK validation passed: {markdown_count} Markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
