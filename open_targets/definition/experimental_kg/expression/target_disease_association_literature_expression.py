"""Expression that builds a primary id for literature index."""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.data.schema import FieldEvidenceLiterature
from open_targets.definition.helper import get_namespaced_expression

target_disease_association_literature_expression: Final[Expression[str]] = get_namespaced_expression(
    "literature_index",
    FieldEvidenceLiterature,
)
