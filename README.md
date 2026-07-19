# Working Backwards

A composable set of agent skills for turning a rough product idea into a clear customer narrative and a build-ready product plan.

Working Backwards keeps the useful discipline of starting with the customer experience, without turning it into a heavyweight process. It is narrative-first: write the future-facing announcement, answer the questions it raises, challenge the proposal from three perspectives, then make the decisions explicit before planning delivery.

## What it helps you do

Start with anything from a sentence to existing product notes, then move through a deliberate flow:

```text
idea → customer and problem → announcement → FAQ → critiques → decisions → product brief + build plan
```

The framework creates durable Markdown artifacts in `docs/working-backwards/<initiative-slug>/`, so the reasoning survives the conversation and is easy to share.

## Skills

| Skill | Use it to |
| --- | --- |
| `start-working-backwards` | Start a guided initiative from a rough idea or notes. |
| `shape-product-idea` | Clarify the customer, problem, scope, constraints, and non-goals. |
| `write-announcement` | Draft the future-facing announcement or blog post. |
| `write-faq` | Answer the customer questions the announcement creates. |
| `write-internal-faq` | Optionally capture internal product, commercial, and delivery questions. |
| `challenge-customer-value` | Test whether the customer problem and value are genuinely compelling. |
| `challenge-product-coherence` | Test scope, decisions, promises, and non-goals for consistency. |
| `challenge-delivery` | Surface decision-level delivery risks and dependencies. |
| `synthesize-working-backwards` | Resolve critiques and keep the narrative and decisions aligned. |
| `handoff-working-backwards` | Create the final product brief and build plan. |

## Getting started

This is intentionally a repository-local skill set, not a plugin. Copy or add the `.agents/` directory to the project where you want to use it, then start a conversation such as:

> I have an idea for a tool that helps small teams understand why customers churn. Start a Working Backwards initiative.

The framework will ask only for the details it cannot infer, then offer to create an initiative workspace. You can also invoke a specific skill directly when you already know the stage you need.

## Artifacts

Each initiative can contain:

- `initiative.md` — context, current phase, scope, and open decisions
- `announcement.md` — customer-facing future narrative
- `faq.md` — customer questions and answers
- `internal-faq.md` — optional internal questions
- `decision-log.md` — assumptions, decisions, alternatives, and risks
- `critique.md` — customer, product, and delivery findings
- `product-brief.md` and `build-plan.md` — handoff outputs

The internal FAQ is optional. External research is optional too: the framework labels uncertainty as an assumption rather than inventing evidence.

## Quality gate

The handoff skill requires the announcement, FAQ, decision log, critiques, product brief, and build plan. Critical critique findings must be resolved or explicitly accepted as risks.

Validate an initiative at any point:

```bash
python3 .agents/working-backwards/scripts/validate_initiative.py \
  docs/working-backwards/<initiative-slug>
```

## Principles

- Start with a specific customer and meaningful change.
- Make promises concrete; expose uncertainty rather than concealing it.
- Keep scope and non-goals visible.
- Challenge the narrative before turning it into a plan.
- Stop at outcomes, milestones, risks, and acceptance criteria—not code, estimates, or engineering tickets.

## Development

Run the validator tests with:

```bash
python3 -B -m unittest discover -s tests -v
```
