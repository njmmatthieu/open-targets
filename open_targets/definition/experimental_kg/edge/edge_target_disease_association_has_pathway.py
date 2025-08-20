"""Acquisition definition that acquires edges from evidence to pathways."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidencePathways,
    FieldEvidencePathwaysElementId,
)

edge_target_disease_association_has_pathway: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetEvidence,
            exploded_field=FieldEvidencePathways,
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidencePathwaysElementId,
        label="TARGET_DISEASE_ASSOCIATION_EVIDENCED_BY_HAS_PATHWAY",
        properties=[],
    )
)
