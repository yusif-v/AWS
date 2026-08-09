#AWS #Service #Storage
### EFS

Fully managed, scalable file storage service for shared access across multiple EC2 instances, containers, or on-premises servers. Uses NFS protocol, supports thousands of concurrent connections, and offers Standard and Infrequent Access storage classes. Ideal for content management, web serving, and big data analytics.

### How It Works

- Create a file system in a VPC and mount it on Linux instances via NFSv4.1 over a mount target.
- Mount targets are placed in each Availability Zone of the VPC to provide highly available local access.
- Storage grows and shrinks automatically as files are added or removed; no capacity provisioning is required.
- Access is controlled with POSIX permissions, security groups, and IAM policies.
- Throughput scales with file system size (bursting) or can be provisioned for consistent performance.

### Key Features

- Elastic, pay-as-you-go storage that scales to petabytes without planning capacity.
- Supports thousands of concurrent NFS connections with strong data consistency.
- Lifecycle management transitions files to EFS Infrequent Access (IA) for cost savings.
- Mountable by EC2, [[ECS]], [[EKS]], [[Lambda]] (via access points), and on-premises via Direct Connect or VPN.
- File systems can be used across AZs within a region or replicated across regions.
- Access points simplify shared-data access for applications and containers.

### Common Use Cases

- Shared web content and application files across a fleet of EC2 instances.
- Home directories and content management systems.
- Big data and analytics workloads sharing staging data.
- Serverless workloads where [[Lambda]] functions read/write common files.
- Lift-and-shift migrations of Linux file-based applications.

### Pricing & Limits

- Billed per GB-month of storage used, plus optional provisioned throughput.
- EFS IA has a lower per-GB cost but a retrieval fee and a minimum file size for eligibility.
- Infrequent Access has a minimum storage duration of 90 days.
- Bursting throughput scales with storage; provisioned throughput is available for consistent performance.

### Related Services

- [[EC2]]: Mounts EFS for shared file storage across instances.
- [[Lambda]]: Accesses EFS for serverless file storage.
- Amazon ECS/EKS: Uses EFS for containerized application storage.
- [[DataSync]]: Transfers data to/from EFS.
- [[CloudWatch]]: Monitors EFS performance and usage metrics.

### Related Concepts

- Network File System (NFS): Protocol enabling shared file access across systems.
- Scalability: Automatically scales storage without provisioning.
- Storage Classes: Standard for frequent access; Infrequent Access for cost savings.
- Data Consistency: Strong consistency for multi-user file operations.
- File Storage: Hierarchical folders and files accessed over a network, unlike block or object storage.
