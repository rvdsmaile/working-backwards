---
name: review-technical-prd
description: Review a repository-aware technical PRD before converting it into issue slices. Use when a technical PRD must be checked for source coverage, repository fit, testability, and unresolved high-risk decisions.
---

# Review Technical PRD

Read the PRD, source handoff, and target repository guidance.

1. Check source coverage, non-goals, architecture fit, existing-mechanism reuse, interface/data clarity, test seams, risks/rollout, and open decisions.
2. Require evidence for material dependency or external API assumptions; reject undocumented high-risk security, migration, or operational decisions.
3. Return `PASS`, `PASS WITH NOTES`, or `FAIL` with concrete corrections. A failed PRD returns to the technical grill or PRD author; do not issue-slice it.
4. On pass, hand off to `break-prd-into-issues`.
