#AWS #Service #Database
### RDS Multi-AZ

RDS Multi-AZ provides high availability by automatically replicating a primary database to a standby in another Availability Zone. Failover is automatic, synchronous replication keeps data in sync, and the standby is not used for reads.

### How It Works
- The primary instance synchronously replicates data to a standby instance in a different Availability Zone.
- If the primary fails (hardware, storage, or AZ-level), RDS automatically promotes the standby within a short failover window.
- The application endpoint (DNS name) is updated automatically, so most applications reconnect without code changes.
- The standby is a separate instance that does not serve reads; Multi-AZ is about availability, not performance.
- Multi-AZ is a deployment option available for most RDS engines and can be enabled on existing instances with minimal downtime.

### Key Features
- Automatic failover with minimal downtime, typically around 60 seconds.
- Synchronous replication ensures no data loss on failover.
- Failure detection covers DB instance, storage, and Availability Zone issues.
- Can be enabled on existing instances with zero downtime.
- Multi-AZ cluster deployments support two readable standby instances in some engines.

### Common Use Cases
- Production relational databases that must survive an Availability Zone failure.
- Workloads with strict availability requirements, such as e-commerce and financial systems.
- Databases where patching or maintenance must avoid downtime.
- Applications requiring automatic failover without manual intervention.

### Pricing & Limits
- Billed for the primary instance plus an additional standby instance, roughly doubling compute and storage cost for the DB.
- Available for MySQL, PostgreSQL, Oracle, SQL Server, MariaDB, and Aurora.
- Failover time depends on instance class and workload; provisioned IOPS improves failover speed.

### Related Services

- [[RDS]]: The managed database service.
- [[RDS Read Replicas]]: Asynchronous read scaling (separate feature).
- [[VPC]]: Network placement across AZs.
- [[CloudWatch]]: Monitors failover events and instance health.

### Related Concepts

- Failover: Automatic switch to standby on failure.
- Synchronous Replication: Standby stays current.
- High Availability: Survives AZ failure.
- Regions & Availability Zones: The standby is placed in a different AZ from the primary.
