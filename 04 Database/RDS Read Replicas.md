#AWS #Service #Database
### RDS Read Replicas

RDS Read Replicas are asynchronous copies of a database used to offload read traffic and improve performance. They can be promoted to standalone instances, support cross-region replication, and help scale read-heavy workloads.

### How It Works
- The primary instance streams changes to replicas asynchronously using engine-native replication.
- Replicas can be created in the same region or in different regions (cross-region replicas) for disaster recovery and geographic read locality.
- Reads are distributed across replicas, offloading read I/O from the primary.
- Replication is asynchronous, so replicas may lag slightly behind the primary at any moment.
- A replica can be promoted to a standalone primary, typically within minutes, though promotion can lose in-flight changes.

### Key Features
- Read scaling: add replicas to handle read-heavy traffic.
- Cross-region replicas support disaster recovery and low-latency global reads.
- A replica can be promoted to a primary for failover or maintenance scenarios.
- Supported for MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server; Aurora uses a similar mechanism.
- Multi-AZ replicas protect individual replicas against Availability Zone failure.

### Common Use Cases
- Scaling read-heavy web applications such as reporting, dashboards, and analytics queries.
- Geographic read locality for users in different regions.
- Database migration or engine upgrade paths via promotion.
- Offloading analytics or ETL jobs from the primary.

### Pricing & Limits
- Replicas are billed as separate DB instances at standard RDS rates.
- MySQL, PostgreSQL, and MariaDB support up to 15 read replicas; Oracle and SQL Server support fewer.
- Cross-region replicas incur data transfer charges.

### Related Services

- [[RDS]]: The primary database being replicated.
- [[RDS Multi-AZ]]: Availability-focused replication (distinct from replicas).
- [[Route 53]]: Routes reads to replica endpoints.
- [[CloudWatch]]: Monitors replica lag.

### Related Concepts

- Asynchronous Replication: Replicas may lag slightly.
- Read Scaling: Distribute SELECT traffic.
- Promotion: Convert a replica to a primary.
- Disaster Recovery: Cross-region replicas protect against region loss.
