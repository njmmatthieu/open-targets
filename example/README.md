# Examples

This directory contains runnable examples demonstrating how to use the Open Targets BioCypher adapter.

## Available Examples

### Full Graph (`full_graph/`)

Builds the complete reference knowledge graph using all predefined node and edge definitions.

**Run:**
```bash
cd example/full_graph
uv run python full_graph.py
```

**Data:** See `full_graph/datasets/README.md` for data preparation instructions.

### Custom Subset (`custom_subset/`)

Demonstrates how to build a knowledge graph with a custom selection of node and edge definitions.

**Run:**
```bash
cd example/custom_subset
uv run python custom_subset.py
```

**Data:** See `custom_subset/datasets/README.md` for data preparation instructions.

## Creating Your Own Example

1. Create a new directory under `example/`
2. Copy `biocypher_config.yaml` and `schema_config.yaml` from an existing example
3. Create your Python script importing definitions from `open_targets.definition.reference_kg`
4. Add a `datasets/` directory with a README explaining required datasets
5. See existing examples for the pattern

