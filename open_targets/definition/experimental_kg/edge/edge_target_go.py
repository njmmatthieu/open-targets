"""Acquisition definition that acquires edges between targets and GO terms."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetTargets,
    FieldTargetsGo,
    FieldTargetsGoElementAspect,
    FieldTargetsGoElementEcoId,
    FieldTargetsGoElementEvidence,
    FieldTargetsGoElementGeneProduct,
    FieldTargetsGoElementId,
    FieldTargetsGoElementSource,
    FieldTargetsId,
)

edge_target_go: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetTargets,
        exploded_field=FieldTargetsGo,
    ),
    primary_id=NewUuidExpression(),
    source=FieldTargetsId,
    target=FieldTargetsGoElementId,
    label="TARGET_TO_GO_TERM_ASSOCIATION",
    properties=[
        FieldTargetsGoElementSource,
        FieldTargetsGoElementEvidence,
        FieldTargetsGoElementEcoId,
        FieldTargetsGoElementAspect,
        FieldTargetsGoElementGeneProduct,
    ],
)
