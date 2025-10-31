#S3 
### S3 Standard-Infrequent Access

Amazon S3 storage class for infrequently accessed data with millisecond access time. Offers 99.9% availability, lower storage cost than Standard, but with retrieval fees. Durable (11 9's), ideal for backups, disaster recovery, and secondary data. Minimum 30-day storage, 128 KB object size.

### Related Services

- [[Amazon S3]]: Core service hosting Standard-IA objects.
- [[AWS Glue]]: Crawls Standard-IA data for ETL.
- [[Amazon Athena]]: Queries data in Standard-IA.
- AWS Lifecycle Policies: Transitions objects to/from Standard-IA.

### Related Concepts

- Storage Optimization: Balances cost and access frequency.
- Retrieval Fees: Charges for data access, unlike Standard.
- Durability/Availability: Matches Standard's durability, slightly lower availability.
- Lifecycle Management: Automates class transitions for cost savings.