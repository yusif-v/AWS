#AWS #Service #Database
### DynamoDB Streams

DynamoDB Streams captures item-level changes (create, update, delete) to a DynamoDB table as a time-ordered stream of events. Applications can consume these events to trigger workflows, replicate data, or maintain analytics, and stream records are retained for 24 hours.

### How It Works
- Every item modification generates a stream record containing the keys, the before and after images (if enabled), and metadata about the change.
- Records are organized into shards that can be read in order; AWS manages shard lifecycle and scaling.
- Consumers read via the DynamoDB Streams API, and [[Lambda]] integrates natively through an event source mapping.
- Records expire after 24 hours, so consumers must process events in a timely fashion.

### Key Features
- Exactly-once ordering per shard within each stream view, enabling reliable change data capture.
- No additional cost to enable; you pay only for reads of the stream.
- Integration with [[Lambda]], [[Kinesis]], and [[EventBridge]] for event-driven architectures.
- Supports TRIM_HORIZON and LATEST iteration strategies for flexible consumption.
- Works with both on-demand and provisioned capacity mode tables.

### Common Use Cases
- Event-driven processing, such as updating derived tables or search indexes when source data changes.
- Real-time analytics pipelines that aggregate changes for dashboards.
- Cross-region replication or maintaining an audit trail of changes.
- Triggering downstream workflows, such as notifications via [[SNS]] or queues via [[SQS]].

### Pricing & Limits
- Streams are free to enable; charges apply only for read requests against the stream.
- Records are retained for 24 hours by default.
- Shard scaling is automatic and managed by AWS.

### Related Services

- [[DynamoDB]]: The source table for changes.
- [[Lambda]]: Processes stream records via event source mapping.
- [[Kinesis]]: Alternative streaming data pipeline.
- [[EventBridge]]: Routes stream-driven events to targets.
- [[SNS]]: Notifications triggered by table changes.
- [[SQS]]: Queues for decoupled processing of stream events.

### Related Concepts

- Change Data Capture: Recording modifications.
- Event-Driven Architecture: React to table changes.
- Streams TTL: 24-hour record retention.
- Exactly-Once Ordering: Sequential processing per shard.
