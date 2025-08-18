"""Acquisition definition that acquires edges from evidence to PMC literature entries."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidencePmcIds,
    FieldEvidencePmcIdsElement,
)

edge_evidence_has_literature_pmc: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidencePmcIds,
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceId,
    target=FieldEvidencePmcIdsElement,
    label="HAS_LITERATURE",
    properties=[],
)
