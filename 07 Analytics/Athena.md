#AWS #Service #Analytics
### Athena

Serverless, interactive query service for analyzing data in Amazon S3 using standard SQL. Requires no infrastructure management and charges per data scanned. Ideal for ad-hoc queries, data lake analytics, and exploring structured or semi-structured data.

### How It Works

- Queries execute directly against data stored in S3 without loading or copying it into a database.
- Uses the Glue Data Catalog (or an external Hive metastore) to resolve table schemas and partitions.
- A serverless query engine distributes work across managed compute and reads only the files it needs.
- Supports CSV, JSON, Parquet, ORC, Avro, and log formats, including compressed data.
- Query results can be written back to S3 or consumed by downstream services such as QuickSight.

### Key Features

- Standard SQL: Runs ANSI-standard SQL with familiar tooling and BI connectors.
- Serverless: No clusters or servers to provision, manage, or tune.
- Pay-per-query: Billed only for data scanned; partitioning and columnar formats reduce cost.
- Partition projection: Speeds up queries on heavily partitioned tables by computing partitions at query time.
- Federated queries: Extends SQL to sources such as DynamoDB, JDBC databases, and CloudWatch Logs without ETL.
- Workgroups: Manage query concurrency, cost controls, and per-team usage.

### Common Use Cases

- Ad-hoc analytics and exploratory queries over data lake content.
- Log analysis on CloudTrail logs, VPC Flow Logs, and application logs stored in S3.
- Feeding QuickSight dashboards from S3 data without loading it into a warehouse.
- Building recurring reporting and audit queries over operational data.
- Running one-off data transformations and export queries.

### Pricing & Limits

- Billed per amount of data scanned per query (widely known ~$5 per TB); free tier includes a monthly scanned-data allowance.
- Costs drop with columnar formats (Parquet/ORC), compression, partitioning, and simple S3 Select alternatives.
- Query concurrency and workgroup limits are managed through service quotas.

### Related Services

- [[S3]]: Stores data queried by Athena.
- [[Glue]]: Creates data catalog for schema and metadata management.
- [[QuickSight]]: Visualizes Athena query results in dashboards.
- [[CloudWatch]]: Monitors Athena query performance and logs.
- [[IAM]]: Controls access to Athena queries and data.
- [[Lake Formation]]: Governs access to tables queried by Athena.
- [[Redshift Spectrum]]: Alternative for querying S3 data from Redshift.
- [[S3 Select]]: Lower-cost option for simple object-level SQL filtering.

### Related Concepts

- Serverless Querying: Eliminates need for managing database servers.
- Data Lake: Centralized S3 storage for structured and unstructured data.
- SQL-Based Analytics: Uses ANSI SQL for querying diverse data formats.
- Pay-Per-Query: Charges based on data scanned, optimizing cost for queries.
- Columnar Storage: Formats like Parquet reduce bytes scanned and query cost.
- Federated Querying: Queries across multiple data sources in a single statement.
