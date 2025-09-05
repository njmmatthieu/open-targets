"""Acquisition definition that acquires nodes of Reactome pathways."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceReactionId,
    FieldEvidenceReactionName,
    FieldEvidenceSourceId,
)

node_reaction: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "reactome"),
    ),
    primary_id=FieldEvidenceReactionId,
    label="REACTION",
    properties=[
        FieldEvidenceReactionName,
    ],
)
