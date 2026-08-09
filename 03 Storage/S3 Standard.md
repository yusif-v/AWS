#AWS #Service #Storage
### S3 Standard

S3 Standard is the default S3 storage class, designed for frequently accessed data with low latency and high throughput. It provides 99.99% availability and 11 nines durability across at least three Availability Zones, with no retrieval fees and no minimum storage duration.

### How It Works

- Objects are stored redundantly across at least three Availability Zones within a region.
- It is the default class for all objects unless another class is explicitly specified.
- Reads and writes are served with millisecond first-byte latency and high throughput.
- No retrieval fee is charged; you pay per GB stored and per request.
- Data can be transitioned to lower-cost classes via lifecycle policies as it cools.

### Key Features

- 99.99% availability SLA with 11 nines durability.
- No retrieval fees and no minimum object size or storage duration.
- Low latency and high throughput for active data.
- Fully supports encryption, versioning, replication, and static website hosting.
- The default and most flexible S3 storage class.

### Common Use Cases

- Frequently accessed application data, active files, and websites.
- Data lakes, analytics, and big data processing with Athena, Glue, and EMR.
- Static website hosting and content distribution via CloudFront.
- Primary storage before lifecycle-based cost optimization.
- Any workload requiring immediate, frequent access.

### Pricing & Limits

- Billed per GB-month of storage and per 1,000 requests (PUT/GET).
- No retrieval or early-deletion fees.
- Storage costs more per GB than the Infrequent Access and Glacier classes.
- Availability is 99.99%, higher than Standard-IA's 99.9%.

### Related Services

- [[S3]]: The service hosting the Standard class.
- [[S3 Standard-Infrequent Access (IA)]]: Lower-cost class for colder data.
- [[S3 Intelligent-Tiering]]: Auto-tiering alternative.
- [[S3 Lifecycle]]: Transitions Standard data to cheaper classes.
- [[Athena]]: Queries Standard data in place.
- [[CloudFront]]: Distributes Standard-hosted content.

### Related Concepts

- Hot Storage: Data accessed frequently with millisecond latency.
- Durability: 11 nines across multiple Availability Zones.
- Availability: 99.99% monthly uptime SLA.
- No Retrieval Fees: Cost model differs from the Infrequent Access classes.
