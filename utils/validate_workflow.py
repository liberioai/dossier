#!/usr/bin/env python3
"""Validate a single workflow file against the JSON schema."""

import argparse
import json
import logging
import os
import sys
from pathlib import Path

import frontmatter
import yaml
from jsonschema import ValidationError, validate

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def get_project_root() -> Path:
    """Get project root from DOSSIER_ROOT env var or auto-detect."""
    root = os.environ.get("DOSSIER_ROOT")
    if root:
        return Path(root)
    # Auto-detect: script is in utils/, so parent is project root
    return Path(__file__).parent.parent


def get_default_schema_path() -> Path:
    """Get default schema path relative to project root."""
    return get_project_root() / "workflows" / "workflow-schema.json"


def validate_workflow(filepath: Path, schema: dict) -> list[str]:
    """Validate a single workflow file. Returns list of errors."""
    errors = []

    try:
        post = frontmatter.load(filepath)
    except (OSError, ValueError, yaml.YAMLError) as e:
        return [f"Could not parse file: {e}"]

    if not post.metadata:
        return ["No frontmatter found"]

    try:
        validate(instance=post.metadata, schema=schema)
    except ValidationError as e:
        errors.append(f"Schema validation error: {e.message}")
        if e.path:
            errors.append(f"  Path: {'.'.join(str(p) for p in e.path)}")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate a workflow file against the JSON schema")
    parser.add_argument("file", type=Path, help="Path to the workflow file (.ds.md)")
    parser.add_argument(
        "--schema",
        type=Path,
        default=get_default_schema_path(),
        help="Path to JSON schema (default: workflows/workflow-schema.json)",
    )

    args = parser.parse_args()

    if not args.file.exists():
        logger.error("File not found: %s", args.file)
        sys.exit(1)

    if not args.schema.exists():
        logger.error("Schema not found: %s", args.schema)
        sys.exit(1)

    schema = json.loads(args.schema.read_text())
    errors = validate_workflow(args.file, schema)

    if errors:
        logger.error("FAIL: %s", args.file)
        for error in errors:
            logger.error("  %s", error)
        sys.exit(1)
    else:
        logger.info("OK: %s", args.file)
        sys.exit(0)


if __name__ == "__main__":
    main()
