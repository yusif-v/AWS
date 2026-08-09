#AWS #Service #Storage
### S3 Event Notifications

S3 Event Notifications send messages to AWS services when specific events occur in a bucket, such as object creation, deletion, or restore completion. Events are published asynchronously to destinations like Lambda, SNS, SQS, or EventBridge, enabling event-driven automation without polling.

### How It Works

- Configure a notification on a bucket, optionally scoped by prefix (e.g., `uploads/`) and suffix (e.g., `.jpg`).
- When a matching event occurs (`s3:ObjectCreated:*`, `s3:ObjectRemoved:*`, `s3:ObjectRestore:*`, etc.), S3 publishes a JSON event message.
- Deliveries go to a Lambda function, SNS topic, or SQS queue, each requiring a resource policy that permits S3 to send events.
- Alternatively, enable EventBridge for the bucket to route S3 events alongside other AWS events.
- Notifications are best-effort: messages can arrive more than once or out of order, so consumers should be idempotent.

### Key Features

- Filtering by event type, prefix, and suffix reduces irrelevant notifications.
- Asynchronous, near-real-time delivery (typically seconds) without polling.
- Supports many object-level event types, including versioned and replica events.
- EventBridge integration enables complex event routing, matching, and enrichment.
- Composes with versioning and replication for complete change tracking.

### Common Use Cases

- Triggering a [[Lambda]] function to process every uploaded file (image resize, validation, ETL).
- Sending a notification to [[SNS]] when new objects arrive for downstream alerting.
- Feeding [[SQS]] queues for decoupled, reliable batch processing of object changes.
- Kicking off data pipelines ([[Glue]], [[Athena]]) when new data lands in a bucket.
- Building event-driven data lakes and automated ingestion workflows.

### Pricing & Limits

- Event notifications themselves are free; you pay only for destination service usage (Lambda invocations, SNS/SQS messages, EventBridge events).
- A bucket can have up to 1,000 notification configurations.
- EventBridge support varies by region.

### Related Services

- [[S3]]: Emits the bucket events.
- [[Lambda]]: Serverless function invoked on object events.
- [[SNS]]: Pub/sub notifications on S3 events.
- [[SQS]]: Queue-based processing of S3 events.
- [[EventBridge]]: Advanced event routing from S3.
- [[S3 Versioning]]: Event generation is version-aware.

### Related Concepts

- Event-Driven Architecture: Systems react to events rather than polling.
- Message Queue: SQS buffers events for decoupled, reliable processing.
- Notification Filtering: Prefix/suffix rules limit which events are delivered.
- Idempotency: Consumers tolerate duplicate or reordered deliveries.
