"""Acquisition definition that acquires edges between drugs (molecules) and genes (targets) using the known drug dataset."""

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
from open_targets.definition.node_shared import node_static_properties

edge_drug_target: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetMolecule,
        exploded_field=FieldMoleculeLinkedTargetsRows,
    ),
    primary_id=NewUuidExpression(),
    source=FieldMoleculeId,
    target=FieldMoleculeLinkedTargetsRowsElement,
    label="DRUG_TO_GENE_ASSOCIATION",
    properties=node_static_properties,
)
