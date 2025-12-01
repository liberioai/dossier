"""Tests for validate_workflow.py."""

from pathlib import Path

from utils.validate_workflow import validate_workflow

MINIMAL_SCHEMA = {
    "type": "object",
    "required": ["schema_version", "title", "version", "status", "objective"],
    "properties": {
        "schema_version": {"type": "string", "const": "1.0.0"},
        "title": {"type": "string"},
        "version": {"type": "string"},
        "status": {"type": "string", "enum": ["draft", "stable", "deprecated"]},
        "objective": {"type": "string"},
    },
}


class TestValidateWorkflow:
    """Tests for validate_workflow function."""

    def test_valid_workflow(self, tmp_path: Path):
        """Valid workflow should return no errors."""
        workflow = tmp_path / "test.ds.md"
        workflow.write_text("""---
{
  "schema_version": "1.0.0",
  "title": "Test Workflow",
  "version": "1.0.0",
  "status": "draft",
  "objective": "Test objective"
}
---
# Test Workflow

Content here.
""")
        errors = validate_workflow(workflow, MINIMAL_SCHEMA)
        assert errors == []

    def test_missing_required_field(self, tmp_path: Path):
        """Missing required field should return error."""
        workflow = tmp_path / "test.ds.md"
        workflow.write_text("""---
{
  "schema_version": "1.0.0",
  "title": "Test Workflow",
  "version": "1.0.0",
  "status": "draft"
}
---
# Test
""")
        errors = validate_workflow(workflow, MINIMAL_SCHEMA)
        assert len(errors) > 0
        assert "objective" in errors[0].lower()

    def test_invalid_status(self, tmp_path: Path):
        """Invalid enum value should return error."""
        workflow = tmp_path / "test.ds.md"
        workflow.write_text("""---
{
  "schema_version": "1.0.0",
  "title": "Test Workflow",
  "version": "1.0.0",
  "status": "invalid",
  "objective": "Test objective"
}
---
# Test
""")
        errors = validate_workflow(workflow, MINIMAL_SCHEMA)
        assert len(errors) > 0
        assert "status" in errors[0].lower() or "invalid" in errors[0].lower()

    def test_wrong_schema_version(self, tmp_path: Path):
        """Wrong schema version should return error."""
        workflow = tmp_path / "test.ds.md"
        workflow.write_text("""---
{
  "schema_version": "2.0.0",
  "title": "Test Workflow",
  "version": "1.0.0",
  "status": "draft",
  "objective": "Test objective"
}
---
# Test
""")
        errors = validate_workflow(workflow, MINIMAL_SCHEMA)
        assert len(errors) > 0

    def test_no_frontmatter(self, tmp_path: Path):
        """File without frontmatter should return error."""
        workflow = tmp_path / "test.ds.md"
        workflow.write_text("# Just markdown\n\nNo frontmatter here.")
        errors = validate_workflow(workflow, MINIMAL_SCHEMA)
        assert errors == ["No frontmatter found"]

    def test_malformed_frontmatter(self, tmp_path: Path):
        """Malformed frontmatter should return error."""
        workflow = tmp_path / "test.ds.md"
        workflow.write_text("""---
{{{not valid yaml or json
---
# Test
""")
        errors = validate_workflow(workflow, MINIMAL_SCHEMA)
        assert len(errors) > 0
