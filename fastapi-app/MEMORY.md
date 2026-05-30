# Project Memory

## Stack
- **Framework:** FastAPI + SQLModel + SQLite
- **Python:** 3.13
- **Package Manager:** `uv`
- **Linter/Formatter:** Ruff (line-length: 120, double quotes)
- **Dev Tools:** Pre-commit hooks configured

## Runtime
- Run Python via `uv run python`
- DB schema is auto-initialized via the FastAPI `lifespan` context manager on startup
- Docker image exposes port `8000` and runs as non-root user `appuser`

## Database
- SQLite file: `blogs.db` (auto-created on startup)
- `DB_ECHO` enables SQLAlchemy statement logging when set to `1`, `true`, or `yes`
- SQLModel models use a three-class pattern: `BlogBase` → `BlogCreate` / `BlogRead` → `Blog` (table)

## Conventions
- Keep Pydantic/SQLModel response and request schemas separate from the table model
- List/detail blog endpoints generally return a `{"data": ...}` envelope, but utility endpoints use route-specific shapes
- Minimal targeted edits preferred; preserve existing architecture and style
