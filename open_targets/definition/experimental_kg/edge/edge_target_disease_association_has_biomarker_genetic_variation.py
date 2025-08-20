"""Acquisition definition that acquires edges from evidence to biomarkers."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBiomarkersGeneticVariation,
    FieldEvidenceBiomarkersGeneticVariationElementId,
    FieldEvidenceId,
)

edge_target_disease_association_has_biomarker_genetic_variation: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetEvidence,
            exploded_field=FieldEvidenceBiomarkersGeneticVariation,
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidenceBiomarkersGeneticVariationElementId,
        label="TARGET_DISEASE_ASSOCIATION_EVIDENCED_BY_HAS_BIOMARKER",
        properties=[],
    )
)
