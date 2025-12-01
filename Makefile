.PHONY: setup test validate

setup:
	uv sync --extra dev

test:
	uv run ruff format .
	uv run ruff check .
	uv run pytest
	cd mcp-server && uv sync --extra dev && uv run pytest

validate:
	./test/lint.sh
