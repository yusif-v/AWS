#AWS #Service #Migration
### DMS

Fully managed service for migrating databases to AWS with minimal downtime. Supports homogeneous (same engine) and heterogeneous (different engines) migrations, including schema conversion. Uses change data capture (CDC) for continuous replication, ensuring zero data loss. Ideal for one-time migrations or ongoing sync, with serverless options for automatic scaling and hourly pricing. Runs as a replication instance in the target AWS region while source and target remain live.

### How It Works

- Provision a **replication instance** (managed compute) that hosts one or more replication tasks.
- Define source and target endpoints pointing at the databases involved, storing credentials in [[Secrets Manager]].
- DMS performs a full load of existing data, then captures ongoing changes via **Change Data Capture (CDC)**.
- Replicates deltas continuously so the target stays in sync until cutover, then you switch applications.
- Integrates with Fleet Advisor for source discovery and [[SCT]] for heterogeneous migrations that need schema conversion first.

### Key Features

- Minimal-downtime full-load plus ongoing-replication migrations.
- Heterogeneous support between major engines (Oracle, SQL Server, PostgreSQL, MySQL, MariaDB) and AWS targets like [[RDS]] and [[Aurora]].
- Change Data Capture for near-real-time synchronization and zero data loss on cutover.
- Serverless replication instances that scale automatically and bill by hour.
- Built-in data validation to confirm target data matches source.
- Supports many-to-one consolidation of multiple sources into one target.

### Common Use Cases

- Moving on-premises databases to [[RDS]] or [[Aurora]] with limited downtime.
- Replatforming legacy Oracle or SQL Server workloads to open-source engines.
- Continuous synchronization for hybrid deployments during a phased cutover.
- Database consolidation across multiple source servers into a single instance.

### Pricing & Limits

- Billed per hour for replication instances, with sizes from small to xlarge (including Multi-AZ).
- Serverless DMS bills by capacity units consumed, on-demand, with no idle charge.
- Data transfer into AWS is free; egress beyond the free tier is billed at standard rates.
- Replication tasks are limited by instance size, storage, and source/target engine capabilities.

### Related Services

- AWS Schema Conversion Tool (SCT): Converts schemas for heterogeneous migrations.
- [[Migration Hub]]: Tracks DMS migration progress centrally.
- [[RDS]]: Common target for migrated relational databases.
- [[Aurora]]: Modernized target for high-performance migrations.
- AWS Database Migration Service Fleet Advisor: Discovers and inventories source databases.
- [[SCT]]: Automates schema and code conversion ahead of DMS data transfer.
- [[Secrets Manager]]: Stores source and target database credentials for endpoints.

### Related Concepts

- Change Data Capture (CDC): Captures database changes for real-time replication.
- Homogeneous vs. Heterogeneous Migration: Same-engine (direct) vs. different-engine (with schema conversion).
- Minimal Downtime Migration: Keeps source operational during transfer.
- Data Validation: Ensures target data matches source post-migration.
- Replication Instance: The managed compute engine that runs DMS tasks.
