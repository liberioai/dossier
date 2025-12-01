---
{
  "schema_version": "1.0.0",
  "title": "Create Workflow",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Create a new workflow file that conforms to the workflow schema and passes validation",
  "category": ["authoring", "meta"],
  "tags": ["workflow", "create", "template"],
  "estimated_duration": {
    "min_minutes": 5,
    "max_minutes": 15
  },
  "inputs": {
    "required": [
      {
        "name": "description",
        "description": "What the workflow should accomplish",
        "type": "string",
        "example": "A workflow to review pull requests for security issues"
      }
    ],
    "optional": [
      {
        "name": "category",
        "description": "Domain folder to place the workflow in",
        "type": "string",
        "example": "security"
      },
      {
        "name": "filename",
        "description": "Name for the workflow file (without .ds.md extension)",
        "type": "string"
      }
    ]
  },
  "outputs": {
    "files": [
      {
        "path": "workflows/{category}/{filename}.ds.md",
        "description": "The new workflow file"
      }
    ]
  },
  "validation": {
    "success_criteria": [
      "Workflow file passes schema validation",
      "make validate succeeds"
    ],
    "verification_commands": [
      {
        "command": "uv run python utils/validate_workflow.py workflows/{path}",
        "expected": "OK"
      }
    ]
  }
}
---
# Create Workflow

Create a new workflow file that follows the workflow schema.

## Steps

1. **Understand the Request**
   - What task should this workflow guide?
   - Who is the target audience (developer, ops, etc.)?
   - What tools or context are required?

2. **Read the Schema**
   - Read `workflows/workflow-schema.json` to understand required and optional fields
   - Required: schema_version, title, version, status, objective
   - Optional: category, tags, tools_required, inputs, outputs, validation, etc.

3. **Determine Placement**
   - If category provided, use `workflows/{category}/`
   - If no category, ask user or infer from the workflow's domain
   - Create the category folder if it doesn't exist

4. **Create the Frontmatter**
   - Use JSON format inside `---` delimiters
   - Set `schema_version` to match the version in `workflows/workflow-schema.json`
   - Set `status` to "draft" for new workflows
   - Write a clear, specific `objective`
   - Add relevant `category` and `tags`
   - Define `inputs` if the workflow needs parameters
   - Define `outputs` if the workflow produces files/artifacts
   - Add `validation.success_criteria` to define what success looks like

5. **Write the Body**
   - Start with a brief description of what the workflow does
   - Add sections as appropriate (see Recommended Body Structure below)
   - Each step should be clear enough for an agent to follow
   - Include specific commands, file paths, or checks where relevant

6. **Validate**
   - Run `uv run python utils/validate_workflow.py workflows/{path}`
   - Fix any schema validation errors
   - Run `make validate` to ensure full validation passes

## Recommended Body Structure

Not all sections are needed for every workflow. Use what makes sense:

| Section | When to Include |
|---------|-----------------|
| `## Objective` | When frontmatter objective needs elaboration |
| `## Prerequisites` | When tools, files, or permissions are required |
| `## Context to Gather` | When the agent needs to analyze the project first |
| `## Decision Points` | When there are multiple approaches to choose from |
| `## Steps` | Always - the core of the workflow |
| `## Validation` | When success criteria need detailed checks |
| `## Troubleshooting` | When common issues are known |
| `## Output Format` | When the workflow produces a report |

### Context to Gather Example

```markdown
## Context to Gather

Before proceeding, analyze:
- [ ] Project structure and file layout
- [ ] Existing configuration files
- [ ] Technology stack (package.json, requirements.txt, etc.)
```

### Decision Points Example

```markdown
## Decision Points

### Database Choice
**Based on**: Project requirements and existing infrastructure

**Options**:
- PostgreSQL - Use when you need relational data with complex queries
- MongoDB - Use when you need flexible schema and document storage
- SQLite - Use for local development or small deployments
```

### Troubleshooting Example

```markdown
## Troubleshooting

### Issue: Permission denied
**Cause**: Missing write access to target directory
**Solution**: Check directory permissions or run with appropriate access
```

## Minimal Example

```markdown
---
{
  "schema_version": "1.0.0",
  "title": "Your Workflow Title",
  "version": "1.0.0",
  "status": "draft",
  "objective": "Clear statement of what this accomplishes",
  "category": ["domain"],
  "tags": ["relevant", "tags"]
}
---
# Your Workflow Title

Brief description.

## Steps

1. **First Step**
   - Details

2. **Second Step**
   - Details
```

## Notes

- Keep workflows focused on a single task
- Prefer concrete steps over abstract guidance
- Include validation criteria so success is measurable
- Reference file paths and commands specifically
- Add Context to Gather when project analysis is needed
- Add Troubleshooting for workflows that commonly fail
