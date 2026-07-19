---
name: break-prd-into-issues
description: Create a reviewable, dependency-ordered issue backlog from an approved technical PRD. Use when a team needs independently grabbable vertical slices before publishing to any issue tracker.
---

# Break PRD into Issues

Use `../../working-backwards/templates/issue-breakdown.md`.

1. Write the breakdown beside the PRD using the same slug plus `-issue-breakdown.md`.
2. Make every issue a thin, complete vertical slice with a verifiable behavior. Do not create horizontal tickets for all schemas, APIs, or UI.
3. Give each issue an AFK or HITL type, dependency, tracker-draft status, end-to-end scope, acceptance criteria, and verification evidence.
4. Order issues so blockers appear first. Present the complete backlog for user approval; do not publish it.
5. Run `../../working-backwards/scripts/validate_technical_artifacts.py issues <breakdown-path>` and hand off to `publish-issue-backlog` only after explicit approval.
