#AWS #Service #Storage
### DataSync

Service for automating and accelerating data transfer between on-premises storage, AWS services, or other clouds. Supports high-speed, secure transfers with encryption and scheduling. Ideal for migrations, backups, or hybrid workflows, syncing data to Amazon S3, EFS, or FSx.

### How It Works

- Deploy a DataSync agent in the source environment, either on-premises (VMware, Hyper-V, KVM) or directly in AWS.
- Create a task that connects a source location (NFS, SMB, or self-managed object storage) to a destination location (S3, EFS, or FSx).
- Transfers run over TLS, are accelerated with automatic network optimization, and are verified with per-file checksums.
- Scheduling enables recurring transfers (e.g., nightly) for ongoing replication between environments.
- Task executions produce detailed transfer logs and [[CloudWatch]] metrics for monitoring.

### Key Features

- Transfer speeds roughly 10x faster than simple copy tools, using parallel multi-threaded transfers.
- Built-in bandwidth throttle and scheduling to avoid saturating production links.
- Supports incremental transfers by copying only changed data after the initial full transfer.
- Handles file metadata (timestamps, permissions, ownership) for NFS and SMB sources.
- Validates integrity with end-to-end checksums; failed files are logged for retry.
- Can also transfer directly between AWS storage services (e.g., EFS to S3) without an agent.

### Common Use Cases

- One-time migration of large on-premises datasets to S3, EFS, or FSx.
- Ongoing hybrid replication between on-premises storage and AWS.
- Data transfer between AWS regions or storage services (e.g., EFS to S3 for analytics).
- Cloud migration staging combined with offline options like [[Snowball Edge]] for very large volumes.
- Backup and disaster-recovery replication to cloud storage.

### Pricing & Limits

- Billed per GB transferred based on the amount of data moved per task execution.
- No upfront cost and no minimum commitments; the agent software is free.
- For extremely large datasets, offline transfer (Snowball family) may be more economical than online transfer.

### Related Services

- [[S3]]: Common destination for DataSync data transfers.
- Amazon EFS: Syncs data to scalable file storage.
- Amazon FSx: Transfers data to managed file systems like FSx for Windows File Server.
- [[Snowball]]: Complements DataSync for large-scale offline transfers.
- [[CloudWatch]]: Monitors DataSync tasks and performance.
- [[Storage Gateway]]: Alternative hybrid gateway approach for ongoing access.

### Related Concepts

- Data Migration: Streamlines moving large datasets to AWS.
- Incremental Sync: Transfers only changed data for efficiency.
- Bandwidth Optimization: Compresses and prioritizes data for faster transfers.
- Data Integrity: Validates data during transfer with checksums.
- Hybrid Cloud: Bridges on-premises data centers with AWS storage services.
- Offline Transfer: Physical devices (Snowball family) for extremely large or constrained-link migrations.
