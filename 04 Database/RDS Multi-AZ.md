#AWS #Service #Database
### RDS Multi-AZ

RDS Multi-AZ provides high availability by automatically replicating a primary database to a standby in another Availability Zone. Failover is automatic, synchronous replication keeps data in sync, and the standby is not used for reads.

### Related Services

- [[RDS]]: The managed database service.
- [[RDS Read Replicas]]: Asynchronous read scaling (separate feature).
- [[VPC]]: Network placement across AZs.

### Related Concepts

- Failover: Automatic switch to standby on failure.
- Synchronous Replication: Standby stays current.
- High Availability: Survives AZ failure.
