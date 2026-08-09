#AWS #Service #Migration
### SCT

Desktop application for automating database schema conversion during migrations to AWS. Converts schemas and application code between different database engines (e.g., Oracle to Aurora PostgreSQL). Supports homogeneous and heterogeneous migrations, generates conversion reports, and integrates with AWS DMS for data transfer.

### Related Services

- [[DMS]]: Uses SCT for schema conversion in migrations.
- [[RDS]]: Target for converted relational database schemas.
- [[Aurora]]: Common destination for heterogeneous migrations.
- [[Migration Hub]]: Tracks migrations involving SCT.
- [[S3]]: Stores SCT reports and converted scripts.

### Related Concepts

- Heterogeneous Migration: Converts schemas between different database engines.
- Homogeneous Migration: Transfers schemas within the same engine type.
- Schema Conversion: Automates transformation of tables, views, and stored procedures.
- Application Code Conversion: Adjusts SQL code in applications for target databases.