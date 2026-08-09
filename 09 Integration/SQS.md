#AWS #Service #Integration
### SQS

Fully managed message queuing service for decoupling and scaling microservices, distributed systems, and serverless applications. Supports standard queues (high throughput, at-least-once delivery) and FIFO queues (exactly-once processing, order preserved). Features visibility timeouts, dead-letter queues, long polling, and encryption.

### How It Works
- Producers send messages to a queue; consumers poll and receive messages for processing.
- Messages are stored redundantly across multiple Availability Zones for durability.
- A visibility timeout hides a received message from other consumers until processing completes or times out.
- Long polling waits for messages and reduces empty responses and cost; short polling checks immediately.
- Consumers must delete a message after processing; otherwise it becomes visible again for retries.

### Key Features
- Standard queues deliver at-least-once with high throughput and no ordering guarantees.
- FIFO queues provide strict ordering, exactly-once processing, and support message groups and deduplication.
- Dead-letter queues capture messages that fail repeatedly for troubleshooting.
- Server-side encryption with KMS and client-side encryption options for sensitive payloads.
- Batching of up to 10 messages per request to reduce costs and improve throughput.
- Configurable message retention up to 14 days and message size up to 256 KB.
- Lambda event-source mapping polls queues and invokes functions without custom worker code.

### Common Use Cases
- Decoupling web frontends from backend processing to absorb traffic spikes.
- Building job queues for tasks such as thumbnail generation, emails, or report jobs.
- Fan-out from SNS to multiple SQS queues for parallel downstream processing.
- Buffering data between producers and consumers with different throughput profiles.
- Reliable hand-off between microservices with retry and DLQ-based failure handling.

### Pricing & Limits
- Billed per request, with each request handling up to 10 messages via batching; includes a monthly free tier of one million requests.
- No minimum fees or per-message-volume charges; you pay only for API requests.
- 256 KB max message size, 14 days max retention, and configurable visibility timeout.
- FIFO queues have lower throughput than standard queues but support higher rates with batching.

### Related Services

- [[SNS]]: Publishes messages to SQS for fan-out scenarios.
- [[Lambda]]: Triggers functions from SQS messages.
- [[EC2]]: Sends/receives messages for distributed apps.
- [[CloudWatch]]: Monitors queue metrics and alarms.
- [[IAM]]: Controls access to queues.
- [[Kinesis]]: Streaming alternative for real-time ordered data.
- [[Step Functions]]: Orchestrates workflows that consume queued messages.
- [[EventBridge]]: Routes events into queues for processing.
- [[DynamoDB Streams]]: Ordered change-data stream alternative.

### Related Concepts

- Message Queuing: Asynchronous communication between components.
- Decoupling: Reduces dependencies for fault tolerance.
- FIFO vs. Standard Queues: Ordered/exactly-once vs. high-throughput/at-least-once.
- Dead-Letter Queues: Handles failed message processing.
- Visibility Timeout: Hides in-flight messages during processing.
- Long Polling: Reduces empty responses and polling cost.
