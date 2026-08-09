#AWS #Service #Database
### DynamoDB

Amazon DynamoDB is a fully managed NoSQL database service built for high-performance, scalable applications. It supports key-value and document data models with low-latency access, and handles automatic scaling, global tables, encryption, and backups so teams can focus on building features. It is a popular choice for gaming, IoT, and mobile apps.

### How It Works
- Data is stored as items within tables, addressed by a partition key and optional sort key that determine how data is distributed across partitions.
- The service automatically partitions data across many servers to deliver consistent performance at scale.
- Two capacity modes are supported: on-demand (pay per request) and provisioned (set read/write capacity units).
- Reads can be eventually consistent (cheaper and faster) or strongly consistent (always the latest value).
- Global Tables replicate data across multiple regions for low-latency access and disaster recovery.

### Key Features
- Single-digit-millisecond latency for reads and writes at any scale.
- Automatic scaling in on-demand mode, plus auto scaling for provisioned capacity.
- Global Tables for active-active multi-region replication.
- Encryption at rest via [[KMS]] and fine-grained access control via [[IAM]] Policies.
- Point-in-time recovery and on-demand backups.
- Integrated with [[Lambda]] and [[DynamoDB Streams]] for event-driven processing.

### Common Use Cases
- High-traffic web, mobile, gaming, and ad-tech applications with unpredictable workloads.
- Session stores, leaderboards, and shopping carts that need low-latency reads and writes.
- IoT device telemetry ingestion at high write rates.
- Serverless application backends built on [[API Gateway]] and [[Lambda]].

### Pricing & Limits
- Billed by read/write capacity: on-demand charges per request, provisioned charges per capacity unit.
- Storage is billed per GiB-month, plus charges for backups and stream reads.
- The free tier includes 25 GB of storage, 25 WCU, and 25 RCU per month.
- Tables have no practical limit on size or throughput; partitions scale automatically.

### Related Services

- [[Lambda]]: Triggers functions on DynamoDB events (e.g., data changes).
- [[API Gateway]]: Exposes DynamoDB data via RESTful APIs.
- [[CloudWatch]]: Monitors DynamoDB performance metrics and capacity.
- [[Glue]]: Crawls DynamoDB for data cataloging and ETL.
- [[S3]]: Stores DynamoDB backups or exported data.
- [[DynamoDB DAX]]: In-memory cache for low-latency reads.
- [[DynamoDB Streams]]: Captures data changes for real-time processing.
- [[IAM]]: Controls access to tables and data.

### Related Concepts

- NoSQL Databases: Schema-less storage for unstructured or semi-structured data.
- Eventual vs. Strong Consistency: Options for read consistency based on application needs.
- Partitioning: Distributes data across servers for scalability and performance.
- DynamoDB Streams: Captures data changes for real-time processing.
- Regions & Availability Zones: Global Tables replicate data across regions.
