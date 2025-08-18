"""Acquisition definition that acquires 'has child' edges between Reactome pathways."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetReactome,
    FieldReactomeChildren,
    FieldReactomeChildrenElement,
    FieldReactomeId,
)

edge_reactome_has_child: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetReactome,
        exploded_field=FieldReactomeChildren,
    ),
    primary_id=NewUuidExpression(),
    source=FieldReactomeId,
    target=FieldReactomeChildrenElement,
    label="REACTOME_HAS_CHILD",
    properties=[],
)
