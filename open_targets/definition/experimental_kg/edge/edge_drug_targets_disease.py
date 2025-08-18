"""Acquisition definition that acquires edges from drugs to diseases via drug indications."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetKnownDrugsAggregated,
    FieldKnownDrugsAggregatedDiseaseId,
    FieldKnownDrugsAggregatedDrugId,
)

edge_drug_targets_disease: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetKnownDrugsAggregated),
    primary_id=NewUuidExpression(),
    source=FieldKnownDrugsAggregatedDrugId,
    target=FieldKnownDrugsAggregatedDiseaseId,
    label="DRUG_TARGETS_DISEASE",
    properties=[],
)
