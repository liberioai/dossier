.PHONY: setup format lint validate build

setup:
	uv sync --extra dev

format:
	uv run ruff format .

lint:
	uv run ruff check . --fix

validate:
	./test/lint.sh

build:
	uv run ruff format . --check
	uv run ruff check .
	$(MAKE) validate
