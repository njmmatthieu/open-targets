"""Acquisition definition that acquires nodes of SLAPenrich evidence."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionNodeAcquisitionDefinition
from open_targets.adapter.output import NodeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.adapter.scan_operation_predicate import PushdownEqualityPredicate
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseFromSource,
    FieldEvidenceDiseaseFromSourceMappedId,
    FieldEvidenceId,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceTargetFromSourceId,
)

node_target_disease_association_slapenrich: Final[AcquisitionDefinition[NodeInfo]] = (
    ExpressionNodeAcquisitionDefinition(
        scan_operation=RowScanOperation(
            dataset=DatasetEvidence,
            predicate=PushdownEqualityPredicate(FieldEvidenceSourceId, "slapenrich"),
        ),
        primary_id=FieldEvidenceId,
        label="TARGET_DISEASE_ASSOCIATION_SLAPENRICH",
        properties=[
            FieldEvidenceDiseaseFromSource,
            FieldEvidenceDiseaseFromSourceMappedId,
            FieldEvidenceResourceScore,
            FieldEvidenceScore,
            FieldEvidenceTargetFromSourceId,
        ],
    )
)
