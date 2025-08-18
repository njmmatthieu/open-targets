"""Acquisition definition that acquires edges from evidence to URLs."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidenceUrls,
    FieldEvidenceUrlsElementUrl,
)

edge_evidence_has_url: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidenceUrls,
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceId,
    target=FieldEvidenceUrlsElementUrl,
    label="HAS_URL",
    properties=[],
)
