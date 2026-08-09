#AWS #Service #Storage
### EBS

Amazon Elastic Block Store (EBS) provides persistent, network-attached block storage for EC2 instances. Volumes are replicated within an Availability Zone, support snapshots to S3 for backup, and offer several volume types (gp2/gp3, io1/io2, st1, sc1) for cost and performance.

### How It Works

- EBS volumes attach to a single EC2 instance at a time (within the same AZ) and behave like raw block devices (e.g., `/dev/sdb`).
- Data is replicated redundantly across multiple servers within the same Availability Zone for durability.
- Volume size and performance can be increased dynamically for most volume types without downtime.
- Snapshots are stored incrementally in S3 and can create new volumes, migrate across AZs/regions, or back up data.
- Volumes should be unmounted or snapshotted consistently for crash-consistent or app-consistent backups.

### Key Features

- Multiple volume types: gp3/gp2 (general-purpose SSD), io1/io2 (provisioned IOPS SSD), st1 (throughput-optimized HDD), sc1 (cold HDD).
- io2 Block Express offers higher IOPS and capacity with sub-millisecond latency for demanding workloads.
- Snapshots provide incremental, point-in-time backups that can be shared or copied across regions.
- EBS encryption at rest with AWS KMS keys, including default encryption for new volumes.
- Multi-Attach for io1/io2 volumes enables shared block access across multiple Nitro-based instances.
- Data lifecycle manager automates snapshot creation and deletion.

### Common Use Cases

- Root and data volumes for EC2 instances running operating systems and applications.
- Database storage requiring high, predictable IOPS (e.g., [[RDS]] volumes and self-managed databases).
- Boot volumes launched from [[EC2 AMIs]].
- Backup and disaster recovery via snapshots copied to other regions.
- High-performance workloads like NoSQL databases and data processing.

### Pricing & Limits

- Billed per GB-month of provisioned storage plus I/O (gp3) or provisioned IOPS (io1/io2).
- Snapshots are billed per GB of stored data in S3 (incremental blocks).
- EBS volumes have region-specific size limits (up to 16 TiB for most types).
- Deleting a volume does not delete its snapshots unless you delete them explicitly.

### Related Services

- [[EC2]]: Attaches EBS volumes to instances.
- [[EC2 Storage]]: How EBS fits into EC2 storage options.
- [[S3]]: Stores EBS snapshots.

### Related Concepts

- Snapshots: Incremental backups to S3.
- IOPS: Input/output operations per second.
- [[EC2 AMIs]]: Root volumes originate from images.
- Block Storage: Fixed-size blocks accessed as raw devices, distinct from file or object storage.
- Availability Zone: Volumes are bound to a single AZ for low-latency access.
