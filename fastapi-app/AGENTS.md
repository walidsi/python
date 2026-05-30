# AGENTS.md

Always:
- Read MEMORY.md and README.md before making changes
- Update MEMORY.md when long-term project knowledge changes
- Update README.md to make it reflect the current project state

Editing Rules:
- Always re-read a file immediately before attempting to edit it
- Never use content from a previous read if any shell commands ran in between

Memory management:
- MEMORY.md stores only long-term project knowledge and important conventions
- Keep MEMORY.md short, concise, and factual
- Do not duplicate source code, README content, or obvious implementation details
- Do not add temporary debugging notes, experiments, logs, or task history
- Update MEMORY.md only when architecture, conventions, dependencies, or important behaviors change
- Prefer editing existing memory entries instead of appending redundant information

When writing code:
- Prefer minimal targeted edits over large rewrites
- Preserve existing architecture and style unless explicitly asked
- Avoid modifying unrelated files
- Stop after producing a working solution
- Explain significant architectural changes before making them
- Ask before introducing new dependencies, frameworks, or major refactors
- Do not change formatting or linting configuration unless requested

Python execution:
- Use `uv run python` to run Python applications and scripts

