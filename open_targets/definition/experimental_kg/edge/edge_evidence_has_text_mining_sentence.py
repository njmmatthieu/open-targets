"""Acquisition definition that acquires edges from evidence to text mining sentences."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetEvidence,
    FieldEvidenceId,
    FieldEvidenceTextMiningSentences,
    FieldEvidenceTextMiningSentencesElementText,
)

edge_evidence_has_text_mining_sentence: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetEvidence,
        exploded_field=FieldEvidenceTextMiningSentences,
    ),
    primary_id=NewUuidExpression(),
    source=FieldEvidenceId,
    target=FieldEvidenceTextMiningSentencesElementText,
    label="HAS_TEXT_MINING_SENTENCE",
    properties=[],
)
