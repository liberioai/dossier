# Dossier

A collection of structured instructions for AI agents.

## What is a Dossier?

A dossier is a markdown file with a specific structure that AI agents (Claude, ChatGPT, Cursor, etc.) can follow to complete tasks. Instead of writing scripts, you write clear instructions with objectives, steps, and validation criteria.

## Contents

| Folder | Description |
|--------|-------------|
| [workflows](./workflows/) | Step-by-step task automation |
| contexts | Conversation starters and personas (coming soon) |

## Development

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)

### Setup

```bash
git clone https://github.com/liberioai/dossier.git
cd dossier
make setup
```

### Commands

```bash
make format   # Format code
make lint     # Lint and auto-fix
make build    # Run all checks (CI)
```
