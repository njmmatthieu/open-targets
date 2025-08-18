from typing import Final

from open_targets.definition.knowledge_graph import KnowledgeGraphDefinition

experimental_kg_definition: Final[KnowledgeGraphDefinition] = KnowledgeGraphDefinition(
    node_definitions=[
        node_biomarker_genetic_variation,
        node_gene_ontology,
    ],
    edge_definitions=[
        edge_disease_biomarker_gene_expression,
    ],
)
