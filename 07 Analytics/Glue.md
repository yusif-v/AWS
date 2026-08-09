#AWS #Service #Analytics
### Glue

Fully managed, serverless ETL (Extract, Transform, Load) service for discovering, preparing, and integrating data for analytics, ML, and application development. Includes data catalog for metadata management, crawlers for schema discovery, and jobs for code generation/execution.

### How It Works

- The Glue Data Catalog is a central metadata repository of tables, schemas, and partitions used by Athena, Redshift Spectrum, EMR, and other services.
- Crawlers scan data sources, infer schemas, and register tables in the catalog.
- ETL jobs run on a serverless Apache Spark or Python runtime with automatic capacity allocation.
- Glue Studio provides a visual interface for authoring, and jobs can be triggered by EventBridge, S3 events, or schedules.
- Flexible storage adapters handle S3, JDBC databases, and many file formats.

### Key Features

- Data Catalog: Centralized schema and metadata store shared across analytics services.
- Crawlers: Automatically discover, classify, and register tables and partitions.
- Serverless ETL: Spark-based jobs scale without infrastructure management.
- Glue Studio: Visual job authoring, debugging, and monitoring.
- DataBrew: Visual data preparation for cleaning and normalizing data.
- Glue Workflows: Orchestrate crawlers, jobs, and triggers into pipelines.

### Common Use Cases

- Building and maintaining a governed data lake in S3.
- ETL pipelines that land raw data and produce curated, queryable tables.
- Moving data between databases and warehouses, such as into Redshift or S3.
- Schema discovery and cataloging for Athena and Redshift Spectrum queries.
- Preparing data for machine learning on SageMaker.

### Pricing & Limits

- Billed per second for Data Processing Units (DPUs) consumed by crawlers and jobs.
- Data Catalog storage and API requests billed at low per-item rates.
- No upfront cost or minimum commitment for serverless jobs.
- Job concurrency and DPU capacity are controlled by service quotas.

### Related Services

- [[S3]]: Stores raw data crawled by Glue and transformed outputs.
- [[Athena]]: Queries data using Glue's data catalog.
- [[Redshift]]: Loads ETL-processed data from Glue.
- [[Lambda]]: Integrates for custom ETL functions or triggers.
- [[EMR]]: Complements Glue for big data processing workflows.
- [[EventBridge]]: Triggers Glue jobs on schedule or events.
- [[Lake Formation]]: Uses the catalog to govern data lake access.
- [[SageMaker]]: Consumes prepared data for machine learning.

### Related Concepts

- ETL Processes: Automates data extraction, transformation, and loading.
- Data Catalog: Centralized metadata repository for data assets.
- Crawlers: Automatically infer schemas and populate catalogs.
- Serverless Architecture: Scales automatically without managing infrastructure.
- Data Lake: Foundation for centralized analytics storage.
