#AWS #Service #Storage
### S3 One Zone-IA

S3 One Zone-Infrequent Access (One Zone-IA) is a lower-cost storage class for infrequently accessed data that does not require multi-AZ resilience. Data is stored in a single Availability Zone, making it cheaper than Standard-IA but vulnerable to AZ loss, with millisecond retrieval and a minimum 30-day storage duration.

### How It Works

- Objects are stored in a single Availability Zone rather than replicated across three.
- It is an infrequent-access class, ideal for data that is rarely retrieved but must be available immediately.
- Because it uses only one AZ, the class is not resilient to Availability Zone destruction.
- Objects can be transitioned to and from One Zone-IA via lifecycle policies.

### Key Features

- Lower storage cost than Standard-IA and Standard.
- Millisecond first-byte latency for immediate retrieval.
- Same 11 nines durability as other S3 classes, but only within a single AZ.
- Encryption and access control features identical to other classes.
- Lifecycle-compatible for automated tiering.

### Common Use Cases

- Secondary backups and disaster-recovery copies that can be recreated.
- Reproducible data, such as cached content or derived datasets.
- Staging data used briefly before moving to more durable storage.
- Data where loss of a single Availability Zone is acceptable.

### Pricing & Limits

- Billed per GB-month of storage with a per-GB retrieval fee when read.
- Minimum storage duration of 30 days applies.
- No minimum object size (unlike Standard-IA's 128 KB minimum).
- Costs less than Standard-IA because redundancy is reduced to one AZ.

### Related Services

- [[S3]]: The service hosting the One Zone-IA class.
- [[S3 Standard-Infrequent Access (IA)]]: Multi-AZ IA alternative with higher cost.
- [[S3 Lifecycle]]: Automates transitions to and from One Zone-IA.
- [[S3 Replication]]: Can replicate data out of One Zone-IA for resilience.

### Related Concepts

- Single Availability Zone: Data redundancy is limited to one AZ.
- Infrequent Access: Lower storage cost, retrieval fees, 30-day minimum.
- Durability: 11 nines durability within the single AZ.
- Availability Trade-Off: Lower cost at the expense of AZ-loss resilience.
