#Amazon #Service #S3
### Amazon S3

Fully managed object storage service for storing, retrieving, and managing any amount of data with 99.999999999% (11 nines) durability and near-infinite scalability. Organizes data in buckets with unique keys, supporting use cases like backups, data lakes, static websites, and content distribution. Offers flexible storage classes, versioning, lifecycle policies, access controls, and encryption for cost optimization, security, and compliance.

### Storage Classes

- [[S3 Standard]]: Low-latency, high-throughput storage for frequently accessed data (e.g., active content, analytics).
- [[S3 Intelligent-Tiering]]: Automatically moves objects between access tiers based on usage patterns, balancing cost and performance.
- [[S3 Standard-Infrequent Access (IA)]]: Lower storage cost for less frequently accessed data with millisecond access.
- [[S3 One Zone-IA]]: Infrequent access storage in a single Availability Zone, cheaper than Standard-IA.
- [[S3 Glacier]]: Low-cost archival storage with retrieval times from minutes to hours.
- **S3 Glacier Deep Archive**: Cheapest storage for long-term, rarely accessed data with retrieval in hours.
- **S3 Express One Zone**: High-performance, low-latency storage for latency-sensitive workloads in a single AZ.

### Features

- **[[S3 Versioning|Versioning]]**: Maintains multiple object versions for recovery from overwrites or deletions.
- **[[S3 Lifecycle|Lifecycle]]**: Automates object transitions between storage classes or deletes expired data.
- **[[S3 Encryption|Encryption]]**: Supports server-side (SSE-S3, SSE-KMS, SSE-C) and client-side encryption for data security.
- **[[S3 Access Control|Access Control]]**: Uses bucket policies, IAM policies, and ACLs for granular permission management.
- **[[S3 Event Notifications|Event Notifications]]**: Triggers AWS Lambda, SNS, or SQS on bucket events (e.g., uploads, deletions).
- [[S3 Replication|Replication]]: Cross-Region (CRR) or Same-Region (SRR) replication for redundancy or compliance.
- **Static Website Hosting**: Serves web content from buckets with custom domain support.
- **[[S3 Select]]**: Queries specific object data using SQL-like expressions for efficient retrieval.

### Related Services

- Amazon CloudFront: Accelerates S3 content delivery via global CDN.
- AWS Lambda: Processes S3 events for automation.
- Amazon Athena: Queries S3 data using SQL.
- AWS Snowball/Snowcone: Transfers large datasets to/from S3.
- AWS IAM: Manages bucket and object access.
- AWS KMS: Provides encryption keys for S3 security.
- AWS DataSync: Automates data transfers to/from S3.
- Amazon Macie: Protects sensitive data in S3 buckets.

### Related Concepts

- Object Storage: Stores unstructured data as objects with unique keys.
- Data Durability/Availability: 11 nines durability; availability varies by storage class.
- Bucket Policies: JSON rules for access control.
- Event-Driven Architecture: S3 events trigger real-time workflows.
- Data Lake: Centralized S3 storage for analytics.
- Compliance: Supports GDPR, HIPAA, PCI-DSS with encryption and auditing.