"""Acquisition definition that acquires edges from evidence to biological models."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBiologicalModelId,
    FieldEvidenceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_disease_association_derived_from_mouse_model: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidence),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidenceBiologicalModelId,
        label=EdgeLabel.INFERRED_FROM,
        properties=[],
    )
)
