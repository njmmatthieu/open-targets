"""Functions for generating the expression/__init__.py file."""

from pathlib import Path, PurePosixPath
from typing import Any

from code_generation.base import GenerationDefinitionBase


def create_expression_render_context() -> dict[str, Any]:
    """Return a jinja context for the expression/__init__.py file."""
    expression_dir = Path("open_targets/definition/reference_kg/expression")

    # Find all Python files except __init__.py
    expression_files = sorted(f.stem for f in expression_dir.glob("*.py") if f.name != "__init__.py")

    # Extract the export name (same as filename)
    expressions = [
        {
            "name": filename,
            "module_path": f"open_targets.definition.reference_kg.expression.{filename}",
        }
        for filename in expression_files
    ]

    # Sort by name to ensure consistent output
    expressions.sort(key=lambda x: x["name"])

    return {
        "expressions": expressions,
    }


class GenerationDefinition(GenerationDefinitionBase):
    """Render the open_targets/definition/reference_kg/expression/__init__.py template."""

    template_path = PurePosixPath("open_targets/definition/reference_kg/expression/__init__.py.jinja")

    def create_context(self) -> dict[str, Any]:
        return create_expression_render_context()
