"""Acquisition definition that acquires nodes of Expression Atlas evidence."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBiosamplesFromSource,
    FieldEvidenceConfidence,
    FieldEvidenceContrast,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceLiterature,
    FieldEvidenceLog2FoldChangePercentileRank,
    FieldEvidenceLog2FoldChangeValue,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceStudyOverview,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_expression_atlas: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=EqualityExpression(FieldEvidenceSourceId, "expression_atlas"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_EXPRESSION_ATLAS",
        properties=[
            FieldEvidenceBiosamplesFromSource,
            FieldEvidenceConfidence,
            FieldEvidenceContrast,
            FieldEvidenceLiterature,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceLog2FoldChangePercentileRank,
            FieldEvidenceLog2FoldChangeValue,
            FieldEvidenceResourceScore,
            FieldEvidenceScore,
            FieldEvidenceStudyId,
            FieldEvidenceStudyOverview,
            FieldEvidenceTargetFromSourceId,
        ],
    )
)
