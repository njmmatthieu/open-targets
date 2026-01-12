"""Functions for generating the node/__init__.py file."""

from pathlib import Path, PurePosixPath
from typing import Any

from code_generation.base import GenerationDefinitionBase


def create_node_render_context() -> dict[str, Any]:
    """Return a jinja context for the node/__init__.py file."""
    node_dir = Path("open_targets/definition/reference_kg/node")

    # Find all Python files except __init__.py
    node_files = sorted(f.stem for f in node_dir.glob("*.py") if f.name != "__init__.py")

    # Extract the export name (same as filename)
    nodes = [
        {
            "name": filename,
            "module_path": f"open_targets.definition.reference_kg.node.{filename}",
        }
        for filename in node_files
    ]

    # Sort by name to ensure consistent output
    nodes.sort(key=lambda x: x["name"])

    return {
        "nodes": nodes,
    }


class GenerationDefinition(GenerationDefinitionBase):
    """Render the open_targets/definition/reference_kg/node/__init__.py template."""

    template_path = PurePosixPath("open_targets/definition/reference_kg/node/__init__.py.jinja")

    def create_context(self) -> dict[str, Any]:
        return create_node_render_context()
