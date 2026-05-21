# Copilot Instructions

This repository uses a document-driven vibe coding workflow.

## Source of truth
- Treat `docs/` as the single source of truth.
- Do not rely on historical chat context when repository documents already define the current state.

## Workflow
Work in the following order:
1. `docs/proposal.md`
2. `docs/high-level-design.md`
3. `docs/detailed-design.md`
4. `docs/tasks/*.md`
5. `docs/prompt.md` and implementation

## Behavior rules
- During requirements and design, ask clarifying questions instead of guessing intent.
- During implementation, only work within the current module boundary.
- Record new implementation assumptions in `.ai/state/assumptions.md`.
- Keep changes testable and small.
- Prefer simple, maintainable solutions over clever or overly broad rewrites.

## Completion rules
Before considering work complete:
- Run lint / typecheck / test for the active language profile.
- Update checklist items in the relevant task file.
- Update `docs/tasks/progress.md`.
