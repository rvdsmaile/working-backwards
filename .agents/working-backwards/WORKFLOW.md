# Working Backwards workflow

## Phases

`intake` → `shaping` → `drafting` → `challenging` → `synthesis` → `handoff`

Move forward only when the current phase has its required artifact. Returning to an earlier phase is allowed when a decision changes.

## Initiative files

| File | Required phase | Purpose |
| --- | --- | --- |
| `initiative.md` | intake | Context, scope, phase, open decisions |
| `announcement.md` | drafting | Future-facing announcement/blog post |
| `faq.md` | drafting | Customer FAQ |
| `internal-faq.md` | optional | Operating, commercial, and delivery questions |
| `decision-log.md` | shaping | Assumptions, decisions, alternatives, risks |
| `critique.md` | challenging | Findings from all three critiques |
| `product-brief.md` | handoff | Decision-ready product brief |
| `build-plan.md` | handoff | Outcomes, milestones, risks, acceptance criteria |

## Critique rules

Record each finding with `severity: critical|important|minor`, an owner, and `status: open|resolved|accepted-risk`. A critical finding must be resolved or explicitly accepted as a risk before handoff.

## Language rules

- Write customer-facing artifacts in plain language.
- Label uncertainty as an assumption. Cite external material only when the user asks for research.
- Prefer a specific customer, problem, and change over generic benefit claims.
- Do not use Amazon framing or require a launch date.
