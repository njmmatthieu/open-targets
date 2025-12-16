# type: ignore[reportUnknownMemberType]

"""A pipeline to build Open Targets platform data as a BioCypher KG."""

import logging

from biocypher import BioCypher

from open_targets.adapter.context import AcquisitionContext
from open_targets.definition.experimental_kg.kg import experimental_kg_definition

from open_targets.definition.experimental_kg.edge import (
    edge_mechanism_of_action_has_target_target,
    edge_molecule_derived_from_molecule,
    edge_molecule_has_mechanism_of_action,
)
from open_targets.definition.experimental_kg.node import (
    node_mechanism_of_action,
    node_molecule,
    node_target,
)

def main():
    """Run the import using BioCypher and the Open Targets adapter."""
    # Start BioCypher
    bc = BioCypher(
        biocypher_config_path="config/biocypher_config.yaml",
    )
    # Set logging level to ERROR only
    logging.getLogger("biocypher").setLevel(logging.ERROR)

    # Check the schema
    bc.show_ontology_structure()

    # Open Targets
    context = AcquisitionContext(
        node_definitions=[node_mechanism_of_action,
                          node_molecule,
                          node_target,
                          ],
        edge_definitions=[edge_mechanism_of_action_has_target_target,
                          edge_molecule_has_mechanism_of_action,
                          edge_molecule_derived_from_molecule,
                          ],
        datasets_location="data/ot_files",
        # limit=1000,
    )

    count = 1
    for node_definition in context.node_definitions:
        print(f"{count}: {node_definition.label}")
        count += 1
        bc.write_nodes(context.get_acquisition_generator(node_definition))
    for edge_definition in context.edge_definitions:
        print(f"{count}: {edge_definition.label}")
        count += 1
        bc.write_edges(context.get_acquisition_generator(edge_definition))

    # Post import functions
    import_file = bc.write_import_call()
    bc.summary()

    print(import_file)


if __name__ == "__main__":
    main()
