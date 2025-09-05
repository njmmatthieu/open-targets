"""Acquisition definition that acquires edges from evidence to cell lines."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.adapter.scan_operation_predicate import EqualityExpression
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceDiseaseCellLines,
    FieldEvidenceDiseaseCellLinesElementId,
    FieldEvidenceDiseaseCellLinesElementTissueId,
    FieldEvidenceSourceId,
)
from open_targets.definition.experimental_kg.constant import EdgeLabel

edge_cell_line_sampled_from_tissue: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidenceDiseaseCellLines,
        predicate=EqualityExpression(FieldEvidenceSourceId, "crispr"),
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceDiseaseCellLinesElementId,
    target=FieldEvidenceDiseaseCellLinesElementTissueId,
    label=EdgeLabel.SAMPLED_FROM,
    properties=[],
)
