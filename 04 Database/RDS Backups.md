#AWS #Service #Database
### RDS Backups

RDS provides automated backups with point-in-time recovery (restorable to any second in the retention window) and manual snapshots that persist until deleted. Backups and snapshots are stored in S3 and are encrypted if the database is encrypted.

### How It Works
- Automated backups are taken daily, and transaction logs are captured continuously, enabling restores to any second within the retention window.
- Manual snapshots are user-initiated copies of the storage volume that persist until explicitly deleted.
- Restoring from a backup or snapshot creates a new DB instance from the restored data.
- Automated backup retention is configurable from 0 to 35 days; manual snapshots have no retention limit.

### Key Features
- Point-in-time recovery across the entire retention window.
- Restores create a new instance without touching the production database.
- Backups and snapshots are stored in S3 with the same encryption as the source database.
- Integrated with [[Backup]] for centralized, policy-based backup management.
- Backups are taken from the storage layer and do not impact database performance.
- Enabling backups also enables cross-region snapshot copy for disaster recovery.

### Common Use Cases
- Disaster recovery: restore databases after accidental deletion or corruption.
- Compliance: retain snapshots for audit and regulatory requirements.
- Database cloning for development and testing.
- Migration between regions via cross-region snapshot copies.

### Pricing & Limits
- Backup storage is billed per GiB-month; automated backup storage up to 100% of the instance size is included free.
- Automated backup retention ranges from 0 to 35 days.
- Manual snapshots incur storage costs until deleted.
- Restores are billed as a new instance at standard RDS rates.

### Related Services

- [[RDS]]: The database service backing up data.
- [[S3]]: Where backups and snapshots are stored.
- [[Backup]]: Centralized backup management.
- [[KMS]]: Encrypts backups and snapshots.

### Related Concepts

- Point-in-Time Recovery: Restore to any second.
- Retention Period: How long automated backups are kept.
- Snapshots: Manual, persistent backups.
- Disaster Recovery: Restore data after loss or corruption.
