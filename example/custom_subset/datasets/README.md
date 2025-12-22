# Data Preparation

Download the required Open Targets datasets (version 24.09) from the [Open Targets FTP server](https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/24.09/output/etl/parquet/).

Place the downloaded datasets in this `datasets` directory, maintaining the original directory structure from the FTP server.

## Required Datasets for This Example

This custom subset example requires:
- `targets/` - Target (gene/protein) information
- `diseases/` - Disease information
- `molecule/` - Drug/molecule information
- `evidence/` - Target-disease evidence (for target-disease associations)

See `custom_subset.py` to see which definitions are used and adjust the required datasets accordingly.

