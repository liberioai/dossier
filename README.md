# Dossier

Structured workflow files (`.ds.md`) for AI agents.

## What is a Workflow?

A workflow is a markdown file with JSON frontmatter that AI agents can follow to complete tasks. Instead of writing scripts, you write clear instructions with objectives, steps, and validation criteria.

### Example

```markdown
---
{
  "schema_version": "1.0.0",
  "title": "Setup Python Project",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Initialize a Python project with uv, ruff, and pytest"
}
---
# Setup Python Project

## Steps

1. **Initialize project** - Run `uv init` to create pyproject.toml
2. **Add dev dependencies** - Run `uv add --dev ruff pytest`
3. **Create structure** - Create `src/` and `tests/` directories
```

## Architecture

```
workflows/                     # Workflow files (.ds.md)
├── workflow-schema.json       # JSON Schema for frontmatter validation
├── create-workflow.ds.md      # Meta-workflow to create new workflows
└── documentation/             # Category folders
    └── readme-reality-check.ds.md

utils/
└── validate_workflow.py       # Validates workflows against schema

mcp-server/                    # MCP server (separate Python project)
└── server.py                  # Exposes workflows as MCP tools
```

Key files:
- [workflows/workflow-schema.json](./workflows/workflow-schema.json) - Schema definition
- [workflows/create-workflow.ds.md](./workflows/create-workflow.ds.md) - Create new workflows
- [utils/validate_workflow.py](./utils/validate_workflow.py) - Validation script
- [mcp-server/server.py](./mcp-server/server.py) - MCP server

## MCP Server

Use workflows directly in Claude Code or Cursor via the MCP server. The server exposes each workflow as an MCP tool.

### Claude Code

```bash
claude mcp add -s user dossier -- uvx --from git+https://github.com/liberioai/dossier#subdirectory=mcp-server dossier-mcp
```

### Cursor

Add to your MCP settings:

```json
{
  "mcpServers": {
    "dossier": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/liberioai/dossier#subdirectory=mcp-server", "dossier-mcp"]
    }
  }
}
```

See [mcp-server/README.md](./mcp-server/README.md) for details.

## Development

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Setup

```bash
git clone https://github.com/liberioai/dossier.git
cd dossier
make setup
```

### Commands

```bash
make test      # Format + lint + run all tests
make validate  # Validate workflow files against schema
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT
