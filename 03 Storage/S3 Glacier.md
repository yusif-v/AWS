#AWS #Service #Storage
### S3 Glacier

S3 Glacier is a low-cost archival storage class within Amazon S3 for data that is accessed infrequently and can tolerate retrieval times of minutes to hours. It provides secure, durable archiving with flexible retrieval options (expedited, standard, bulk) and integrates with S3 lifecycle policies.

### How It Works

- Objects are stored as S3 objects in the Glacier storage class and cannot be read directly without a restore request.
- A restore request copies the object to a temporary, retrievable copy for a configurable number of days.
- Retrieval tiers offer different speed/cost trade-offs: Expedited (1–5 minutes, premium), Standard (3–5 hours), and Bulk (5–12 hours, cheapest).
- Data is stored redundantly across multiple Availability Zones with 11 nines durability.
- Lifecycle policies transition objects into Glacier automatically as they age.

### Key Features

- Much lower storage cost than Standard or Infrequent Access classes.
- Flexible retrieval options to balance speed and cost.
- Same 11 nines durability, security, and encryption features as other S3 classes.
- S3 Object Lock supports write-once-read-many (WORM) compliance with versioning.
- Lifecycle integration automates tiering from Standard to IA to Glacier to Deep Archive.
- Works with replication for compliance or disaster recovery.

### Common Use Cases

- Long-term backup and archive of databases, media, and application data.
- Compliance archives with mandated retention periods.
- Media asset archives (video masters, photographs) with rare access.
- Offloading cold data from primary storage to reduce cost.
- Legal and e-discovery record retention.

### Pricing & Limits

- Billed per GB-month of storage plus retrieval fees (per GB and per request) that vary by tier.
- Minimum storage duration of 90 days applies to the Glacier storage class.
- Expedited retrieval requires objects in the Glacier Flexible Retrieval class (formerly Amazon S3 Glacier).
- Early deletion before 90 days incurs a charge as if stored for 90 days.

### Related Services

- [[S3]]: The service hosting the Glacier storage class.
- [[S3 Deep Archive]]: Even lower-cost class with 12–48 hour retrieval.
- [[S3 Lifecycle]]: Automates transitions into and out of Glacier.
- [[Storage Gateway]]: Tape gateway archives virtual tapes to Glacier.
- [[Backup]]: Can archive backups into Glacier.

### Related Concepts

- Archive Storage: Cold data with slower, cost-based retrieval.
- Retrieval Tiers: Expedited/Standard/Bulk balance speed and cost.
- Restore: Copying archived data to a temporary retrievable state.
- Minimum Storage Duration: Early-deletion charges apply before 90 days.
