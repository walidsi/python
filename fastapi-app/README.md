# FastAPI Blog Application

A FastAPI-based web application that implements a small blog API with SQLModel and a SQLite backend. The current API supports creating posts, listing posts, reading posts by ID, and filtering by publication status.

## Features

- Create blog posts
- Read all blog posts or fetch a single post by ID
- Filter blog posts by publication status
- Auto-create the SQLite schema on application startup
- Docker support for containerized runs
- Automatically generated OpenAPI documentation

## Getting Started

### Prerequisites

- Python 3.13
- Docker (for containerized deployment)

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd fastapi-app
```

2. Install dependencies
```bash
uv sync --frozen
```

3. Run the development server
```bash
uv run uvicorn main:app --reload --host 127.0.0.1 --port 9000
```

The API will be available at `http://127.0.0.1:9000`.
Interactive docs are available at `http://127.0.0.1:9000/docs`.

### Docker Usage

Build and run the container:
```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

The container serves the app on `http://127.0.0.1:8000`.

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/health` | Health check endpoint |
| GET | `/` | Get all blogs |
| GET | `/blog` | Get blogs with optional `limit` and `published` filters |
| GET | `/blog/unpublished` | Get unpublished blogs |
| GET | `/blog/{id}` | Get a specific blog by ID |
| GET | `/blog/{id}/comments` | Get placeholder comments for a blog |
| POST | `/blog` | Create a new blog |
| GET | `/about` | Get author information |

`/blog` currently accepts a `sort` query parameter, but it is not applied by the implementation yet.

## Configuration

- Database file: `blogs.db` (SQLite)
- Optional environment variable: `DB_ECHO=1` enables SQL statement logging
- Docker configuration in `Dockerfile`

## Development Notes

- The database schema is created automatically during app startup through the FastAPI `lifespan` hook.
- The project uses `uv` for dependency management.
- Ruff and pre-commit are configured for linting and formatting.
