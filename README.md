# BioCypher Open Targets Data (24.09) Adapter

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

This repository contains a [BioCypher](https://biocypher.org) adapter for Open
Targets data version 24.09. The project is currently under active development.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Node and Edge Types](#node-and-edge-types)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Not So Quick Start](#not-so-quick-start)
- [Open Targets Data Schema](#open-targets-data-schema)
- [Custom Node/Edge Definitions](#custom-nodeedge-definitions)
- [Code Generation](#code-generation)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)

## Overview

BioCypher's modular design enables the use of different adapters to consume
various data sources and produce knowledge graphs. This adapter serves as a
["secondary
adapter"](https://biocypher.org/latest/learn/tutorials/tutorial003_adapters/)
for [Open Targets data](https://platform.opentargets.org/downloads), meaning it
adapts a pre-harmonised composite of atomic resources via the Open Targets
pipeline. The adapter includes predefined sets of node types (entities) and edge
types (relationships), or in the language of this adapter, presets of node and
edge `definitions`. A script is provided to run BioCypher with the adapter,
creating a knowledge graph with all predefined nodes and edges. On a consumer
laptop, building the full graph typically takes 1-2 hours.

## Features

- Converts Open Targets data (version 24.09) into BioCypher-compatible format
- Includes comprehensive predefined sets of node types and edge types (node and edge definition presets)
- Uses declarative syntax to minimize code needed for graph schema construction
- Powered by [duckdb](https://duckdb.org/) for fast and memory-efficient processing
- Implements true streaming from datasets to BioCypher with minimal intermediate memory usage
- Type-safe schema representation with Python classes for all datasets and fields

## Node and Edge Types

The adapter includes a comprehensive set of node and edge definitions covering:

**Core Entities:**
- Targets (genes, proteins)
- Diseases
- Molecules (drugs, compounds)
- Phenotypes
- Pathways and reactions
- Literature entries
- Mouse models and phenotypes

**Associations:**
- Target-disease associations from multiple data sources (CRISPR, expression, genetics, etc.)
- Target-target interactions
- Molecule-disease indications
- Disease-phenotype associations
- Pathway annotations

**Supporting Entities:**
- Gene Ontology terms
- Database cross-references
- Mechanisms of action
- Adverse reactions
- Drug warnings
- And many more...

The experimental knowledge graph definition includes 40+ node types and 50+ edge types. See `open_targets/definition/experimental_kg/kg.py` for the complete list.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/biocypher/open-targets.git
   cd open-targets
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

   Alternatively, you can run commands directly with uv:
   ```bash
   uv run python <script>
   ```

4. The adapter can now be imported:
   ```python
   from open_targets.adapter.context import AcquisitionContext
   from open_targets.definition.experimental_kg.kg import experimental_kg_definition
   ```

## Data Preparation

Download the required Open Targets datasets (version 24.09) from the [Open Targets FTP server](https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/24.09/output/etl/parquet/). The adapter requires multiple datasets including:

- `targets/` - Target (gene/protein) information
- `diseases/` - Disease information
- `molecule/` - Drug/molecule information
- `evidence/` - Target-disease evidence
- `go/` - Gene Ontology annotations
- `mousePhenotypes/` - Mouse phenotype data
- `interaction/` - Target-target interactions
- `pathway/` - Pathway information
- And other datasets as needed by specific node/edge definitions

The resulting directory should have the following structure:
```
data/ot_files/
├── targets/
│   └── **/
│       └── *.parquet
├── diseases/
│   └── **/
│       └── *.parquet
├── molecule/
│   └── **/
│       └── *.parquet
├── evidence/
│   └── **/
│       └── *.parquet
...
```

Place all downloaded datasets in the `data/ot_files` directory, maintaining the original directory structure from the Open Targets FTP server.

## Usage
### Quick Start
1. Follow the [Installation](#installation) steps

2. Follow the [Data Preparation](#data-preparation) steps and place the downloaded Parquet files in the `data/ot_files` directory

3. Run the script:
    ```bash
    uv run python scripts/open_targets_biocypher_run.py
    ```
    The script runs BioCypher and generates a knowledge graph using all our node/edge definition presets.

### Not So Quick Start

To use a custom subset of node/edge definitions from our presets:

```python
from biocypher import BioCypher
from open_targets.adapter.context import AcquisitionContext
from open_targets.definition.experimental_kg.node import (
    node_target,
    node_disease,
    node_molecule,
)
from open_targets.definition.experimental_kg.edge import (
    edge_target_disease_association_has_object_disease,
    edge_molecule_indicates_disease,
)

# Initialize BioCypher
bc = BioCypher(biocypher_config_path="config/biocypher_config.yaml")

# Define your custom set of definitions
node_definitions = [
    node_target,
    node_disease,
    node_molecule,
]

edge_definitions = [
    edge_target_disease_association_has_object_disease,
    edge_molecule_indicates_disease,
]

# Create acquisition context
context = AcquisitionContext(
    node_definitions=node_definitions,
    edge_definitions=edge_definitions,
    datasets_location="data/ot_files",  # directory containing the downloaded datasets
)

# Stream nodes and edges to BioCypher
for node_definition in node_definitions:
    bc.write_nodes(context.get_acquisition_generator(node_definition))
for edge_definition in edge_definitions:
    bc.write_edges(context.get_acquisition_generator(edge_definition))

# Finalize
bc.write_import_call()
bc.summary()
```

In brief, first construct a context by providing a set of node/edge definitions.
Then, for each definition, you can obtain a generator that streams data from a
dataset to BioCypher. The data querying and transformation logic is defined in
the node/edge definitions.

More details about customization are provided below.

## Open Targets Data Schema

The full schema of Open Targets data is represented as Python classes included
in this adapter. This design provides type checking for dataset and field
references in code to minimize human error. All dataset and field classes can be
found in `open_targets/data/schema.py`.

**Naming Conventions:**
- All dataset classes are prefixed with `Dataset` (e.g., `DatasetTargets`, `DatasetDiseases`)
- All field classes are prefixed with `Field` (e.g., `FieldTargetsId`, `FieldTargetsApprovedSymbol`)
- Field names follow their structural location in their datasets. For example, `FieldTargetsHallmarksAttributes` represents the `attributes` field in the `targets` dataset, under the `hallmarks` field.

**Usage:**
The schema classes are used throughout node/edge definitions to reference datasets and fields in a type-safe manner. This enables:
- IDE autocompletion and type checking
- Early detection of schema mismatches
- Clear documentation of data structure
- Refactoring safety when schema changes

The schema is generated from Open Targets metadata using code generation (see [Code Generation](#code-generation)).

## Custom Node/Edge Definitions

A node/edge definition describes how nodes/edges are acquired from a dataset.
Each node/edge has essential attributes that make it a valid graph component,
and a definition specifies how these values are acquired or computed. Each
attribute has an expression that describes the chain of actions to acquire the
value from the dataset. An expression can be as simple as a field access or a
complex chain of transformations. Here's a simple example:

```python
definition = ExpressionNodeAcquisitionDefinition(
    scan_operation=RowScanOperation(dataset=DatasetTargets),
    primary_id=FieldExpression(FieldTargetsId),
    label=LiteralExpression("ensembl"),
    properties=[
        (LiteralExpression(FieldTargetsApprovedSymbol.name), FieldExpression(FieldTargetsApprovedSymbol))
    ],
)
```

In plain language, this definition scans through the `targets` dataset and
generates a node for each row. The node's ID is assigned from the `id` field,
its label is set to the literal value `ensembl`, and its properties include a
single property where the key is the name of the referenced field
`approvedSymbol` and the value comes from that field.

Expressions can be chained together:

```python
expression = NormaliseCurieExpression(ToStringExpression(FieldExpression(FieldEvidenceDiseaseId)))
```

This is equivalent to:

```python
value = normalise_curie(str(data[FieldEvidenceDiseaseId]))
```

In fact, this is almost exactly how a function will be built and run during
acquisition.

An edge definition is similar but includes two additional attributes, `source`
and `target`, to link two nodes together.

For minor customization, you can derive from one of our presets as follows:

```python
from dataclasses import replace
from open_targets.data.schema import FieldTargetsApprovedSymbol
from open_targets.definition.experimental_kg.node import node_target

node_definition = replace(node_target, primary_id=FieldTargetsApprovedSymbol)
```

## Code Generation

This repository uses code generation (powered by
[Jinja](https://jinja.palletsprojects.com/en/stable/)) to generate the Open Targets data schema represented in Python classes. 

**Structure:**
- Code generation scripts: `code_generation/`
- Jinja templates: `open_targets/*.jinja` (e.g., `base.jinja`, `config.py.jinja`)
- Generated code: `open_targets/data/schema.py` and related files

**Workflow:**
1. Templates (`.jinja` files) define the structure of the generated code
2. Run `python code_generation/generate.py` to regenerate schema classes
3. Generated files are created from templates using Open Targets metadata

**Important:** Never edit generated files directly. Always modify the templates and regenerate.

## Future Plans

- Implement cloud streaming to eliminate the need for local dataset storage
- Develop a codeless mode for defining node/edge definitions in JSON/YAML files
- Support Open Targets metadata migration to Croissant ML
- Extend beyond Open Targets data to support various tabular data formats
- Create additional scientifically meaningful node/edge definitions and knowledge graph schemas
- Support for newer Open Targets data versions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or create
an Issue if you discover any problems.

## License

This project is licensed under the MIT License - see the LICENSE file for
details.
