---
name: synthesize-working-backwards
description: Resolve customer, product, and delivery critique findings in a Working Backwards initiative. Use after independent critiques or when a PRFAQ needs a decision-focused revision before handoff.
---

# Synthesize Working Backwards

Read `../../working-backwards/WORKFLOW.md`.

1. Group duplicate findings, then resolve each by revising the artifact, recording a decision, narrowing scope, or explicitly accepting a risk.
2. Update `critique.md`, `decision-log.md`, announcement, and FAQs together so they remain consistent.
3. Set the phase to `synthesis`; do not proceed while a critical finding remains open.
4. Run `../../working-backwards/scripts/validate_initiative.py <initiative-path>` before handoff and route to `handoff-working-backwards` only on success.
