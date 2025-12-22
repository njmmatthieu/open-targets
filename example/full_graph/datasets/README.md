# Data Preparation

The reference knowledge graph is comprehensive and uses datasets across the Open Targets platform. Download all available datasets (version 24.09) from the [Open Targets FTP server](https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/24.09/output/etl/parquet/).

Place all downloaded datasets in this `datasets` directory, maintaining the original directory structure from the FTP server:

```
datasets/
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

Since this is a comprehensive knowledge graph, it's recommended to download all available datasets to ensure all node and edge definitions can be processed successfully.

