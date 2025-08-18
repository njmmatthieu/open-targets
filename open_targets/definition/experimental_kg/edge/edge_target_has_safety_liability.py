"""Acquisition definition that acquires edges from targets to safety liabilities."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsId,
    FieldTargetsSafetyLiabilities,
    FieldTargetsSafetyLiabilitiesElementEventId,
)

edge_target_has_safety_liability: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsSafetyLiabilities,
    ),
    primary_id=NewUuidExpression(),
    source=FieldTargetsId,
    target=FieldTargetsSafetyLiabilitiesElementEventId,
    label="HAS_SAFETY_LIABILITY",
    properties=[],
)
