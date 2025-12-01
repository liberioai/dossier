# Dossier MCP Server

MCP server that exposes Dossier workflows as **tools**. Each workflow becomes a callable tool with its inputs as parameters.

> **Note**: This server only exposes tools. It does not provide prompts or resources.

## Installation

### Claude Code

```bash
claude mcp add -s user dossier -- uvx --from git+https://github.com/liberioai/dossier#subdirectory=mcp-server dossier-mcp
```

If you hit rate limits, set `GITHUB_TOKEN` in your environment or add it to the server config in `~/.claude/settings.json`.

### Cursor

Add to your MCP settings:

```json
{
  "mcpServers": {
    "dossier": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/liberioai/dossier#subdirectory=mcp-server", "dossier-mcp"],
      "env": {
        "GITHUB_TOKEN": "your_token_here"
      }
    }
  }
}
```

> **Note**: `GITHUB_TOKEN` is recommended to avoid rate limiting. Without it, you're limited to 60 requests/hour which can cause tool listing to fail.

## Usage

Once installed, workflows appear as tools. For example:

- `create-workflow` - Create a new workflow file
- `readme-reality-check` - Compare README promises vs implementation

The server fetches workflows directly from GitHub, so you always get the latest version. Workflow list is cached for 1 hour.

## Development

This is a separate Python project from the root dossier repo.

```bash
cd mcp-server
uv sync --extra dev    # Install dependencies
uv run pytest          # Run tests
uv run python server.py # Run server locally
```

### Architecture

- `server.py` - Main MCP server, exposes `list_tools` and `call_tool`
- `test_server.py` - Tests for the server
- Fetches `.ds.md` files from `workflows/` directory on GitHub
- Parses frontmatter to build tool schemas
