# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Essential Commands

```bash
make setup     # Install dependencies
make test      # Format + lint + run all tests
make validate  # Validate workflow files against schema
```

## Architecture

Dossier is a collection of structured workflows (`.ds.md` files) for AI agents, with an MCP server that exposes them as tools.

### Components

1. **Workflows** (`workflows/`): Markdown files with JSON frontmatter following `workflow-schema.json`. Each workflow has objectives, steps, and validation criteria.

2. **MCP Server** (`mcp-server/`): Python server that fetches workflows from GitHub and exposes them as MCP tools. Caches workflow list for 1 hour.

3. **Validation** (`utils/validate_workflow.py`, `test/lint.sh`): Ensures workflows have valid frontmatter matching the schema.

### Workflow Schema

Workflows require frontmatter with: `schema_version`, `title`, `version`, `status`, `objective`. Optional fields include `inputs`, `outputs`, `prerequisites`, `validation`, etc.

## Code Style

- Use `uv run ruff format .` and `uv run ruff check .` before committing
- Python 3.12+
- Imports at top of file, never inline
