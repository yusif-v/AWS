#AWS #Service #Database
### Redshift

Amazon Redshift is a fully managed, petabyte-scale data warehouse service for analyzing large datasets using SQL. It leverages columnar storage and massively parallel processing (MPP) for fast query performance, and integrates data from S3, databases, and streams, with automated backups, scaling, and encryption for analytics and business intelligence.

### How It Works
- Data is stored by column rather than by row, which speeds up analytical queries that aggregate over a few columns.
- A cluster consists of a leader node (query coordination) and multiple compute nodes (parallel execution).
- Queries are split into slices and run across all nodes simultaneously (MPP).
- Data can be loaded from S3 with the COPY command, from databases via [[DMS]], or from streaming sources via [[Kinesis]].
- RA3 nodes separate compute and storage, allowing each to scale independently.

### Key Features
- Columnar storage and zone maps reduce I/O for analytic queries.
- MPP architecture delivers fast query performance at petabyte scale.
- Concurrency scaling adds transient query capacity during demand spikes.
- Automated backups, snapshots, and cross-region snapshot copy for disaster recovery.
- Encryption at rest and in transit with [[KMS]] integration and [[IAM]] access control.
- Redshift Spectrum queries S3 data directly; Redshift Serverless removes cluster management.

### Common Use Cases
- Business intelligence and analytics dashboards with [[QuickSight]].
- Large-scale data warehousing for reporting and decision support.
- Log analytics and ad-hoc analytical queries over large datasets.
- Data lake integration, querying warehouse and S3 data together.

### Pricing & Limits
- Billed per node-hour based on node type and number of nodes; RA3 nodes separate compute and storage costs.
- Dense compute (DC2) and dense storage (RA3) node families are available.
- Storage scales from hundreds of GB to petabytes.
- Redshift Serverless bills by compute capacity consumed.

### Related Services

- [[S3]]: Stores data for Redshift ingestion and backups.
- [[Glue]]: Prepares and loads data into Redshift.
- [[QuickSight]]: Visualizes Redshift data in dashboards.
- [[Kinesis]]: Streams real-time data to Redshift.
- [[DMS]]: Migrates databases to Redshift.
- [[Athena]]: Serverless alternative for querying S3 data.
- [[IAM]]: Controls access to Redshift resources.
- [[KMS]]: Encrypts Redshift data.

### Related Concepts

- Data Warehousing: Centralized storage for structured data analytics.
- Massively Parallel Processing (MPP): Distributes queries across nodes for speed.
- Columnar Storage: Optimizes analytics by storing data by column.
- Data Lake Integration: Combines Redshift with S3 for unified analytics.
- Regions & Availability Zones: Clusters run in a single AZ; cross-region snapshots enable DR.
