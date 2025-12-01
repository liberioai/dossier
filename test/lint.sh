#!/bin/bash
# Validate all workflow files against the schema

set -e

echo "=== Validating workflows ==="

count=0
for f in $(find workflows -name "*.ds.md"); do
    uv run python utils/validate_workflow.py "$f"
    count=$((count + 1))
done

echo ""
echo "Validated $count workflow(s)"
