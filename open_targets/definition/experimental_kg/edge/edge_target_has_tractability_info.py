"""Acquisition definition that acquires edges from targets to tractability information."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsId,
    FieldTargetsTractability,
    FieldTargetsTractabilityElementId,
)

edge_target_has_tractability_info: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsTractability,
    ),
    primary_id=NewUuidExpression(),
    source=FieldTargetsId,
    target=FieldTargetsTractabilityElementId,
    label="HAS_TRACTABILITY_INFO",
    properties=[],
)
