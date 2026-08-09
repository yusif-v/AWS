#AWS #Service #Database
### RDS Read Replicas

RDS Read Replicas are asynchronous copies of a database used to offload read traffic and improve performance. They can be promoted to standalone instances, support cross-region replication, and help scale read-heavy workloads.

### Related Services

- [[RDS]]: The primary database being replicated.
- [[RDS Multi-AZ]]: Availability-focused replication (distinct from replicas).
- [[Route 53]]: Routes reads to replica endpoints.

### Related Concepts

- Asynchronous Replication: Replicas may lag slightly.
- Read Scaling: Distribute SELECT traffic.
- Promotion: Convert a replica to a primary.
