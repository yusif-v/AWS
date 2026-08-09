#AWS #Service #Storage
### S3 Select

S3 Select enables you to run SQL-like queries directly against objects stored in S3 using simple expressions. Only the relevant subset of the data is returned, reducing data transferred to your application and improving performance for analytics over large objects.

### How It Works

- Issue an S3 Select API request (e.g., via SDK or CLI) specifying a SQL expression and an object.
- S3 filters records server-side, returning only the matching rows and columns.
- Supported formats include CSV, JSON, and Parquet; gzip and bzip2 compressed input is supported.
- Output is delivered as a serialized stream (CSV or JSON).
- Well suited for large objects where transferring the entire file is wasteful.

### Key Features

- Server-side filtering reduces network transfer and client-side processing.
- SQL-like expressions (SELECT, WHERE, LIMIT, aggregate functions) on structured objects.
- Reduces per-GB data transfer costs and improves latency for analytics.
- No additional infrastructure required; runs directly against S3.
- Integrated with the SDKs and CLI for simple automation.

### Common Use Cases

- Filtering large CSV/JSON logs before processing in an application.
- Extracting specific columns from big data files for quick checks.
- Pre-filtering data before loading into analytics tools.
- Lightweight data retrieval without standing up an analytics service.
- Reducing egress cost when pulling subsets from massive objects.

### Pricing & Limits

- Billed per GB scanned by S3 Select plus per GB of data returned to the client.
- Works well for structured data; less effective for binary or unstructured data.
- A lightweight alternative to a full analytics service for smaller queries.

### Related Services

- [[S3]]: Hosts the objects being queried.
- [[Athena]]: Full SQL query service over S3 at scale (pairs naturally with Select).
- [[Glue]]: ETL and cataloging over S3 data.
- [[Redshift Spectrum]]: Querying S3 data at scale from Redshift.
- [[Lake Formation]]: Data lake governance over S3.

### Related Concepts

- Object Storage: S3 stores unstructured objects, queried in place.
- SQL-like Filtering: Server-side record-level filtering.
- Data Transfer Optimization: Reducing bytes moved by filtering server-side.
- Columnar Formats: Parquet allows efficient column-level access.
