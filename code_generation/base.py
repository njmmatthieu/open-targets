"""Base types for code generation templates."""

from abc import ABC, abstractmethod
from pathlib import PurePosixPath
from typing import Any


class GenerationDefinitionBase(ABC):
    """Base class for generation definitions."""

    template_path: PurePosixPath

    @abstractmethod
    def create_context(self) -> dict[str, Any]:
        """Return the template context."""
