"""Acquisition definition that acquires edges between molecules and targets."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceConfidence,
    FieldEvidenceDatasourceId,
    FieldEvidenceDrugId,
    FieldEvidenceLiterature,
    FieldEvidencePublicationFirstAuthor,
    FieldEvidencePublicationYear,
    FieldEvidenceReleaseDate,
    FieldEvidenceReleaseVersion,
    FieldEvidenceResourceScore,
    FieldEvidenceScore,
    FieldEvidenceSourceId,
    FieldEvidenceStatisticalMethod,
    FieldEvidenceStatisticalMethodOverview,
    FieldEvidenceTargetId,
)

edge_molecule_target: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetEvidence),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceDrugId,
    target=FieldEvidenceTargetId,
    label="MOLECULE_TO_TARGET_ASSOCIATION",
    properties=[
        FieldEvidenceDatasourceId,
        FieldEvidenceLiterature,
        FieldEvidenceScore,
        FieldEvidenceConfidence,
        FieldEvidenceResourceScore,
        FieldEvidenceReleaseDate,
        FieldEvidenceReleaseVersion,
        FieldEvidenceSourceId,
        FieldEvidenceStatisticalMethod,
        FieldEvidenceStatisticalMethodOverview,
        FieldEvidencePublicationFirstAuthor,
        FieldEvidencePublicationYear,
    ],
)
