#AWS #Service #Database
### Aurora

Amazon Aurora is a fully managed relational database engine built for MySQL and PostgreSQL compatibility, engineered for high performance and cloud-scale availability. It combines the speed of commercial databases with the simplicity and cost-effectiveness of open-source engines, delivering enterprise-grade durability, automatic scaling, and low-latency access for demanding workloads. It provides up to 15 read replicas, automatic backups, and global databases for cross-region replication.

### How It Works
- Aurora uses a distributed, SSD-backed storage subsystem separate from compute, so storage scales independently up to 128 TiB per cluster.
- The storage layer replicates data six ways across three Availability Zones, providing durability without separate replication logic.
- Compute nodes read from the shared storage volume, allowing up to 15 low-latency read replicas with replication lag typically under a second.
- A single writer endpoint and multiple reader endpoints route application traffic without manual failover logic.
- Aurora continuously backs up to S3 without impacting performance and supports point-in-time restore within the retention window.

### Key Features
- MySQL and PostgreSQL compatibility: a drop-in replacement for applications using those engines.
- High availability: automatic failover to a replica or the Multi-AZ standby, typically within 30 seconds.
- Global Database: a primary region plus up to 15 secondary regions for low-latency global reads and disaster recovery.
- Aurora Serverless v2: scales compute capacity automatically, even down to zero in scaled capacity, for variable workloads.
- Auto Scaling adjusts the number of read replicas to match demand.
- Encryption at rest via [[KMS]] and in transit, with access control through [[IAM]].

### Common Use Cases
- Enterprise SaaS applications that require a highly available, ACID-compliant relational database.
- High-traffic web and mobile backends that need read scaling beyond a single instance.
- Global applications that serve users from multiple regions with low-latency reads and fast failover.
- Migration targets for on-premises MySQL or PostgreSQL workloads seeking managed operations.

### Pricing & Limits
- Billed per instance hour for compute (standard, memory-optimized, or serverless) plus per-GiB-month for storage and per-GiB for backup storage beyond the included amount.
- Storage grows automatically to a maximum of 128 TiB per cluster and is billed only for what is used.
- The free tier includes 750 instance-hours per month of a small instance for the first 12 months.
- Aurora clusters support up to 15 read replicas per region.

### Related Services

- [[RDS]]: Aurora is part of the RDS family, sharing management features.
- [[Lambda]]: Integrates for serverless application logic.
- [[CloudWatch]]: Monitors Aurora performance metrics and logs.
- [[DMS]]: Migrates databases to Aurora.
- [[S3]]: Stores Aurora backups and snapshots.
- [[KMS]]: Encrypts Aurora storage, backups, and snapshots.
- [[IAM]]: Controls access to Aurora clusters and data.

### Related Concepts

- Relational Databases: Structured data with SQL and ACID compliance.
- High Availability: Multi-AZ deployments and read replicas for fault tolerance.
- Global Databases: Low-latency access and disaster recovery across Regions.
- Serverless Aurora: Auto-scales compute and storage for variable workloads.
- Regions & Availability Zones: Aurora replicates data across three AZs for durability.
