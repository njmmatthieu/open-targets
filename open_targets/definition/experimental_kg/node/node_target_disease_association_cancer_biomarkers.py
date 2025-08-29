"""Acquisition definition that acquires nodes of Cancer Biomarkers evidence."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import PushdownEqualityPredicate
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceBiomarkerName,
    FieldEvidenceConfidence,
    FieldEvidenceDatasourceId,
    FieldEvidenceDrugFromSource,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_cancer_biomarkers: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=PushdownEqualityPredicate(FieldEvidenceDatasourceId, "cancer_biomarkers"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_CANCER_BIOMARKERS",
        properties=[
            FieldEvidenceBiomarkerName,
            FieldEvidenceConfidence,
            FieldEvidenceDrugFromSource,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
        ],
    )
)
