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

edge_evidence_has_biological_model: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidence),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceId,
    target=FieldEvidenceBiologicalModelId,
    label="HAS_BIOLOGICAL_MODEL",
    properties=[],
)
