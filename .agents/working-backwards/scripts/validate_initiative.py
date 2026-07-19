#!/usr/bin/env python3
"""Validate a Working Backwards initiative without external dependencies."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PHASES = ("intake", "shaping", "drafting", "challenging", "synthesis", "handoff")
REQUIRED_BY_PHASE = {
    "intake": ("initiative.md",),
    "shaping": ("initiative.md", "decision-log.md"),
    "drafting": ("initiative.md", "decision-log.md", "announcement.md", "faq.md"),
    "challenging": ("initiative.md", "decision-log.md", "announcement.md", "faq.md", "critique.md"),
    "synthesis": ("initiative.md", "decision-log.md", "announcement.md", "faq.md", "critique.md"),
    "handoff": ("initiative.md", "decision-log.md", "announcement.md", "faq.md", "critique.md", "product-brief.md", "build-plan.md"),
}


def phase_from(initiative: Path) -> str | None:
    lines = initiative.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.strip().lower() == "## phase":
            for candidate in lines[index + 1 :]:
                value = candidate.strip().lower()
                if value:
                    return value
    return None


def unresolved_critical_findings(critique: Path) -> list[str]:
    findings = []
    for line in critique.read_text(encoding="utf-8").splitlines():
        lowered = line.lower()
        if "critical" in lowered and ("| open |" in lowered or "| unresolved |" in lowered):
            findings.append(line)
    return findings


def validate(root: Path) -> list[str]:
    errors = []
    initiative = root / "initiative.md"
    if not initiative.is_file():
        return ["missing initiative.md"]
    phase = phase_from(initiative)
    if phase not in PHASES:
        return [f"invalid phase: {phase or 'missing'}"]
    for filename in REQUIRED_BY_PHASE[phase]:
        if not (root / filename).is_file():
            errors.append(f"missing {filename} required for {phase}")
    if phase == "handoff" and (root / "critique.md").is_file():
        errors.extend(f"unresolved critical finding: {line}" for line in unresolved_critical_findings(root / "critique.md"))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("initiative", type=Path)
    args = parser.parse_args()
    errors = validate(args.initiative)
    if errors:
        print("INVALID")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
