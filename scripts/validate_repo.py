#!/usr/bin/env python3
"""Read-only repository release checks for skill-ai."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Invalid or unreadable JSON: {path.relative_to(ROOT)} ({exc})")
        return None


def check_skill_inventory() -> int:
    skills = sorted((ROOT / "skills").rglob("SKILL.md"))
    names: dict[str, list[Path]] = {}
    for path in skills:
        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeError as exc:
            fail(f"Skill is not valid UTF-8: {path.relative_to(ROOT)} ({exc})")
            continue
        if not content.startswith("---"):
            fail(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
            continue
        end = content.find("\n---", 3)
        if end < 0:
            fail(f"Unclosed YAML frontmatter: {path.relative_to(ROOT)}")
            continue
        frontmatter = content[3:end]
        name = re.search(r"(?m)^name:\s*([^\s#]+)\s*$", frontmatter)
        description = re.search(r"(?m)^description:\s*(\S.*)$", frontmatter)
        if not name or not description:
            fail(f"Frontmatter needs non-empty name and description: {path.relative_to(ROOT)}")
            continue
        names.setdefault(name.group(1), []).append(path)
    duplicates = {name: paths for name, paths in names.items() if len(paths) > 1}
    for name, paths in sorted(duplicates.items()):
        WARNINGS.append(f"Duplicate skill frontmatter name {name!r}: " + ", ".join(str(p.relative_to(ROOT)) for p in paths))
    return len(skills)


def check_configs() -> None:
    config = read_json(ROOT / ".gemini-config" / "skills.json")
    if config is not None:
        entries = config.get("entries")
        if not isinstance(entries, list) or not entries:
            fail(".gemini-config/skills.json must contain a non-empty entries array")
        else:
            for entry in entries:
                path = entry.get("path", "") if isinstance(entry, dict) else ""
                if not path or "${USER_HOME}" not in path:
                    fail(f"Skill config path must use the portable ${{USER_HOME}} token: {path!r}")
    mcp = read_json(ROOT / ".gemini-config" / "mcp_config.json")
    if mcp is not None and not isinstance(mcp, dict):
        fail(".gemini-config/mcp_config.json must be a JSON object")
    if not (ROOT / "LICENSE").exists():
        WARNINGS.append("No repository-wide LICENSE: preserve and review each bundled upstream license before redistribution.")
    restore = (ROOT / "restore.ps1").read_text(encoding="utf-8-sig")
    if "catch {}" in restore or "catch { }" in restore:
        fail("restore.ps1 must not silently swallow installation errors")
    if "C:/Users/User" in restore or "C:\\Users\\User" in restore:
        fail("restore.ps1 contains a machine-specific user path")


def check_readme_count(skill_count: int) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
    headline = re.search(r"Isi Lengkap Backup \((\d+)\+? Skills\)", readme)
    if not headline:
        fail("README.md must state the current SKILL.md inventory count")
    elif int(headline.group(1)) != skill_count:
        fail(f"README count is {headline.group(1)} but actual SKILL.md count is {skill_count}")


def main() -> int:
    count = check_skill_inventory()
    check_configs()
    check_readme_count(count)
    print(f"Skill files discovered: {count}")
    for warning in WARNINGS:
        print(f"WARN: {warning}")
    for error in ERRORS:
        print(f"ERROR: {error}")
    if ERRORS:
        print(f"Release checks failed: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
        return 1
    print(f"Release checks passed: 0 error(s), {len(WARNINGS)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
