"""Acquisition definition that acquires 'has child' edges for molecules."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMolecule,
    FieldMoleculeChildChemblIds,
    FieldMoleculeChildChemblIdsElement,
    FieldMoleculeId,
)

edge_molecule_has_child: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMolecule,
        exploded_field=FieldMoleculeChildChemblIds,
    ),
    primary_id=NewUuidExpression(),
    source=FieldMoleculeId,
    target=FieldMoleculeChildChemblIdsElement,
    label="HAS_CHILD_MOLECULE",
    properties=[],
)
