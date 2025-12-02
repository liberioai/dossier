# Dossier MCP Server

MCP server that exposes Dossier workflows as callable tools.

## What This Does

The server connects to the [Dossier workflow repository](https://github.com/liberioai/dossier) and exposes each workflow as an MCP tool. When you call a tool, the server fetches the workflow content and returns it for your AI agent to execute.

**Example interaction in Claude Code:**

```
You: Use the readme-reality-check tool on this project

Claude: [Calls readme-reality-check tool]
        [Receives workflow instructions]
        [Executes the workflow steps]
        [Returns structured findings]
```

## Available Tools

| Tool | Description |
|------|-------------|
| `create-workflow` | Create a new workflow file that passes validation |
| `readme-reality-check` | Compare README promises vs actual implementation |

Tools are discovered automatically from the `workflows/` directory on GitHub. New workflows appear as tools without server updates.

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

## How It Works

1. **On startup**: Server connects to GitHub API
2. **On `tools/list`**: Fetches all `.ds.md` files from `workflows/` directory, parses frontmatter, returns tool definitions with input schemas
3. **On `tools/call`**: Fetches the requested workflow, returns the markdown body (with any provided arguments prepended)

The workflow list is cached for 1 hour to reduce GitHub API calls.

## Tool Input Schemas

Tools automatically get input schemas from workflow frontmatter. For example, this workflow:

```json
{
  "inputs": {
    "required": [
      {"name": "description", "type": "string", "description": "What the workflow does"}
    ],
    "optional": [
      {"name": "category", "type": "string", "description": "Domain folder"}
    ]
  }
}
```

Becomes a tool with:
- Required parameter: `description` (string)
- Optional parameter: `category` (string)

## Limitations

- **Read-only**: The server only reads workflows from GitHub. It doesn't execute them or modify files.
- **No authentication for workflows**: Anyone can read public workflows. The server doesn't verify workflow authenticity.
- **Rate limits**: Without `GITHUB_TOKEN`, you're limited to 60 requests/hour to the GitHub API.

## Development

This is a separate Python project from the root dossier repo.

### Setup

```bash
cd mcp-server
uv sync --extra dev
```

### Run locally

```bash
uv run python server.py
```

### Run tests

```bash
uv run pytest
```

### Architecture

- `server.py` - MCP server implementation
  - `get_workflows()` - Fetches and caches workflow list from GitHub
  - `get_workflow_content()` - Fetches individual workflow content
  - `build_input_schema()` - Converts frontmatter inputs to JSON Schema
  - `list_tools()` - MCP handler for tool discovery
  - `call_tool()` - MCP handler for tool execution
- `test_server.py` - Tests (requires GitHub API access)
