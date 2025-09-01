"""Expression that builds a primary id for disease-phenotype associations.

To be honest this is a guess, but it's the only way I can think of to
ensure that the primary id is unique.
"""

from typing import Final

from open_targets.adapter.expression import (
    Expression,
)
from open_targets.definition.experimental_kg.expression.database_cross_reference_target_value_expression import (
    database_cross_reference_target_value_expression,
)
from open_targets.definition.helper import get_namespaced_hash_expression

database_cross_reference_target_primary_id_expression: Final[Expression[str]] = get_namespaced_hash_expression(
    "database_cross_reference",
    database_cross_reference_target_value_expression,
)
