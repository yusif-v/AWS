#AWS #Service #Storage
### S3 Replication

S3 Replication automatically and asynchronously copies objects between buckets. Same-Region Replication (SRR) copies within one region; Cross-Region Replication (CRR) copies to another region. It provides redundancy, compliance, lower-latency access, and protection against regional failures.

### How It Works

- Configure a replication rule on a source bucket, specifying the destination bucket and scope (prefix or tags).
- Objects that match the rule are copied to the destination bucket automatically.
- Versioning must be enabled on both source and destination buckets.
- S3 uses a replication IAM role and a destination bucket policy to establish permissions.
- Once enabled, new objects are replicated; existing objects are replicated only if a backlog status or S3 Batch Replication is used.
- Replicated objects are marked with the `s3:replication` status.

### Key Features

- CRR for disaster recovery and low-latency access to data in other regions.
- SRR for compliance, log aggregation, and production/test duplication in the same region.
- Replication of metadata, ACLs, tags, and object locks.
- Replica modification sync and delete marker replication options.
- S3 Replication Time Control (RTC) provides a 15-minute recovery point objective.
- Supports SSE-S3, SSE-KMS, and SSE-C encrypted objects.

### Common Use Cases

- Cross-region disaster recovery with low RPO.
- Reducing latency by replicating data closer to distributed users.
- Compliance: replicating data to a specific region for regulatory retention.
- Aggregating logs from many buckets into a central account.
- Maintaining production and test copies of datasets.

### Pricing & Limits

- CRR incurs data transfer charges; SRR has no cross-region data transfer charge.
- Replication requests are billed per 1,000 objects replicated.
- Both buckets must have versioning enabled.
- Replication is asynchronous; RTC reduces the RPO to 15 minutes for an additional cost.

### Related Services

- [[S3]]: The bucket service where replication is configured.
- [[S3 Versioning]]: A prerequisite for replication.
- [[S3 Lifecycle]]: Applies to replicated copies independently.
- [[S3 Access Control]]: Destination bucket policies allow the replication role.
- [[S3 Encryption]]: Replication of encrypted objects.

### Related Concepts

- Cross-Region Replication (CRR): Copying to another region.
- Same-Region Replication (SRR): Copying within one region.
- Replication Time Control (RTC): 15-minute RPO guarantee.
- RPO/RTO: Recovery point and recovery time objectives for disaster recovery.
- Backlog Status: Tracks whether existing objects have been replicated.
