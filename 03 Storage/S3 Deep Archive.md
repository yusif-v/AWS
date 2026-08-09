#AWS #Service #Storage
### S3 Deep Archive

S3 Deep Archive is the lowest-cost S3 storage class for rarely accessed, long-term retention (e.g., compliance archives). Retrieval takes 12 to 48 hours and objects must be stored for at least 180 days, making it appropriate only for cold data.

### How It Works

- Objects transition into S3 Deep Archive via lifecycle policies or by storing them directly to the class.
- Data is stored redundantly across at least three Availability Zones with the same 11 nines durability as other S3 classes.
- Retrieval is a two-step process: a restore request first, then access once restoration completes (standard/bulk take 12–48 hours).
- Because retrieval is slow, the class is designed for data that is effectively never accessed directly.

### Key Features

- Lowest storage cost per GB of any AWS storage tier.
- Same 11 nines durability and encryption options as other S3 classes.
- Lifecycle integration automates transitions from Standard, IA, or Glacier.
- Works with S3 Object Lock for WORM compliance (with versioning enabled).
- Bulk retrieval supports very large-scale restores at reduced retrieval cost.

### Common Use Cases

- Regulatory, legal, and compliance archives that must be retained for years.
- Historical media, logs, and research data with extremely rare access.
- Long-term data retention after initial processing completes.
- Cold archival for backup vaults and medical/financial record retention.

### Pricing & Limits

- Billed per GB-month of storage, per GB of retrieval, and per 1,000 requests.
- Minimum storage duration of 180 days applies (early deletion is billed as if stored 180 days).
- Retrieval typically takes 12–48 hours; there is no real-time retrieval option.
- Objects should be at least 128 KB for the class to be cost-efficient.

### Related Services

- [[S3]]: The service providing this storage class.
- [[S3 Lifecycle]]: Automates transitions into Deep Archive.
- [[S3 Glacier]]: Faster archival alternative.

### Related Concepts

- Retrieval Time: Hours, not minutes.
- Minimum Storage Duration: 180-day commitment.
- Archival: Long-term, low-access data.
- Storage Classes: S3 tiers balancing cost, access latency, and retrieval fees.
- WORM/Immutable Storage: S3 Object Lock prevents modification or deletion for compliance.
