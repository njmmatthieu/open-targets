"""Acquisition definition that acquires 'has child' edges between diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesChildren,
    FieldDiseasesChildrenElement,
    FieldDiseasesId,
)

edge_disease_has_child: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetDiseases,
        exploded_field=FieldDiseasesChildren,
    ),
    primary_id=NewUuidExpression(),
    source=FieldDiseasesId,
    target=FieldDiseasesChildrenElement,
    label="DISEASE_HAS_CHILD",
    properties=[],
)
