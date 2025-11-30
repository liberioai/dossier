# Contributing to Dossier

Thanks for your interest in contributing!

## How to Contribute

1. Fork the repo
2. Add or improve workflows in `workflows/`
3. Submit a PR

## Adding a Workflow

- Use the `.ds.md` extension
- Place in the appropriate `workflows/` subdirectory
- Include clear objectives, steps, and validation criteria
- Test with an LLM before submitting

## Workflow Structure

```markdown
# Workflow: [Name]

## Objective
What this accomplishes

## Prerequisites
What must exist before running

## Steps
1. Step one
2. Step two

## Validation
How to verify success
```

Include JSON frontmatter matching `workflows/workflow-schema.json`. Run `make build` to validate.

## Questions?

Open an issue or discussion on GitHub.
