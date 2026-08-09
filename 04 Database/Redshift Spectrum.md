#AWS #Service #Database
### Redshift Spectrum

Redshift Spectrum lets you run SQL queries directly against data in S3 without loading it into Redshift. It uses the Redshift cluster to coordinate queries while massively parallel nodes scan S3, enabling petabyte-scale analytics over a data lake.

### How It Works
- Spectrum reads files (Parquet, ORC, JSON, CSV, and others) directly from S3 as an external query engine.
- The Redshift cluster acts as the query coordinator and the connection point for applications.
- Spectrum nodes execute queries in parallel against S3 and return results through the cluster.
- External tables in Redshift reference S3 locations and are registered in the Glue Data Catalog.
- Data is not copied into the cluster, so storage costs stay in S3.

### Key Features
- Query petabyte-scale data directly in S3 without loading or ETL.
- Supports standard SQL and joins between external S3 data and local Redshift tables.
- Automatic parallelism across many Spectrum nodes for fast scans.
- Uses columnar formats (Parquet, ORC) and predicate pushdown to minimize data scanned and cost.
- Integrates with the [[Glue]] Data Catalog for schema management.
- Scales independently of the Redshift cluster's compute.

### Common Use Cases
- Analytics over a data lake of raw or semi-structured data in S3.
- Infrequent queries of large datasets where loading into Redshift is not cost-effective.
- Combining warehouse tables with external S3 data in a single query.
- Ad-hoc exploration of new data before deciding to load it.

### Pricing & Limits
- Billed per terabyte of data scanned by Spectrum queries; the Redshift cluster provides compute.
- Columnar formats and partitioning reduce the amount of data scanned, lowering costs.
- Spectrum queries share the cluster's capacity with regular Redshift workloads.

### Related Services

- [[Redshift]]: The cluster that runs Spectrum queries.
- [[S3]]: The data lake being queried.
- [[Athena]]: Serverless alternative for S3 queries.
- [[Glue]]: Data Catalog and ETL for external tables.

### Related Concepts

- Data Lake: Querying raw data in S3.
- External Tables: Tables backed by S3.
- ELT/ETL: Spectrum avoids loading data.
- Columnar Storage: Formats like Parquet reduce scan cost.
- Petabyte-Scale Analytics: Querying large datasets in place.
