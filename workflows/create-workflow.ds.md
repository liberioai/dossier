---
{
  "schema_version": "1.0.0",
  "title": "Create Workflow",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Create a new workflow file that conforms to the dossier schema and passes validation",
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
      "make build succeeds"
    ],
    "verification_commands": [
      {
        "command": "uv run python scripts/validate_workflow.py workflows/{path}",
        "expected": "OK"
      }
    ]
  }
}
---
# Create Workflow

Create a new workflow file that follows the dossier schema.

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
   - Add a `## Steps` section with numbered, actionable steps
   - Each step should be clear enough for an agent to follow
   - Include specific commands, file paths, or checks where relevant
   - Add an `## Output Format` section if the workflow produces a report

6. **Validate**
   - Run `uv run python scripts/validate_workflow.py workflows/{path}`
   - Fix any schema validation errors
   - Run `make build` to ensure full validation passes

## Example Structure

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

## Output Format

[If applicable]
```

## Notes

- Keep workflows focused on a single task
- Prefer concrete steps over abstract guidance
- Include validation criteria so success is measurable
- Reference file paths and commands specifically
