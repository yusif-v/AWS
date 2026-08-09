#AWS #Service #Database
### DynamoDB DAX

DynamoDB Accelerator (DAX) is an in-memory cache for DynamoDB that delivers single-digit-millisecond read performance. It sits between applications and DynamoDB, caching frequently accessed items to reduce read cost and latency, and is managed by AWS with automatic failover.

### Related Services

- [[DynamoDB]]: The underlying NoSQL database.
- [[ElastiCache]]: General-purpose in-memory caching.

### Related Concepts

- In-Memory Caching: Low-latency reads.
- Read Throughput: Offloads reads from the table.
- TTL: Cache item expiration.
