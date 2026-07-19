---
name: start-technical-delivery
description: Start repository-aware technical delivery from a completed Working Backwards handoff. Use when product brief, build plan, and initiative are complete and a user wants a technical PRD or tracker-ready issue backlog.
---

# Start Technical Delivery

Read `../../working-backwards/WORKFLOW.md`.

1. Require paths to the source initiative and the target implementation repository. Run `../../working-backwards/scripts/validate_initiative.py <initiative> --require-handoff`.
2. Read target-repository instructions, architecture/ADRs, area docs, testing and verification conventions, durable learnings, and tracker guidance before asking design questions.
3. Never assume the target's language, architecture, spec directory, or tracker. Use its documented convention; if absent, default only the PRD location to `docs/specs/` and ask the user to identify the tracker.
4. Hand off to `grill-technical-prd`.
