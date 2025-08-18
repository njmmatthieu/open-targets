"""Acquisition definition that acquires 'linked to target' edges for molecules."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMolecule,
    FieldMoleculeId,
    FieldMoleculeLinkedTargetsRows,
    FieldMoleculeLinkedTargetsRowsElement,
)

edge_molecule_linked_target: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMolecule,
        exploded_field=FieldMoleculeLinkedTargetsRows,
    ),
    primary_id=NewUuidExpression(),
    source=FieldMoleculeId,
    target=FieldMoleculeLinkedTargetsRowsElement,
    label="LINKED_TO_TARGET",
    properties=[],
)
