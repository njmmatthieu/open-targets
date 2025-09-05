"""Acquisition definition that acquires 'is a' edges between Reactome pathways."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseId,
    FieldEvidencePathways,
    FieldEvidencePathwaysElementId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_pathway_annotated_with_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidencePathways,
        predicate=EqualityExpression(FieldEvidenceSourceId, "reactome"),
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidencePathwaysElementId,
    target=FieldEvidenceDiseaseId,
    label=EdgeLabel.ANNOTATED_WITH,
    properties=[],
)
