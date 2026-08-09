#AWS #Service #Analytics
### OpenSearch

Amazon OpenSearch Service (formerly Elasticsearch) is a managed search and analytics engine. It indexes and queries logs, documents, and other data with full-text search, powers log analytics dashboards (Kibana/OpenSearch Dashboards), and integrates with CloudWatch Logs and Kinesis.

### How It Works

- Data is indexed as JSON documents into indices, which are stored across shards for scalability.
- Documents are inverted-indexed for fast full-text and keyword search.
- Queries use the OpenSearch/Elasticsearch REST API and Query DSL.
- OpenSearch Dashboards (Kibana lineage) provide visualization and exploration.
- OpenSearch Ingestion pipelines stream data from S3, Kinesis, and other sources into the service.
- Integrations such as Lambda and Firehose feed records before indexing.

### Key Features

- Full-text and keyword search over large document sets.
- Managed clusters with automatic scaling, patching, and snapshots.
- Built-in visualization via OpenSearch Dashboards and Kibana.
- Analytics on logs, metrics, and traces.
- Data Prepper pipelines for log enrichment and S3 ingestion.
- Integrates with CloudWatch Logs, Kinesis, Lambda, and S3.
- Cross-cluster search, alerting, and anomaly detection capabilities.

### Common Use Cases

- Centralized log analytics and observability.
- Application and infrastructure monitoring dashboards.
- Full-text search for e-commerce and content applications.
- Security and audit log analysis.
- Vector and semantic search workloads (optional plugins).

### Pricing & Limits

- Billed per node type, size, and count on an hourly basis.
- UltraWarm storage offers lower cost for rarely accessed data.
- EBS-backed or instance-storage data nodes; pricing varies by instance family.
- Cluster and node counts follow service quotas.

### Related Services

- [[Kinesis]]: Streams data into OpenSearch.
- [[CloudWatch]]: Sends logs for search and alerting.
- [[Lambda]]: Processes records before ingestion.
- [[S3]]: Long-term log archival and bulk ingest sources.
- [[SageMaker]]: Vector embeddings for semantic search.

### Related Concepts

- Full-Text Search: Query indexed documents.
- Index: Logical collection of documents.
- Dashboards: Kibana-style visualization.
- Inverted Index: Data structure enabling fast text search.
- Log Analytics: Aggregating and searching log data.
