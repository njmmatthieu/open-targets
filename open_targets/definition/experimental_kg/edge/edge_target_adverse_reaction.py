"""Acquisition definition that acquires edges between targets and adverse reactions."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import RowScanOperation
from open_targets.data.schema import (
    DatasetAdverseTargetReactions,
    FieldAdverseTargetReactionsA,
    FieldAdverseTargetReactionsActerm,
    FieldAdverseTargetReactionsAterm,
    FieldAdverseTargetReactionsB,
    FieldAdverseTargetReactionsC,
    FieldAdverseTargetReactionsCterm,
    FieldAdverseTargetReactionsD,
    FieldAdverseTargetReactionsLlr,
    FieldAdverseTargetReactionsMeddraCode,
    FieldAdverseTargetReactionsReactionReactionmeddrapt,
    FieldAdverseTargetReactionsTargetId,
    FieldAdverseTargetReactionsUniqReportIdsByReaction,
    FieldAdverseTargetReactionsUniqReportIdsByTarget,
)

edge_target_adverse_reaction: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetAdverseTargetReactions),
    primary_id=NewUuidExpression(),
    source=FieldAdverseTargetReactionsTargetId,
    target=FieldAdverseTargetReactionsMeddraCode,
    label="TARGET_TO_ADVERSE_REACTION",
    properties=[
        FieldAdverseTargetReactionsActerm,
        FieldAdverseTargetReactionsAterm,
        FieldAdverseTargetReactionsCterm,
        FieldAdverseTargetReactionsLlr,
        FieldAdverseTargetReactionsReactionReactionmeddrapt,
        FieldAdverseTargetReactionsA,
        FieldAdverseTargetReactionsB,
        FieldAdverseTargetReactionsC,
        FieldAdverseTargetReactionsD,
        FieldAdverseTargetReactionsUniqReportIdsByReaction,
        FieldAdverseTargetReactionsUniqReportIdsByTarget,
    ],
)
