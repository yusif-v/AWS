#AWS #Service #Analytics
### Lake Formation

AWS Lake Formation simplifies building and securing a data lake. It ingests and catalogs data in S3, centralizes permissions for analytics services, and automates ETL with Glue, giving analysts governed access to the data lake.

### How It Works

- Lake Formation ingests data from sources into S3 and registers the location as a governed data lake.
- Uses the Glue Data Catalog to define databases and tables over the lake.
- Centralizes permissions so access granted in Lake Formation is enforced across Athena, Redshift Spectrum, EMR, and QuickSight.
- Blueprints automate data ingestion and ETL jobs to land and curate data.
- Column- and row-level security policies restrict access at fine granularity.

### Key Features

- Governed data lake: Central place to set up and secure the lake.
- Fine-grained access control: Table, column, and row-level permissions.
- Cross-service enforcement: Permissions apply across analytics engines.
- Blueprints: Templates automate data ingestion from S3 and databases.
- Transactional tables: Supports ACID operations with governance.
- Data location management: Registers and tracks S3 locations as queryable tables.

### Common Use Cases

- Building a governed data lake with centralized access control.
- Sharing curated datasets across analytics teams and services.
- Enforcing compliance and row/column-level privacy restrictions.
- Automating ingestion from databases and S3 sources.
- Securing BI and machine learning access to lake data.

### Pricing & Limits

- Billed per amount of data processed by ingestion workflows.
- Storage charges apply for the S3 backing the lake.
- Catalog storage and requests billed like the Glue Data Catalog.
- No charge for the permission management layer itself beyond data processing.

### Related Services

- [[S3]]: The storage backing the data lake.
- [[Glue]]: ETL and catalog for the lake.
- [[Athena]]: Queries data in the lake.
- [[Redshift]]: Queries governed lake data via Redshift Spectrum.
- [[QuickSight]]: Visualizes governed lake data.
- [[EMR]]: Processes lake data with open-source frameworks.
- [[IAM]]: Grants Lake Formation administrative permissions.

### Related Concepts

- Data Lake: Centralized raw + curated data.
- Lake Permissions: Column/row-level access control.
- Catalog: Metadata for queryable tables.
- Data Governance: Centralized policies for access and compliance.
