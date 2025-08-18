"""Acquisition definition that acquires edges between molecules and drug warnings."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDrugWarnings,
    FieldDrugWarningsChemblIds,
    FieldDrugWarningsChemblIdsElement,
    FieldDrugWarningsCountry,
    FieldDrugWarningsDescription,
    FieldDrugWarningsEfoId,
    FieldDrugWarningsEfoIdForWarningClass,
    FieldDrugWarningsEfoTerm,
    FieldDrugWarningsId,
    FieldDrugWarningsReferences,
    FieldDrugWarningsToxicityClass,
    FieldDrugWarningsWarningType,
    FieldDrugWarningsYear,
)

edge_molecule_drug_warning: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDrugWarnings,
        exploded_field=FieldDrugWarningsChemblIds,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDrugWarningsChemblIdsElement,
    target=FieldDrugWarningsEfoId,
    label="MOLECULE_TO_DRUG_WARNING",
    properties=[
        FieldDrugWarningsEfoIdForWarningClass,
        FieldDrugWarningsEfoTerm,
        FieldDrugWarningsId,
        FieldDrugWarningsToxicityClass,
        FieldDrugWarningsWarningType,
        FieldDrugWarningsYear,
        FieldDrugWarningsCountry,
        FieldDrugWarningsDescription,
        FieldDrugWarningsReferences,
    ],
)
