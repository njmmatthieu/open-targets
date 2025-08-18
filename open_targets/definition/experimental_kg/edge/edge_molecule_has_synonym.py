"""Acquisition definition that acquires 'has synonym' edges for molecules."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetMolecule,
    FieldMoleculeId,
    FieldMoleculeSynonyms,
    FieldMoleculeSynonymsElement,
)

edge_molecule_has_synonym: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMolecule,
        exploded_field=FieldMoleculeSynonyms,
    ),
    primary_id=NewUuidExpression(),
    source=FieldMoleculeId,
    target=FieldMoleculeSynonymsElement,
    label="HAS_SYNONYM",
    properties=[],
)
