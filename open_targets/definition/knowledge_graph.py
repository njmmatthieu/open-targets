from collections.abc import Sequence
from dataclasses import dataclass

from open_targets.adapter.acquisition_definition import AcquisitionDefinition
from open_targets.adapter.output import EdgeInfo, NodeInfo


@dataclass(frozen=True, kw_only=True)
class KnowledgeGraphDefinition:
    """Definition of a knowledge graph."""

    node_definitions: Sequence[AcquisitionDefinition[NodeInfo]]
    edge_definitions: Sequence[AcquisitionDefinition[EdgeInfo]]
