"""Acquisition definition that acquires edges from evidence to pathways."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import PushdownEqualityPredicate
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidencePathways,
    FieldEvidencePathwaysElementId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_disease_association_inferred_from_pathway_slapenrich: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetEvidence,
            exploded_field=FieldEvidencePathways,
            predicate=PushdownEqualityPredicate(FieldEvidenceSourceId, "slapenrich"),
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidencePathwaysElementId,
        label=EdgeLabel.INFERRED_FROM,
        properties=[],
    )
)
