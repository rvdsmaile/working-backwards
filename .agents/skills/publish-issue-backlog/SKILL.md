---
name: publish-issue-backlog
description: Publish an explicitly approved Working Backwards issue backlog to a user-selected or repository-documented tracker. Use only after a technical PRD and issue breakdown are approved; supports GitHub, Linear, Jira, local Markdown, or another instructed workflow.
---

# Publish Issue Backlog

1. Confirm the target tracker, project/repository, labels/statuses, and the approved breakdown. If the tracker workflow is not documented or supplied, stop and ask; never guess.
2. Publish blockers first. Include the PRD link, end-to-end scope, acceptance criteria, verification, and actual blocker IDs in each item.
3. Use only tracker fields that the user specified or the target repository documents. Do not modify or close existing items.
4. Replace each `Tracker: Draft` marker in the breakdown with the real identifier and URL, then set its publication status to published.
