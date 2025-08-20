"""Acquisition definition that acquires edges from evidence to variants."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidenceVariantId,
)

edge_target_disease_association_has_variant: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=RowScanOperation(dataset=DatasetEvidence),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidenceVariantId,
        label="TARGET_DISEASE_ASSOCIATION_EVIDENCED_BY_HAS_VARIANT",
        properties=[],
    )
)
