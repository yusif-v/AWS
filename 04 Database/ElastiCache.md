#AWS #Service #Database
### ElastiCache

Amazon ElastiCache is a fully managed in-memory data store compatible with Redis and Memcached. It powers caching, session stores, leaderboards, and pub/sub messaging, delivering microsecond latency while reducing load on backend databases.

### How It Works
- ElastiCache runs in-memory engines (Redis and Memcached) on managed nodes within a VPC.
- Applications query the cache directly via standard Redis or Memcached protocols; cache misses fall through to the database.
- Redis clusters support replication (primary plus replicas) and automatic failover for high availability.
- TTL policies let cached data expire, keeping the cache fresh and bounded in size.

### Key Features
- Microsecond read and write latency for hot data.
- Redis support includes rich data structures, sorted sets, pub/sub, and Lua scripting.
- Encryption in transit and at rest, with [[KMS]] key support and [[IAM]] access control.
- Automatic patching, node replacement, and scaling.
- Global Datastore for cross-region Redis replication and disaster recovery.
- Memcached compatibility for simple, fast, horizontal caching.

### Common Use Cases
- Caching database query results to reduce load on [[RDS]] and other databases.
- Session state storage for web applications.
- Real-time leaderboards and counters using Redis sorted sets.
- Pub/sub messaging for fan-out notifications.
- Machine-learning feature stores and distributed rate limiting.

### Pricing & Limits
- Billed per node instance-hour based on node type and the number of nodes.
- Cluster mode with sharding scales horizontally across many nodes.
- The free tier includes 750 hours of a small node per month for 12 months.
- Node types range from small general-purpose instances to large memory-optimized instances.

### Related Services

- [[RDS]]: Offloads reads from relational databases.
- [[DynamoDB]]: Offloads reads from NoSQL tables.
- [[DynamoDB DAX]]: DynamoDB-specific in-memory cache.
- [[EC2]]: Hosts the underlying cache nodes.
- [[VPC]]: ElastiCache clusters run inside a VPC.

### Related Concepts

- Redis/Memcached: In-memory engines.
- TTL: Cache expiration policies.
- Cache Hit Ratio: Effectiveness of caching.
- In-Memory Caching: Low-latency data access.
- High Availability: Replication and failover for Redis.
