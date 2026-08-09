#AWS #Service #Storage
### S3 Standard-Infrequent Access (IA)

Amazon S3 storage class for infrequently accessed data with millisecond access time. Offers 99.9% availability, lower storage cost than Standard, but with retrieval fees. Durable (11 9's), ideal for backups, disaster recovery, and secondary data. Minimum 30-day storage, 128 KB object size.

### How It Works

- Data is stored redundantly across at least three Availability Zones, matching Standard durability.
- It is an infrequent-access class, so it is accessed rarely but must be available immediately.
- A per-GB retrieval fee applies whenever an object is accessed.
- Lifecycle policies can transition data in and out of Standard-IA automatically.

### Key Features

- Millisecond first-byte latency, the same as S3 Standard.
- Lower storage cost than Standard for infrequently accessed data.
- Same 11 nines durability as Standard, with slightly lower 99.9% availability.
- Automatic lifecycle transition from Standard via [[S3 Lifecycle]].
- Fully supports encryption, versioning, and replication.

### Common Use Cases

- Backups and disaster recovery copies that are rarely read.
- Long-term storage of secondary datasets.
- Infrequently accessed application data, such as older user files.
- Compliance archives that require fast access when needed.
- Data migrated from Standard to reduce storage cost.

### Pricing & Limits

- Billed per GB-month of storage plus a retrieval fee per GB accessed.
- Minimum storage duration of 30 days applies.
- Minimum object size of 128 KB for cost efficiency.
- More expensive to retrieve than Standard, which has no retrieval fee.

### Related Services

- [[S3]]: Core service hosting Standard-IA objects.
- [[Glue]]: Crawls Standard-IA data for ETL.
- [[Athena]]: Queries data in Standard-IA.
- AWS Lifecycle Policies: Transitions objects to/from Standard-IA.

### Related Concepts

- Storage Optimization: Balances cost and access frequency.
- Retrieval Fees: Charges for data access, unlike Standard.
- Durability/Availability: Matches Standard's durability, slightly lower availability.
- Lifecycle Management: Automates class transitions for cost savings.
- Minimum Duration: 30-day commitment before early-deletion charges.
- Infrequent Access: Cost-effective tier for rarely accessed data.
