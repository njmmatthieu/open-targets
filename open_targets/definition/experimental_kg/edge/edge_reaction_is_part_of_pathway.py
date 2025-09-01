"""Acquisition definition that acquires 'is a' edges between Reactome pathways."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import PushdownEqualityPredicate
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidencePathways,
    FieldEvidencePathwaysElementId,
    FieldEvidenceReactionId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_reaction_is_part_of_pathway: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidencePathways,
        predicate=PushdownEqualityPredicate(FieldEvidenceSourceId, "reactome"),
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceReactionId,
    target=FieldEvidencePathwaysElementId,
    label=EdgeLabel.IS_PART_OF,
    properties=[],
)
