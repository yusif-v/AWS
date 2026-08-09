#AWS #Service #Compute
### EC2 Storage

EC2 instances use two block storage options: EBS volumes (durable, network-attached, detached and reattached) and instance store volumes (ephemeral, physically attached, lost on stop). File-level shared storage can be added via EFS, and object storage via S3.

### Related Services

- [[EBS]]: Persistent block storage for instances.
- [[EFS]]: Shared file storage for Linux instances.
- [[S3]]: Object storage for data exchange and backup.

### Related Concepts

- [[EC2 AMIs]]: Images store root volumes.
- Durability: EBS persists independently of the instance.
- Ephemeral Storage: Instance store data is temporary.
