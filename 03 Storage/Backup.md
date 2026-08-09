#AWS #Service #Storage
### Backup

Fully managed, centralized backup service for automating and managing backups across AWS services like EC2, EBS, RDS, DynamoDB, EFS, and Storage Gateway. Supports scheduled backups, retention policies, and cross-region replication. Ensures data protection and compliance with encryption and access controls.

### How It Works

- Backup plans define a schedule (frequency), a lifecycle (how long backups are kept), and the resources to include.
- A backup vault stores recovery points; vaults are region-specific and can be configured with vault lock for immutability.
- Supported resources are protected through native integrations (e.g., EC2 instances, EBS volumes, RDS databases, DynamoDB tables, EFS file systems).
- Cross-region backup copies recovery points to a secondary region, while cross-account copies enable centralization and isolation.
- Restores are performed at the recovery-point level, either to the original resource or to a new resource in the same or a different region.

### Key Features

- Centralized management of backups across many AWS services from a single console.
- Backup policies automate scheduling, retention, and cross-region copying without scripting.
- Vault Lock (WORM) enforces compliance by preventing backup deletion, even by privileged users.
- Point-in-time restore for many supported services, down to seconds for some databases.
- On-demand backups complement scheduled backups for pre-change or pre-migration snapshots.
- Monitoring and auditing via [[CloudWatch]] and [[CloudTrail]].

### Common Use Cases

- Compliance-driven retention (e.g., regulatory requirements for multi-year retention).
- Disaster recovery by replicating backups to a secondary region.
- Protection of production databases and application data against accidental deletion or corruption.
- Backup of hybrid workloads via [[Storage Gateway]] and on-premises resources.
- Replacing per-service backup scripts with a single, centrally managed service.

### Pricing & Limits

- Billed per GB of backed-up data, per backup copy, and per data transferred across regions.
- Costs vary by source service (EC2, RDS, DynamoDB, etc.) and whether backups are stored in the backup vault or S3.
- No minimum storage duration for most backups; vault lock adds no upfront cost but applies retention rules.
- Cross-region and cross-account copies incur additional storage and transfer charges.

### Related Services

- [[EC2]]: Backs up instances and attached EBS volumes.
- [[EBS]]: Creates snapshots for block storage backups.
- [[RDS]]: Automates database backups and restores.
- [[DynamoDB]]: Backs up tables with point-in-time recovery.
- [[S3]]: Supports backup storage and lifecycle policies.
- [[RDS Backups]]: Details RDS-native backup and point-in-time recovery.

### Related Concepts

- Backup Policies: Defines schedules, retention, and backup scope in backup plans.
- Point-in-Time Recovery: Restores data to a specific moment for supported services.
- Data Protection: Uses encryption (AWS KMS) and IAM policies for secure backups.
- Disaster Recovery: Enables cross-region backups for high availability and resilience.
- Immutable Backups: Vault Lock prevents deletion to defeat ransomware and accidental loss.
- Retention Policy: Defines how long recovery points are kept and when they expire.
