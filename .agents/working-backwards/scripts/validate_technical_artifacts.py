#!/usr/bin/env python3
"""Validate required sections in Working Backwards technical-delivery artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_HEADINGS = {
    "prd": (
        "## Source handoff",
        "## Problem and outcomes",
        "## Repository context",
        "## Architecture decisions",
        "## Interfaces and data flow",
        "## Testing and validation",
        "## Risks and rollout",
        "## Non-goals",
        "## Vertical slices",
        "## Open decisions",
    ),
    "issues": (
        "## Source PRD",
        "## Publication status",
        "## Issues",
    ),
}


def validate(path: Path, artifact_type: str) -> list[str]:
    if not path.is_file():
        return [f"missing {path}"]
    content = path.read_text(encoding="utf-8")
    errors = [f"missing required heading: {heading}" for heading in REQUIRED_HEADINGS[artifact_type] if heading not in content]
    if artifact_type == "issues" and "## Issues" in content:
        issue_content = content.split("## Issues", maxsplit=1)[1]
        if "### " not in issue_content:
            errors.append("issue breakdown must contain at least one vertical slice")
        for field in ("- Type:", "- Blocked by:", "#### What to build", "#### Acceptance criteria", "#### Verification"):
            if field not in issue_content:
                errors.append(f"issue breakdown missing slice field: {field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("type", choices=REQUIRED_HEADINGS)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    errors = validate(args.path, args.type)
    if errors:
        print("INVALID")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
