#AWS #Service #Database
### RDS

Amazon Relational Database Service (RDS) is a fully managed relational database service supporting MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora. It automates backups, patching, scaling, and failover, and offers Multi-AZ deployments for high availability, read replicas for scalability, and point-in-time recovery for data restoration.

### How It Works
- RDS provisions a managed DB instance running your chosen engine on infrastructure AWS manages for you.
- AWS handles the underlying host: patching, OS maintenance, storage, and replication configuration.
- You access the database through a standard connection endpoint while RDS manages supporting components.
- Compute, storage, and network are configured through the console, CLI, or infrastructure as code.
- RDS monitors instance health and can automatically fail over with [[RDS Multi-AZ]].

### Key Features
- Multiple engine options: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora.
- Automated backups with point-in-time recovery and manual snapshots.
- [[RDS Multi-AZ]] for high availability and [[RDS Read Replicas]] for read scaling.
- Automatic minor version patching and storage scaling.
- Encryption at rest and in transit via [[KMS]], with access control through [[IAM]].
- Managed maintenance windows and automated monitoring with [[CloudWatch]].

### Common Use Cases
- Standard web and mobile application backends that need a reliable relational database.
- Lift-and-shift migrations of existing MySQL, PostgreSQL, Oracle, or SQL Server databases.
- Enterprise applications requiring ACID transactions and SQL.
- Workloads that want to offload database administration tasks.

### Pricing & Limits
- Billed per instance hour based on instance class, plus storage per GiB-month and I/O.
- On-demand and reserved instance pricing options are available.
- The free tier includes 750 hours of a small instance per month for 12 months.
- Multi-AZ deployments roughly double compute and storage cost for the standby.

### Related Services

- [[Aurora]]: High-performance engine within RDS family.
- [[DMS]]: Migrates databases to RDS.
- [[CloudWatch]]: Monitors RDS performance metrics and logs.
- [[IAM]]: Controls access to RDS instances.
- [[VPC]]: Secures RDS in isolated network environments.
- [[RDS Backups]]: Automated backups and snapshots.
- [[KMS]]: Encrypts RDS storage and backups.

### Related Concepts

- Relational Databases: Structured data with SQL and ACID compliance.
- Multi-AZ Deployments: Synchronous replication for fault tolerance.
- Read Replicas: Asynchronous copies for scaling read-heavy workloads.
- Shared Responsibility Model: AWS manages infrastructure; customers handle data and configurations.
- Regions & Availability Zones: Instances run in specific AZs.
