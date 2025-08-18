"""Acquisition definition that acquires edges between targets and targets."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetInteraction,
    FieldInteractionCount,
    FieldInteractionScoring,
    FieldInteractionTargetA,
    FieldInteractionTargetB,
)

edge_target_target: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetInteraction),
    primary_id=NewUuidExpression(),
    source=FieldInteractionTargetA,
    target=FieldInteractionTargetB,
    label="TARGET_TO_TARGET_ASSOCIATION",
    properties=[
        FieldInteractionCount,
        FieldInteractionScoring,
    ],
)
