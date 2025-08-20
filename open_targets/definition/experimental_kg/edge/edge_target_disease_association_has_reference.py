"""Acquisition definition that acquires edges from disease-phenotype evidence to references."""

from typing import Final

from open_targets.adapter.acquisition_definition import AcquisitionDefinition, ExpressionEdgeAcquisitionDefinition
from open_targets.adapter.expression import NewUuidExpression
from open_targets.adapter.output import EdgeInfo
from open_targets.adapter.scan_operation import ExplodingScanOperation
from open_targets.data.schema import (
    DatasetDiseaseToPhenotype,
    FieldDiseaseToPhenotypeDisease,
    FieldDiseaseToPhenotypeEvidenceElementReferences,
    FieldDiseaseToPhenotypeEvidenceElementReferencesElement,
    FieldDiseaseToPhenotypePhenotype,
)
from open_targets.definition.helper import get_arrow_expression

edge_target_disease_association_has_reference: Final[AcquisitionDefinition[EdgeInfo]] = (
    ExpressionEdgeAcquisitionDefinition(
        scan_operation=ExplodingScanOperation(
            dataset=DatasetDiseaseToPhenotype,
            exploded_field=FieldDiseaseToPhenotypeEvidenceElementReferences,
        ),
        primary_id=NewUuidExpression(),
        source=get_arrow_expression(FieldDiseaseToPhenotypeDisease, FieldDiseaseToPhenotypePhenotype),
        target=FieldDiseaseToPhenotypeEvidenceElementReferencesElement,
        label="TARGET_DISEASE_ASSOCIATION_EVIDENCED_BY_HAS_REFERENCE",
        properties=[],
    )
)
