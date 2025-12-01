#!/usr/bin/env python3
"""Dossier MCP Server - Exposes workflows as tools from GitHub."""

import asyncio
import base64
import logging
import time
from dataclasses import dataclass, field

import frontmatter
import yaml
from ghapi.all import GhApi
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

REPO_OWNER = "liberioai"
REPO_NAME = "dossier"
WORKFLOWS_PATH = "workflows"
CACHE_TTL = 3600  # 1 hour

server = Server("dossier-mcp")
api = GhApi()
logger = logging.getLogger(__name__)


@dataclass
class WorkflowCache:
    """Cache for workflow list."""

    workflows: list[dict] = field(default_factory=list)
    timestamp: float = 0

    def is_valid(self) -> bool:
        """Check if cache is still valid."""
        return bool(self.workflows) and (time.time() - self.timestamp) < CACHE_TTL

    def update(self, workflows: list[dict]) -> None:
        """Update cache with new workflows."""
        self.workflows = workflows
        self.timestamp = time.time()


_cache = WorkflowCache()


def get_workflows() -> list[dict]:
    """Fetch all .ds.md files from the workflows directory (cached for 1 hour)."""
    if _cache.is_valid():
        return _cache.workflows

    workflows = []

    def scan_directory(path: str):
        contents = api.repos.get_content(REPO_OWNER, REPO_NAME, path)
        for item in contents:
            if item.type == "dir":
                scan_directory(item.path)
            elif item.type == "file" and item.name.endswith(".ds.md"):
                workflows.append(
                    {
                        "name": item.name.replace(".ds.md", ""),
                        "path": item.path,
                        "download_url": item.download_url,
                    }
                )

    scan_directory(WORKFLOWS_PATH)
    _cache.update(workflows)
    return workflows


def get_workflow_content(path: str) -> tuple[dict, str]:
    """Fetch and parse a workflow file. Returns (frontmatter, body)."""
    content = api.repos.get_content(REPO_OWNER, REPO_NAME, path)
    raw = base64.b64decode(content.content).decode("utf-8")
    parsed = frontmatter.loads(raw)
    return parsed.metadata, parsed.content


def build_input_schema(meta: dict) -> dict:
    """Build JSON schema for tool inputs from workflow metadata."""
    properties = {}
    required = []

    for inp in meta.get("inputs", {}).get("required", []):
        properties[inp["name"]] = {
            "type": inp.get("type", "string"),
            "description": inp.get("description", ""),
        }
        required.append(inp["name"])

    for inp in meta.get("inputs", {}).get("optional", []):
        properties[inp["name"]] = {
            "type": inp.get("type", "string"),
            "description": inp.get("description", ""),
        }
        if "default" in inp:
            properties[inp["name"]]["default"] = inp["default"]

    return {
        "type": "object",
        "properties": properties,
        "required": required,
    }


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available workflow tools."""
    tools = []
    for wf in get_workflows():
        try:
            meta, _ = get_workflow_content(wf["path"])
            tools.append(
                Tool(
                    name=wf["name"],
                    description=meta.get("objective", meta.get("title", wf["name"])),
                    inputSchema=build_input_schema(meta),
                )
            )
        except (KeyError, ValueError, yaml.YAMLError) as e:
            logger.warning("Skipping workflow %s: %s", wf["name"], e)
            continue
    return tools


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Execute a workflow tool."""
    workflows = get_workflows()
    workflow = next((wf for wf in workflows if wf["name"] == name), None)

    if not workflow:
        msg = f"Workflow not found: {name}"
        raise ValueError(msg)

    _meta, body = get_workflow_content(workflow["path"])

    # Build context with arguments if provided
    context = ""
    if arguments:
        context = "## Provided Arguments\n\n"
        for key, value in arguments.items():
            context += f"- **{key}**: {value}\n"
        context += "\n---\n\n"

    return [
        TextContent(
            type="text",
            text=f"{context}{body}",
        )
    ]


async def _run():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main():
    """Entry point for the MCP server."""
    asyncio.run(_run())


if __name__ == "__main__":
    main()
