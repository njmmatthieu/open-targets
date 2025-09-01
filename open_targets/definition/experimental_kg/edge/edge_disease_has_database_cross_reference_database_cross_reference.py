"""Acquisition definition that acquires 'has cross-reference' edges for diseases."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseases,
    FieldDiseasesDbXRefs,
    FieldDiseasesId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel
from open_targets.definition.experimental_kg.expression import database_cross_reference_disease_primary_id_expression

edge_disease_has_database_cross_reference_database_cross_reference: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetDiseases,
            exploded_field=FieldDiseasesDbXRefs,
        ),
        primary_id=NewUuidExpression(),
        source=FieldDiseasesId,
        target=database_cross_reference_disease_primary_id_expression,
        label=EdgeLabel.HAS_DATABASE_CROSS_REFERENCE,
        properties=[],
    )
)
