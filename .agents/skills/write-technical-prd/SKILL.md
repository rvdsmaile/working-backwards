---
name: write-technical-prd
description: Write a repository-aware technical PRD from an approved Working Backwards handoff and technical grill. Use after target-repository discovery and technical design approval, before implementation planning or issue slicing.
---

# Write Technical PRD

Use `../../working-backwards/templates/technical-prd.md`.

1. Save the PRD in the target repository's existing spec location; otherwise use `docs/specs/YYYY-MM-DD-<slug>.md`.
2. Link to source handoff artifacts and canonical target-repository documents. Do not duplicate commands, conventions, or architecture inventories.
3. Commit to architecture, interfaces/data flow, test seams, risks/rollout, non-goals, and independently testable vertical slices. Do not include exact files, code snippets, estimates, or implementation tasks.
4. Run `../../working-backwards/scripts/validate_technical_artifacts.py prd <prd-path>` and hand off to `review-technical-prd`.
