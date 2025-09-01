"""Acquisition definition that acquires edges between targets and gene expression biomarkers."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import PushdownEqualityPredicate
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBiomarkersGeneExpression,
    FieldEvidenceId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import target_disease_association_literature_expression

edge_target_disease_association_supported_by_literature: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetEvidence,
            exploded_field=FieldEvidenceBiomarkersGeneExpression,
            predicate=PushdownEqualityPredicate(FieldEvidenceSourceId, "cancer_biomarkers"),
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=target_disease_association_literature_expression,
        label=EdgeLabel.SUPPORTED_BY,
        properties=[],
    )
)
