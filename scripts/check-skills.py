# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml==6.0.3"]
# ///
"""Check each skills/<dir>/SKILL.md frontmatter against the Agent Skills limits.

name: present, equal to the directory, at most 64 characters, lowercase letters,
digits and single hyphens, without "anthropic" or "claude". description: present,
non-empty, at most 1024 characters. Neither may hold an XML tag.
"""

import re
import sys
from pathlib import Path

import yaml

NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TAG = re.compile(r"<[^>]+>")


def check(skill: Path) -> list[str]:
    path = skill / "SKILL.md"
    if not path.is_file():
        return [f"{path}: missing"]
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return [f"{path}: no YAML frontmatter"]
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as error:
        return [f"{path}: frontmatter does not parse: {error}"]
    if not isinstance(meta, dict):
        return [f"{path}: frontmatter is not a mapping"]

    errors = []
    name = meta.get("name")
    if not isinstance(name, str) or not name:
        errors.append("name: missing")
    else:
        if name != skill.name:
            errors.append(f"name: {name!r} differs from the directory {skill.name!r}")
        if len(name) > 64:
            errors.append(f"name: {len(name)} characters, the limit is 64")
        if not NAME.match(name):
            errors.append("name: only lowercase letters, digits and single hyphens")
        if "anthropic" in name or "claude" in name:
            errors.append('name: may not contain "anthropic" or "claude"')
        if TAG.search(name):
            errors.append("name: contains an XML tag")

    description = meta.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("description: missing or empty")
    else:
        if len(description) > 1024:
            errors.append(f"description: {len(description)} characters, the limit is 1024")
        if TAG.search(description):
            errors.append("description: contains an XML tag")
    return [f"{path}: {error}" for error in errors]


def main() -> int:
    skills = sorted(p for p in Path("skills").iterdir() if p.is_dir())
    if not skills:
        print("no skill directories under skills/", file=sys.stderr)
        return 1
    errors = [error for skill in skills for error in check(skill)]
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print(f"{len(skills)} skills ok")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
