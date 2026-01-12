"""Functions for generating the edge/__init__.py file."""

from pathlib import Path, PurePosixPath
from typing import Any

from code_generation.base import GenerationDefinitionBase


def create_edge_render_context() -> dict[str, Any]:
    """Return a jinja context for the edge/__init__.py file."""
    edge_dir = Path("open_targets/definition/reference_kg/edge")

    # Find all Python files except __init__.py
    edge_files = sorted(f.stem for f in edge_dir.glob("*.py") if f.name != "__init__.py")

    # Extract the export name (same as filename)
    edges = [
        {
            "name": filename,
            "module_path": f"open_targets.definition.reference_kg.edge.{filename}",
        }
        for filename in edge_files
    ]

    # Sort by name to ensure consistent output
    edges.sort(key=lambda x: x["name"])

    return {
        "edges": edges,
    }


class GenerationDefinition(GenerationDefinitionBase):
    """Render the open_targets/definition/reference_kg/edge/__init__.py template."""

    template_path = PurePosixPath("open_targets/definition/reference_kg/edge/__init__.py.jinja")

    def create_context(self) -> dict[str, Any]:
        return create_edge_render_context()
