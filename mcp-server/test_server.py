"""Tests for the Dossier MCP server."""

import pytest
from server import call_tool, get_workflow_content, get_workflows, list_tools


class TestGetWorkflows:
    """Tests for get_workflows function."""

    def test_returns_list(self):
        """Should return a list of workflows."""
        workflows = get_workflows()
        assert isinstance(workflows, list)

    def test_workflow_structure(self):
        """Each workflow should have name, path, and download_url."""
        workflows = get_workflows()
        assert len(workflows) > 0
        for wf in workflows:
            assert "name" in wf
            assert "path" in wf
            assert "download_url" in wf

    def test_finds_ds_md_files(self):
        """Should only find .ds.md files."""
        workflows = get_workflows()
        for wf in workflows:
            assert wf["path"].endswith(".ds.md")


class TestGetWorkflowContent:
    """Tests for get_workflow_content function."""

    def test_returns_tuple(self):
        """Should return (metadata, body) tuple."""
        workflows = get_workflows()
        assert len(workflows) > 0
        meta, body = get_workflow_content(workflows[0]["path"])
        assert isinstance(meta, dict)
        assert isinstance(body, str)

    def test_metadata_has_required_fields(self):
        """Metadata should have schema_version, title, version, status, objective."""
        workflows = get_workflows()
        meta, _ = get_workflow_content(workflows[0]["path"])
        assert "schema_version" in meta
        assert "title" in meta
        assert "version" in meta
        assert "status" in meta
        assert "objective" in meta

    def test_body_is_markdown(self):
        """Body should be markdown content."""
        workflows = get_workflows()
        _meta, body = get_workflow_content(workflows[0]["path"])
        assert body.startswith("#")


class TestListTools:
    """Tests for list_tools MCP handler."""

    @pytest.mark.asyncio
    async def test_returns_tools(self):
        """Should return list of Tool objects."""
        tools = await list_tools()
        assert isinstance(tools, list)
        assert len(tools) > 0

    @pytest.mark.asyncio
    async def test_tool_has_name_and_description(self):
        """Each tool should have name and description."""
        tools = await list_tools()
        for tool in tools:
            assert tool.name
            assert tool.description


class TestCallTool:
    """Tests for call_tool MCP handler."""

    @pytest.mark.asyncio
    async def test_returns_text_content_list(self):
        """Should return list of TextContent."""
        result = await call_tool("create-workflow", {})
        assert isinstance(result, list)
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_content_has_text(self):
        """Content should have text."""
        result = await call_tool("create-workflow", {})
        assert result[0].type == "text"
        assert result[0].text

    @pytest.mark.asyncio
    async def test_unknown_workflow_raises(self):
        """Should raise ValueError for unknown workflow."""
        with pytest.raises(ValueError, match="Workflow not found"):
            await call_tool("nonexistent-workflow", {})

    @pytest.mark.asyncio
    async def test_arguments_included_in_content(self):
        """Arguments should be included in the content."""
        result = await call_tool("create-workflow", {"description": "Test workflow"})
        assert "Test workflow" in result[0].text
        assert "Provided Arguments" in result[0].text
