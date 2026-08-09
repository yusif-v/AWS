#AWS #Service #Migration
### SCT

Desktop application for automating database schema conversion during migrations to AWS. Converts schemas and application code between different database engines (e.g., Oracle to Aurora PostgreSQL). Supports homogeneous and heterogeneous migrations, generates conversion reports, and integrates with AWS DMS for data transfer. Free to download and use as the schema-conversion front end to the database migration workflow.

### How It Works

- Connect SCT to the source database and read its schema, objects, and stored code.
- Analyze the schema against a selected AWS target such as [[RDS]], [[Aurora]], [[Redshift]], or [[DynamoDB]].
- Convert tables, views, indexes, stored procedures, and application SQL to the target engine.
- Generate **conversion reports** and migration assessment summaries with action items.
- Export the converted schema and scripts, then use [[DMS]] to move the actual data.

### Key Features

- Broad engine coverage: Oracle, SQL Server, PostgreSQL, MySQL, MariaDB, SAP ASE, and more to AWS.
- Converts not only schemas but also embedded application SQL and stored code.
- Creates detailed conversion reports and an assessment report for migration planning.
- Supports both homogeneous and heterogeneous migrations.
- Free tool, run locally as a desktop application.
- Can convert data warehouse workloads to [[Redshift]] and NoSQL to [[DynamoDB]].

### Common Use Cases

- Moving Oracle to [[Aurora]] PostgreSQL as part of a database modernization.
- Migrating SQL Server to [[RDS]] with less manual rewriting.
- Preparing an assessment of conversion effort before committing to a migration.
- Feeding converted schemas into [[DMS]] for the data-transfer phase.

### Pricing & Limits

- No license cost; SCT is free to download and run.
- You pay only for the AWS target resources and DMS usage during migration.
- Runs as a desktop tool, so the memory/CPU of the local machine bound the conversion jobs.

### Related Services

- [[DMS]]: Uses SCT for schema conversion in migrations.
- [[RDS]]: Target for converted relational database schemas.
- [[Aurora]]: Common destination for heterogeneous migrations.
- [[Migration Hub]]: Tracks migrations involving SCT.
- [[S3]]: Stores SCT reports and converted scripts.
- [[Redshift]]: Target for data-warehouse conversions.

### Related Concepts

- Heterogeneous Migration: Converts schemas between different database engines.
- Homogeneous Migration: Transfers schemas within the same engine type.
- Schema Conversion: Automates transformation of tables, views, and stored procedures.
- Application Code Conversion: Adjusts SQL code in applications for target databases.
- Database Modernization: Replatforming legacy engines onto managed AWS databases.
