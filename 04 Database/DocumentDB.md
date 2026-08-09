#AWS #Service #Database
### DocumentDB

Amazon DocumentDB is a fully managed document database that is compatible with MongoDB. It stores JSON-like documents with a flexible, schema-less structure, and delivers the performance, scalability, and availability of a commercial database without the operational burden of running it yourself. It supports up to 15 read replicas and offers automatic scaling, encryption, and point-in-time backups.

### How It Works
- Data is stored as JSON-like documents within collections, using a flexible schema that adapts as applications evolve.
- The storage layer replicates data six ways across three Availability Zones for durability.
- Compute and storage scale independently; storage grows automatically up to 64 TiB.
- Up to 15 low-latency read replicas read from the same distributed storage volume.

### Key Features
- MongoDB compatibility: existing MongoDB applications and drivers migrate with minimal changes.
- Automatic scaling of storage and compute resources.
- Encryption at rest and in transit, with integration with [[KMS]] and [[IAM]].
- Point-in-time recovery and automatic backups with retention up to 35 days.
- Global clusters for low-latency reads across multiple regions.
- ACID transactions for workloads that need multi-document consistency.

### Common Use Cases
- Content management and user-profile stores that rely on flexible document schemas.
- Mobile and web application backends with high-throughput reads and writes.
- Applications already built on MongoDB that want a managed AWS-native alternative.
- Catalog and personalization services that evolve their data model frequently.

### Pricing & Limits
- Billed per instance hour for compute, per-GiB-month for storage, and for backup storage beyond the included amount.
- Storage automatically scales up to 64 TiB per cluster.
- A free tier is available for the first 12 months with 750 instance-hours per month.
- Up to 15 read replicas per cluster.

### Related Services

- [[DynamoDB]]: Other NoSQL option for key-value/document data.
- [[Neptune]]: Graph database for connected data.
- [[RDS]]: Relational alternative.
- [[DMS]]: Migrates MongoDB workloads to DocumentDB.

### Related Concepts

- Document Model: JSON-like flexible schemas.
- MongoDB Compatibility: Drop-in migration support.
- Read Replicas: Scale reads up to 15 copies.
- NoSQL Databases: Schema-less storage for unstructured or semi-structured data.
- Regions & Availability Zones: Replication across three AZs for durability.
