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
    FieldEvidenceDrugId,
    FieldEvidenceId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_target_disease_association_cancer_biomarkers_has_molecule: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetEvidence,
            exploded_field=FieldEvidenceBiomarkersGeneExpression,
            predicate=PushdownEqualityPredicate(FieldEvidenceSourceId, "cancer_biomarkers"),
        ),
        primary_id=NewUuidExpression(),
        source=FieldEvidenceId,
        target=FieldEvidenceDrugId,
        label=EdgeLabel.HAS_MOLECULE,
        properties=[],
    )
)
