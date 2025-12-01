# Contributing to Dossier

Thanks for your interest in contributing!

## Adding a Workflow

### End-to-End Flow

1. **Create the workflow** using the create-workflow workflow:
   ```
   Use the create-workflow dossier to create a workflow that [description]
   ```

2. **Place the file** in the appropriate `workflows/` subdirectory

3. **Validate**:
   ```bash
   make validate
   ```

4. **Run tests**:
   ```bash
   make test
   ```

5. **Submit a PR**

### Workflow Requirements

- Use the `.ds.md` extension
- Include JSON frontmatter matching [workflows/workflow-schema.json](./workflows/workflow-schema.json)
- Test with an LLM before submitting

### Minimal Example

```markdown
---
{
  "schema_version": "1.0.0",
  "title": "My Workflow",
  "version": "1.0.0",
  "status": "draft",
  "objective": "What this workflow accomplishes"
}
---
# My Workflow

Brief description.

## Steps

1. **First step** - Details
2. **Second step** - Details
```

### Manual Validation

```bash
uv run python utils/validate_workflow.py workflows/path/to/your-workflow.ds.md
```

## Modifying the MCP Server

The `mcp-server/` directory is a separate Python project with its own dependencies.

```bash
cd mcp-server
uv sync --extra dev
uv run pytest           # Run tests
uv run python server.py # Run locally
```

## Questions?

Open an issue or discussion on GitHub.
