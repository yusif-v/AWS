#AWS #Service #Storage
### Storage Gateway

AWS Storage Gateway provides hybrid cloud storage, connecting on-premises environments to AWS. Modes include File Gateway (SMB/NFS to S3), Volume Gateway (block storage with snapshots), and Tape Gateway (virtual tapes to S3/Glacier).

### How It Works

- A gateway appliance runs as a VM on-premises (VMware, Hyper-V) or as a hardware appliance, presenting cloud storage through familiar protocols.
- File Gateway presents SMB/NFS file shares backed by S3, caching hot data locally.
- Volume Gateway presents iSCSI block volumes stored in S3, with point-in-time snapshots.
- Tape Gateway presents an iSCSI virtual tape library, archiving virtual tapes to S3 and [[S3 Glacier]].
- Data written through the gateway is asynchronously uploaded to AWS, then durable in the cloud.

### Key Features

- Low-latency access to cloud storage via a local cache.
- Three gateway modes (File, Volume, Tape) cover file, block, and tape workloads.
- Integrates with S3 storage classes and lifecycle for cost optimization.
- Snapshots of volumes and tapes enable disaster recovery.
- Secure transfer with TLS encryption and IAM-based access control.

### Common Use Cases

- Extending on-premises file shares to S3 without rewriting applications.
- Backing up on-premises servers to cloud-based virtual tapes.
- Disaster recovery using volume snapshots stored in AWS.
- Hybrid migrations where applications must keep local access while data is in the cloud.
- Cost-effective archival of backups and media.

### Pricing & Limits

- Billed per gateway (monthly fee) plus per-GB stored in AWS and data transfer costs.
- Local cache storage is on your own hardware; only uploaded cloud data is billed.
- Volume and tape storage are stored as S3 objects, so S3 storage and request charges apply.

### Related Services

- [[S3]]: Backend storage for file and tape gateways.
- [[S3 Glacier]]: Archival for virtual tapes.
- [[DataSync]]: Large-scale data transfer to AWS.
- [[FSx File Gateway]]: A gateway mode that fronts Amazon FSx for Windows File Server.
- [[Backup]]: Can back up gateway-protected resources.

### Related Concepts

- Hybrid Cloud: On-premises + AWS storage.
- Caching: Local cache for low-latency access.
- Snapshots: Point-in-time recovery to AWS.
- Virtual Tape Library (VTL): Software-emulated tape drives backed by S3/Glacier.
- iSCSI: Block-level protocol used by Volume and Tape gateways.
