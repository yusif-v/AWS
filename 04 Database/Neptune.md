#AWS #Service #Database
### Neptune

Amazon Neptune is a fully managed graph database service optimized for storing and querying highly connected data. It supports both property graph and RDF models, with Gremlin and SPARQL query languages, and offers high performance, scalability, and availability for social networks, recommendation engines, and fraud detection.

### How It Works
- Data is stored as nodes (vertices), edges (relationships), and properties, optimized for relationship-heavy traversal queries.
- Neptune supports open graph query languages: Gremlin for property graphs and SPARQL for RDF/W3C standards.
- The engine uses a cluster architecture with a primary writer and up to 15 read replicas.
- Storage replicates six ways across three Availability Zones for durability and availability.
- Fast graph traversals avoid the expensive JOINs relational databases require for connected data.

### Key Features
- High performance for graph traversals and complex relationship queries.
- ACID transactions for consistent, multi-step graph operations.
- Encryption at rest and in transit, integrated with [[KMS]] and [[IAM]].
- Automatic backups, snapshots, and point-in-time recovery.
- Neptune Streams for change capture into event-driven pipelines.
- Neptune ML for graph-based machine learning predictions.

### Common Use Cases
- Social networks: modeling users, friendships, and interactions.
- Fraud detection: identifying rings and suspicious connections in transactions.
- Recommendation engines: finding related products, people, or content.
- Knowledge graphs and identity graphs.
- Network and IT dependency mapping.

### Pricing & Limits
- Billed per instance hour for compute plus per-GiB-month for storage.
- Clusters support up to 15 read replicas and scale storage automatically to 128 TiB.
- Query performance depends on the instance class; memory-optimized instances speed up traversals.

### Related Services

- [[EC2]]: Hosts applications that query Neptune databases.
- [[CloudWatch]]: Monitors Neptune performance and operational metrics.
- [[IAM]]: Manages access to Neptune resources and queries.
- [[Lambda]]: Integrates with Neptune for serverless query processing.
- [[S3]]: Stores Neptune backups and export data.
- [[KMS]]: Encrypts Neptune storage and backups.

### Related Concepts

- Graph Databases: Store data as nodes and edges for efficient relationship queries.
- Property Graph vs. RDF: Neptune supports both for flexible data modeling.
- High Availability: Multi-AZ deployments and read replicas ensure uptime and scalability.
- ACID Transactions: Ensures data consistency for complex graph operations.
- Regions & Availability Zones: Storage replicated across three AZs.
