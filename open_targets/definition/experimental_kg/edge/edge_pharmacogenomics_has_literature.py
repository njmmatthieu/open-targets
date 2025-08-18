"""Acquisition definition that acquires edges from pharmacogenomics evidence to literature entries."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetPharmacogenomics,
    FieldPharmacogenomicsLiterature,
    FieldPharmacogenomicsLiteratureElement,
    FieldPharmacogenomicsStudyId,
)

edge_pharmacogenomics_has_literature: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetPharmacogenomics,
        exploded_field=FieldPharmacogenomicsLiterature,
    ),
    primary_id=NewUuidExpression(),
    source=FieldPharmacogenomicsStudyId,
    target=FieldPharmacogenomicsLiteratureElement,
    label="HAS_LITERATURE",
    properties=[],
)
