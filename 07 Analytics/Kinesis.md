#AWS #Service #Analytics
### Kinesis

Fully managed service for real-time data streaming, processing, and analytics. Includes Kinesis Data Streams for high-throughput data ingestion, Kinesis Data Firehose for simplified data delivery to destinations, Kinesis Data Analytics for real-time SQL-based processing, and Kinesis Video Streams for video data. Ideal for IoT, log analytics, and real-time applications.

### How It Works

- Kinesis Data Streams ingests records into shards; each shard provides fixed read/write capacity, scaling horizontally as shards are added.
- Records are stored in order within a shard and retained for a configurable period (default 24 hours).
- Consumers such as Lambda functions, Kinesis Data Analytics, and custom applications read and process records in near real time.
- Kinesis Data Firehose buffers incoming data and delivers it to destinations such as S3, Redshift, OpenSearch, and Splunk.
- Kinesis Video Streams captures and streams video from edge devices for machine learning and playback.

### Key Features

- Real-time ingestion: Processes streaming data with low latency.
- Shard-based scaling: Add shards to increase Data Streams throughput.
- Data Firehose: Fully managed delivery with buffering and transformation, no code required.
- Data Analytics: SQL-based and Flink-based processing of streams in real time.
- Integrates with Lambda, S3, Redshift, OpenSearch, CloudWatch, and SageMaker.
- Supports multiple producers and consumers per stream.

### Common Use Cases

- IoT telemetry ingestion and processing.
- Real-time log and application metrics streaming.
- Clickstream analysis for personalization and monitoring.
- Feeding real-time analytics into warehouses and dashboards.
- Video stream capture for Rekognition or custom ML analysis.

### Pricing & Limits

- Data Streams billed per shard-hour plus per GB ingested and retrieved.
- Firehose billed per GB ingested into the delivery stream.
- Data Analytics billed per amount of processing capacity consumed.
- Per-shard limits define read/write throughput for the stream.

### Related Services

- [[S3]]: Stores processed or archived streaming data.
- [[Lambda]]: Processes Kinesis streams in real-time.
- [[Redshift]]: Receives data from Kinesis Firehose for data warehousing.
- [[CloudWatch]]: Monitors Kinesis performance and stream metrics.
- [[IAM]]: Controls access to Kinesis streams and resources.
- [[OpenSearch]]: Search destination for streaming data.
- [[DynamoDB]]: Stores processed streaming results.
- [[Rekognition]]: Analyzes video from Kinesis Video Streams.
- [[Glue]]: ETL processing of streamed data.

### Related Concepts

- Real-Time Streaming: Ingests and processes data with minimal latency.
- Data Sharding: Distributes data across shards for scalable processing in Kinesis Data Streams.
- Firehose Delivery: Simplifies data transformation and loading to destinations.
- Stream Processing: Enables continuous analysis of data as it arrives.
- Producer/Consumer: Decoupled writers and readers over the same stream.
