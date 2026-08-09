#AWS #Service #Compute
### EC2 Storage

EC2 instances use two block storage options: EBS volumes (durable, network-attached, detached and reattached) and instance store volumes (ephemeral, physically attached, lost on stop). File-level shared storage can be added via EFS, and object storage via S3.

### How It Works

- EBS volumes are network-attached block devices that persist independently of the instance and can be detached, resized, or snapshotted.
- Instance store volumes are physically attached to the host and provide high I/O but lose data when the instance stops or terminates.
- EFS provides a fully managed NFS file system that many instances can mount simultaneously across Availability Zones.
- S3 offers object storage for durable, versioned, and lifecycle-managed data outside the instance file system.
- A block-device mapping in the AMI defines the root volume and any additional volumes created at launch.

### Key Features

- EBS volume types: General Purpose (gp3/gp2), Provisioned IOPS (io2/io1), Throughput Optimized (st1), and Cold HDD (sc1).
- EBS snapshots are incremental, stored in S3, and support encryption via KMS.
- EBS Multi-Attach, fast snapshot restore, and data lifecycle management for automation.
- Instance store is free and included in the instance price, ideal for caches, scratch data, and temporary processing.
- EFS scales elastically as files are added and is used with Linux/Unix instances.

### Common Use Cases

- Persistent boot volumes and application data on EBS.
- High-throughput scratch space and ephemeral caches on instance store.
- Shared file storage for web farms and content management on EFS.
- Durable object data, backups, and archives on S3.

### Pricing & Limits

- EBS is billed per GB-month plus IOPS and throughput for provisioned types; snapshots billed for S3 storage.
- Instance store is included in the instance price with no separate charge.
- EFS is billed per GB-month for the storage you use; S3 charges per GB-month with tiered pricing.

### Related Services

- [[EBS]]: Persistent block storage for instances.
- [[EFS]]: Shared file storage for Linux instances.
- [[S3]]: Object storage for data exchange and backup.
- [[EC2 AMIs]]: Images store root volumes.
- [[Backup]]: Centralized backup of EBS volumes.

### Related Concepts

- Durability: EBS persists independently of the instance.
- Ephemeral Storage: Instance store data is temporary.
- [[EC2 Instance Types]]: Storage optimized families for high I/O workloads.
- [[S3 Lifecycle]]: Managing data transition and expiry over time.
