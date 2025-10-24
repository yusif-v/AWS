#AWS #Tool #Migration 
### AWS Schema Conversion Tool (SCT)

Desktop application for automating database schema conversion during migrations to AWS. Converts schemas and application code between different database engines (e.g., Oracle to Aurora PostgreSQL). Supports homogeneous and heterogeneous migrations, generates conversion reports, and integrates with AWS DMS for data transfer.

### Related Services

- [[AWS Database Migration Service (DMS)]]: Uses SCT for schema conversion in migrations.
- [[Amazon RDS]]: Target for converted relational database schemas.
- [[Amazon Aurora]]: Common destination for heterogeneous migrations.
- [[AWS Migration Hub]]: Tracks migrations involving SCT.
- [[Amazon S3]]: Stores SCT reports and converted scripts.

### Related Concepts

- Heterogeneous Migration: Converts schemas between different database engines.
- Homogeneous Migration: Transfers schemas within the same engine type.
- Schema Conversion: Automates transformation of tables, views, and stored procedures.
- Application Code Conversion: Adjusts SQL code in applications for target databases.