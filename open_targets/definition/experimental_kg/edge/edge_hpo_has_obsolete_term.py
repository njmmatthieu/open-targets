"""Acquisition definition that acquires 'has obsolete term' edges for HPO phenotypes."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetHpo,
    FieldHpoId,
    FieldHpoObsoleteTerms,
    FieldHpoObsoleteTermsElement,
)

edge_hpo_has_obsolete_term: Final[AcquisitionDefinition[EdgeInfo]] = ExpressionEdgeAcquisitionDefinition(
    scan_operation=ExplodingScanOperation(
        dataset=DatasetHpo,
        exploded_field=FieldHpoObsoleteTerms,
    ),
    primary_id=NewUuidExpression(),
    source=FieldHpoId,
    target=FieldHpoObsoleteTermsElement,
    label="HPO_HAS_OBSOLETE_TERM",
    properties=[],
)
