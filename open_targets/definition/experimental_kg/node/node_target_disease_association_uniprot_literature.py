"""Acquisition definition that acquires nodes of UniProt literature evidence."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import PushdownEqualityPredicate
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceConfidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceId,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
    FieldEvidenceTargetModulation,
)

node_target_disease_association_uniprot_literature: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=PushdownEqualityPredicate(FieldEvidenceSourceId, "uniprot_literature"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_UNIPROT_LITERATURE",
        properties=[
            FieldEvidenceConfidence,
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceId,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
            FieldEvidenceTargetModulation,
        ],
    )
)
