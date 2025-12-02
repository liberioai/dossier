# Dossier

Structured workflow files for AI agents.

## The Problem

When you ask an AI agent to "set up a Python project" or "review this PR", the quality depends entirely on how well you prompt it. Different people get different results. Knowledge isn't shared or reusable.

## The Solution

Dossier provides `.ds.md` files—markdown documents with structured frontmatter that AI agents can follow consistently. Instead of crafting prompts from scratch, you point your agent at a workflow file that contains:

- **Objective**: What the workflow accomplishes
- **Inputs**: What parameters it accepts
- **Steps**: Clear instructions the agent follows
- **Validation**: How to verify success

Workflows are portable across projects, shareable across teams, and version-controlled like code.

## Quick Example

```markdown
---
{
  "schema_version": "1.0.0",
  "title": "Setup Python Project",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Initialize a Python project with uv, ruff, and pytest",
  "inputs": {
    "required": [
      {"name": "project_name", "description": "Name of the project", "type": "string"}
    ]
  }
}
---
# Setup Python Project

Initialize a production-ready Python project.

## Steps

1. **Initialize project**
   - Run `uv init {project_name}`
   - This creates pyproject.toml with basic metadata

2. **Add dev dependencies**
   - Run `uv add --dev ruff pytest`
   - These provide linting and testing

3. **Create structure**
   - Create `src/{project_name}/` for source code
   - Create `tests/` for test files
   - Add `__init__.py` to both directories

## Validation

- [ ] `pyproject.toml` exists with correct project name
- [ ] `uv run pytest` executes without import errors
- [ ] `uv run ruff check .` passes
```

## Try It Now

Paste this into any AI agent (Claude, ChatGPT, etc.) to audit a project's README:

```
Follow this workflow to analyze the current project:
https://raw.githubusercontent.com/liberioai/dossier/main/workflows/documentation/readme-reality-check.ds.md
```

This workflow compares what the README promises vs what's actually implemented, finding gaps, outdated claims, and missing documentation.

## Installation

### MCP Server (Recommended)

Install the MCP server to use workflows as tools in Claude Code or Cursor.

**Claude Code:**
```bash
# Using uvx (comes with uv)
claude mcp add -s user dossier -- uvx --from git+https://github.com/liberioai/dossier#subdirectory=mcp-server dossier-mcp

# Using pipx
claude mcp add -s user dossier -- pipx run --spec git+https://github.com/liberioai/dossier#subdirectory=mcp-server dossier-mcp
```

**Cursor** (add to `~/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "dossier": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/liberioai/dossier#subdirectory=mcp-server", "dossier-mcp"],
      "env": {
        "GITHUB_TOKEN": "<your-token-here>"
      }
    }
  }
}
```

Or with pipx:
```json
{
  "mcpServers": {
    "dossier": {
      "command": "pipx",
      "args": ["run", "--spec", "git+https://github.com/liberioai/dossier#subdirectory=mcp-server", "dossier-mcp"],
      "env": {
        "GITHUB_TOKEN": "<your-token-here>"
      }
    }
  }
}
```

### Direct Use (No Installation)

You can use any workflow without installing the MCP server—just point your AI agent at the raw file URL:

```
Follow this workflow: https://raw.githubusercontent.com/liberioai/dossier/main/workflows/{path}.ds.md
```

## Available Workflows

| Workflow | Description |
|----------|-------------|
| [create-workflow](./workflows/create-workflow.ds.md) | Create new workflow files that pass validation |
| [readme-reality-check](./workflows/documentation/readme-reality-check.ds.md) | Audit README claims against actual code |

## When to Use Workflows

**Use workflows when:**
- The task requires multiple steps with decisions
- You want consistent results across runs
- The process should be shareable and reusable
- Success criteria need to be explicit

**Use regular prompts when:**
- It's a one-off question or simple task
- The task is highly specific to your current context
- You're exploring or brainstorming

## Project Structure

```
workflows/                     # Workflow files (.ds.md)
├── workflow-schema.json       # JSON Schema for frontmatter validation
├── create-workflow.ds.md      # Meta-workflow for creating workflows
└── documentation/
    └── readme-reality-check.ds.md

utils/
├── validate_workflow.py       # Validates workflows against schema
└── tests/

mcp-server/                    # MCP server (separate Python project)
├── server.py                  # Exposes workflows as tools
└── README.md
```

## Creating Your Own Workflows

1. **Start with the meta-workflow**
   ```
   Use the create-workflow tool with description: "A workflow to [your task]"
   ```

2. **Or copy the template manually**
   - Copy an existing workflow from `workflows/`
   - Update the frontmatter (title, objective, inputs, etc.)
   - Write clear steps in the markdown body
   - Add validation criteria

3. **Validate your workflow**
   ```bash
   uv run python utils/validate_workflow.py workflows/your-workflow.ds.md
   ```

## Schema

Workflows use JSON frontmatter validated against [workflow-schema.json](./workflows/workflow-schema.json).

**Required fields:**
- `schema_version`: Always `"1.0.0"`
- `title`: Human-readable name
- `version`: Semantic version of the workflow
- `status`: One of `draft`, `stable`, `deprecated`
- `objective`: Clear statement of what it accomplishes

**Optional fields:**
- `inputs`: Required and optional parameters
- `outputs`: Files or artifacts produced
- `validation`: Success criteria and verification commands
- `category`, `tags`: For organization

See the [schema file](./workflows/workflow-schema.json) for all available fields.

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
make test      # Format, lint, and run all tests
make validate  # Validate all workflow files against schema
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on adding workflows or improving the tooling.

## License

MIT
