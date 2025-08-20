"""Acquisition definition that acquires edges from evidence to diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseId,
    FieldEvidenceId,
)

edge_target_disease_association_for_disease: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidence),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidenceDiseaseId,
        label="TARGET_DISEASE_ASSOCIATION_EVIDENCED_BY_FOR_DISEASE",
        properties=[],
    )
)
