#Amazon #Service 
### Amazon EFS

Fully managed, scalable file storage service for shared access across multiple EC2 instances, containers, or on-premises servers. Uses NFS protocol, supports thousands of concurrent connections, and offers Standard and Infrequent Access storage classes. Ideal for content management, web serving, and big data analytics.

### Related Services

- Amazon EC2: Mounts EFS for shared file storage across instances.
- [[AWS Lambda]]: Accesses EFS for serverless file storage.
- Amazon ECS/EKS: Uses EFS for containerized application storage.
- [[AWS DataSync]]: Transfers data to/from EFS.
- Amazon CloudWatch: Monitors EFS performance and usage metrics.

### Related Concepts

- Network File System (NFS): Protocol enabling shared file access across systems.
- Scalability: Automatically scales storage without provisioning.
- Storage Classes: Standard for frequent access; Infrequent Access for cost savings.
- Data Consistency: Strong consistency for multi-user file operations.