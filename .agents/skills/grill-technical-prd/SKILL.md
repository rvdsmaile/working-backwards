---
name: grill-technical-prd
description: Adaptively pressure-test a completed product handoff against a target repository before writing a technical PRD. Use when architecture, contracts, operations, or testing decisions remain material and must be resolved collaboratively.
---

# Grill Technical PRD

Read the source product artifacts and target repository context first. Ask focused questions only when the handoff and repository leave a material decision open.

1. Test architecture fit: existing mechanisms, boundaries, ADRs, and alternatives. Flag conflicts instead of silently creating a second mechanism.
2. Test interfaces and data: ownership, inputs/outputs, validation boundaries, migrations, and compatibility.
3. Test operations: security, privacy, failure handling, observability, rollout, and external dependencies when relevant.
4. Test validation: the highest practical test seams, acceptance evidence, and required target-repository commands.
5. Present each material decision and its recommendation for approval. Keep unanswered decisions in the PRD's open-decisions section; do not draft until blocking decisions are resolved or explicitly deferred.
6. Hand off to `write-technical-prd`.
