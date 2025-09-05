"""Acquisition definition that acquires nodes of ChEMBL evidence."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceClinicalPhase,
    FieldEvidenceClinicalStatus,
    FieldEvidenceCohortPhenotypes,
    FieldEvidenceDirectionOnTrait,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStudyId,
    FieldEvidenceStudyStartDate,
    FieldEvidenceStudyStopReason,
    FieldEvidenceStudyStopReasonCategories,
    FieldEvidenceVariantEffect,
)

node_target_disease_association_chembl: Final[AcquisitionDefinition[NodeInfo]] = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(
        dataset=DatasetEvidence,
        predicate=EqualityExpression(FieldEvidenceSourceId, "chembl"),
    ),
    primary_id=FieldEvidenceId,
    label="TARGET_DISEASE_ASSOCIATION_CHEMBL",
    properties=[
        FieldEvidenceClinicalPhase,
        FieldEvidenceClinicalStatus,
        FieldEvidenceCohortPhenotypes,
        FieldEvidenceDirectionOnTrait,
        FieldEvidenceDiseaseFromSource,
        FieldEvidenceDiseaseFromSourceMappedId,
        FieldEvidenceScore,
        FieldEvidenceStudyId,
        FieldEvidenceStudyStartDate,
        FieldEvidenceStudyStopReason,
        FieldEvidenceStudyStopReasonCategories,
        FieldEvidenceVariantEffect,
    ],
)
