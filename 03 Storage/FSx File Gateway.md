#AWS #Service #Storage
### FSx File Gateway

Fully managed hybrid storage service within AWS Storage Gateway, providing low-latency on-premises access to Amazon FSx for Windows File Server via SMB protocol. Caches frequently accessed data locally on gateway appliances, syncs changes to FSx in the cloud for seamless file sharing and backups.

### How It Works

- Deploy the gateway as a VM on-premises (VMware/Hyper-V) configured for the FSx File Gateway mode.
- The gateway connects to Amazon FSx for Windows File Server and presents shared folders over SMB to on-premises clients.
- Frequently accessed data is cached locally on the gateway appliance for low-latency reads and writes.
- Writes are asynchronously synced back to the cloud FSx file system to keep a durable copy.
- On-premises files are accessed through the gateway, while AWS resources (e.g., EC2 in the cloud) access FSx directly.

### Key Features

- Low-latency on-premises access to fully managed FSx for Windows File Server.
- Local cache minimizes latency and reduces reliance on the network link for hot data.
- Combines the durability and features of FSx (AD integration, quotas, deduplication) with local performance.
- Supports standard Windows features such as SMB 3.x, Windows ACLs, and DFS namespace integration.
- Data is synced to FSx for centralized backup, archiving, and disaster recovery.

### Common Use Cases

- Hybrid file shares for Windows-based departments or applications.
- Migrating on-premises file servers to FSx while retaining local read/write performance.
- Centralizing Windows file backups to cloud-managed storage.
- Edge sites with limited bandwidth that still need fast access to hot files.

### Pricing & Limits

- Billed per GB stored in FSx plus a monthly per-gateway fee for the Storage Gateway service.
- Local cache storage on the gateway VM is your own hardware; egress and network costs apply for synced data.
- Pricing differs from File Gateway, which backs onto S3.

### Related Services

- [[Storage Gateway]]: Core service hosting FSx File Gateway mode.
- Amazon FSx for Windows File Server: Cloud file storage accessed via the gateway.
- [[EC2]]: Runs virtual gateways for FSx access.
- [[CloudWatch]]: Monitors gateway performance and metrics.
- AWS Backup: Backs up data stored in FSx via the gateway.

### Related Concepts

- Hybrid Cloud Storage: Extends on-premises access to cloud file systems.
- File Caching: Local storage of hot data for reduced latency.
- SMB Protocol: Enables Windows-compatible file sharing.
- Data Synchronization: Ensures consistency between on-premises and cloud.
- Gateway Modes: Storage Gateway also offers File, Volume, and Tape gateway modes for different storage types.
