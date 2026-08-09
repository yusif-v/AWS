#AWS #Service #Database
### DynamoDB DAX

DynamoDB Accelerator (DAX) is an in-memory cache for DynamoDB that delivers single-digit-millisecond read performance. It sits between applications and DynamoDB, caching frequently accessed items to reduce read cost and latency, and is fully managed by AWS with automatic failover and scaling.

### How It Works
- DAX is a write-through cache: writes are applied to DynamoDB first and then cached, so a successful write is never served stale.
- Applications read through the DAX cluster; cache hits are served from memory while misses fall through to DynamoDB.
- Data is distributed across nodes in a cluster made up of a primary and optional read replicas.
- Items can be given a TTL so cached values expire and are refreshed automatically.

### Key Features
- Single-digit-millisecond read latency for frequently accessed (hot) items.
- Reduces read capacity unit consumption on the underlying table, lowering costs.
- Fully managed: automatic node replacement, patching, and scaling.
- Compatible with the DynamoDB API, so applications switch to a DAX endpoint with minimal code change.
- Encrypted at rest, supports [[IAM]] for access control, and runs inside a VPC.

### Common Use Cases
- Real-time bidding, gaming, and ad-tech workloads that need consistent low-latency reads.
- Applications with read-heavy access patterns where a small set of items is accessed repeatedly.
- Caching session state or frequently queried reference data.
- Reducing provisioned read capacity on hot DynamoDB tables.

### Pricing & Limits
- Billed per node instance-hour based on node type and the number of nodes.
- Clusters scale from 1 to 10 nodes; larger node types provide more memory.
- Estimate costs with the AWS Pricing Calculator rather than fixed published figures.
- Not available in every region; check regional availability when planning.

### Related Services

- [[DynamoDB]]: The underlying NoSQL database.
- [[ElastiCache]]: General-purpose in-memory caching.
- [[VPC]]: DAX clusters run inside a VPC for secure network access.

### Related Concepts

- In-Memory Caching: Low-latency reads.
- Read Throughput: Offloads reads from the table.
- TTL: Cache item expiration.
- Cache Hit Ratio: Effectiveness of the cache.
