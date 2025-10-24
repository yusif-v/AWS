#AWS #Service #Database #Migration
### AWS Database Migration Service (DMS)

Fully managed service for migrating databases to AWS with minimal downtime. Supports homogeneous (same engine) and heterogeneous (different engines) migrations, including schema conversion. Uses change data capture (CDC) for continuous replication, ensuring zero data loss. Ideal for one-time migrations or ongoing sync, with serverless options for automatic scaling and hourly pricing.

### Related Services

- AWS Schema Conversion Tool (SCT): Converts schemas for heterogeneous migrations.
- [[AWS Migration Hub]]: Tracks DMS migration progress centrally.
- [[Amazon RDS]]: Common target for migrated relational databases.
- [[Amazon Aurora]]: Modernized target for high-performance migrations.
- AWS Database Migration Service Fleet Advisor: Discovers and inventories source databases.

### Related Concepts

- Change Data Capture (CDC): Captures database changes for real-time replication.
- Homogeneous vs. Heterogeneous Migration: Same-engine (direct) vs. different-engine (with schema conversion).
- Minimal Downtime Migration: Keeps source operational during transfer.
- Data Validation: Ensures target data matches source post-migration.