# Copilot Instructions

This repository uses a document-driven VibeFlow workflow.

## Source of truth
- Treat `docs/` as the single source of truth.
- Do not rely on historical chat context when repository documents already define the current state.

## Workflow
For initial setup, work in the following order:
1. `docs/proposal.md`
2. `docs/high-level-design.md`
3. `docs/detailed-design.md`
4. `docs/tasks/*.md`
5. `docs/prompt.md` and implementation

For ongoing development, prefer:
- `docs/changes/feature-*.md`
- `docs/changes/bugfix-*.md`
- `docs/changes/refactor-*.md`

## Behavior rules
- During requirements and design, ask clarifying questions instead of guessing intent.
- During implementation, only work within the current module boundary.
- Record new implementation assumptions in `.ai/state/assumptions.md`.
- Keep changes testable and small.
- Prefer simple, maintainable solutions over clever or overly broad rewrites.
- For feature / bugfix / refactor work, create or read the relevant file in `docs/changes/` first.

## Completion rules
Before considering work complete:
- Run lint / typecheck / test for the active language profile.
- Update checklist items in the relevant task file.
- Update `docs/tasks/progress.md`.
