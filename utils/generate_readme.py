#!/usr/bin/env python3
"""Generate README files for workflow directories from frontmatter."""

import sys
from pathlib import Path

import frontmatter


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_workflows(directory: Path) -> list[dict]:
    """Return sorted list of {name, title, objective} for workflows in directory."""
    workflows = []
    for f in sorted(directory.glob("*.ds.md")):
        post = frontmatter.load(f)
        name = f.stem.removesuffix(".ds")
        workflows.append(
            {
                "name": name,
                "title": post.metadata.get("title", name),
                "objective": post.metadata.get("objective", ""),
            }
        )
    return workflows


def process_category(subdir: Path) -> dict | None:
    """Process a category directory. Returns category info or None if no workflows."""
    workflows = get_workflows(subdir)
    if not workflows:
        return None

    readme_path = subdir / "README.md"

    # Extract title and description from existing README
    title = subdir.name.replace("-", " ").title() + " Workflows"
    long_desc = ""

    if readme_path.exists():
        lines = readme_path.read_text().splitlines()
        if lines and lines[0].startswith("# "):
            title = lines[0][2:]
        # Find first non-empty line after the title
        for i, line in enumerate(lines):
            if line.startswith("# "):
                for j in range(i + 1, len(lines)):
                    if lines[j].strip() and not lines[j].startswith("#"):
                        long_desc = lines[j].strip()
                        break
                break

    short_desc = long_desc.split(".")[0] if long_desc else ""

    return {
        "name": subdir.name,
        "title": title,
        "long_desc": long_desc,
        "short_desc": short_desc,
        "workflows": workflows,
        "readme_path": readme_path,
    }


def generate_category_readme(title: str, description: str, workflows: list[dict]) -> str:
    """Generate README content for a category."""
    lines = [
        f"# {title}",
        "",
        description,
        "",
        "## Available Workflows",
        "",
        "| Workflow | Description |",
        "|----------|-------------|",
    ]

    lines.extend(f"| [{w['name']}](./{w['name']}.ds.md) | {w['objective']} |" for w in workflows)
    lines.append("")
    return "\n".join(lines)


def generate_root_readme(categories: list[dict]) -> str:
    """Generate README content for workflows/ root directory."""
    lines = [
        "# Workflows",
        "",
        "Step-by-step instructions for AI agents to complete tasks.",
        "",
        "## Getting Started",
        "",
        "Use [create-workflow](./create-workflow.ds.md) to create new workflows that pass validation.",
        "",
        "## Categories",
        "",
        "| Category | Description |",
        "|----------|-------------|",
    ]

    lines.extend(f"| [{c['name']}](./{c['name']}/) | {c['short_desc']} |" for c in categories)
    lines.append("")
    return "\n".join(lines)


def update_file(path: Path, content: str, *, check_only: bool, out_of_sync: list) -> None:
    """Update a file or record it as out of sync."""
    if path.exists() and path.read_text() == content:
        return

    if check_only:
        out_of_sync.append(path)
    else:
        path.write_text(content)
        print(f"Updated {path}")


def main():
    check_only = "--check" in sys.argv

    root = get_project_root()
    workflows_dir = root / "workflows"

    out_of_sync = []

    # Process each category subdirectory
    categories = []
    for subdir in sorted(workflows_dir.iterdir()):
        if not subdir.is_dir():
            continue
        cat = process_category(subdir)
        if cat:
            categories.append(cat)

    # Update category READMEs
    for cat in categories:
        content = generate_category_readme(cat["title"], cat["long_desc"], cat["workflows"])
        update_file(cat["readme_path"], content, check_only=check_only, out_of_sync=out_of_sync)

    # Update root workflows/README.md
    root_readme = workflows_dir / "README.md"
    root_content = generate_root_readme(categories)
    update_file(root_readme, root_content, check_only=check_only, out_of_sync=out_of_sync)

    if check_only:
        if out_of_sync:
            print("READMEs out of sync:")
            for p in out_of_sync:
                print(f"  {p}")
            print("\nRun: uv run python utils/generate_readme.py")
            sys.exit(1)
        print("All READMEs are in sync")
    else:
        print("All READMEs are up to date")

    sys.exit(0)


if __name__ == "__main__":
    main()
