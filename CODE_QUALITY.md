# Code Quality

This project uses automated code formatting and linting tools to maintain code quality.

## Backend (Python)

### Tools
- **Ruff**: Fast Python linter
- **Black**: Opinionated code formatter

### Usage
```bash
# Run from project root
docker-compose exec backend ruff check . --fix
docker-compose exec backend black .
```

### Configuration
See `backend/pyproject.toml` for Ruff and Black settings.

## Frontend (JavaScript/React)

### Tools
- **Prettier**: Code formatter

### Usage
```bash
# Run from frontend directory
npm run format        # Format all files
npm run format:check  # Check formatting without changes
```

### Configuration
See `frontend/.prettierrc` for Prettier settings.

## Pre-commit Recommendations

Consider adding these commands to your workflow:
1. Format code before committing
2. Run linters to catch issues early
3. Ensure tests pass
