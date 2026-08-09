#AWS #Service #Database
### RDS Backups

RDS provides automated backups with point-in-time recovery (restorable to any second in the retention window) and manual snapshots that persist until deleted. Backups and snapshots are stored in S3 and are encrypted if the database is encrypted.

### Related Services

- [[RDS]]: The database service backing up data.
- [[S3]]: Where backups and snapshots are stored.
- [[Backup]]: Centralized backup management.

### Related Concepts

- Point-in-Time Recovery: Restore to any second.
- Retention Period: How long automated backups are kept.
- Snapshots: Manual, persistent backups.
