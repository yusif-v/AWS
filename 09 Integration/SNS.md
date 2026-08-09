#AWS #Service #Integration
### SNS

Fully managed messaging service for sending notifications and messages to a large number of subscribers or endpoints. Uses a publish-subscribe (pub/sub) model, supporting topics for broadcasting messages via email, SMS, HTTP, mobile push, SQS, or Lambda. Scales automatically and ensures reliable, low-latency delivery.

### How It Works
- Publishers send messages to a topic; SNS fans the message out to every subscribed endpoint.
- Subscription types include email, SMS, HTTP/HTTPS, mobile push (APNs/FCM), Lambda, SQS queues, and EventBridge.
- Subscription filter policies let a topic deliver only matching messages to each subscriber.
- Message attributes carry structured metadata alongside the message body for filtering and routing.
- SNS handles delivery retries with exponential backoff and dead-letter queues for failed deliveries.

### Key Features
- Fan-out to many endpoints from a single publish call, enabling high-throughput distribution.
- FIFO topics guarantee strict ordering and exactly-once delivery to SQS FIFO subscribers.
- Message Data Protection policies can detect, encrypt, or block sensitive content such as PII.
- Server-side encryption with KMS and fine-grained access control with IAM and topic policies.
- Delivery status logging to CloudWatch and dead-letter queue support for email, SMS, HTTP, and Lambda deliveries.
- SMS supports two-way messaging, sender IDs, and delivery receipts.

### Common Use Cases
- Application and user notifications via email, SMS, and mobile push.
- Fan-out of S3 and CloudWatch events to multiple consumers (e.g., multiple SQS queues).
- Broadcasting transactional messages to groups of services.
- Mobile push notifications to APNs, FCM, and other push providers.
- System health and alarm notifications from CloudWatch alarms.

### Pricing & Limits
- Billed per published message, with messages over 64 KB charged in 64 KB increments.
- SMS delivery is billed per message and per destination country; email and HTTP deliveries have their own rates.
- Includes a monthly free tier of one million publishes for most accounts.
- Delivery to SQS, Lambda, and HTTP endpoints incurs normal costs on the receiving service.

### Related Services

- [[Lambda]]: Processes SNS messages for event-driven workflows.
- [[SQS]]: Receives SNS messages for queue-based processing.
- [[CloudWatch]]: Monitors SNS metrics and delivery status.
- [[IAM]]: Controls access to SNS topics and subscriptions.
- [[S3]]: Triggers SNS notifications for bucket events.
- [[SES]]: Email delivery alternative for rich transactional mail.
- [[EventBridge]]: Event bus alternative for event-driven routing.
- [[Kinesis]]: Streaming option for high-volume data.
- [[Step Functions]]: Orchestration triggered by SNS notifications.
- [[DynamoDB]]: Receives messages via streams and event-driven consumers.

### Related Concepts

- Publish-Subscribe Messaging: Publishers send messages to topics; subscribers receive them.
- Fan-Out Architecture: Distributes messages to multiple endpoints simultaneously.
- Message Filtering: Subscribers receive only relevant messages based on filters.
- Scalability: Handles high message volumes with automatic scaling.
- Dead-Letter Queue: Captures undeliverable messages for investigation.
- Mobile Push: Delivery to APNs and FCM endpoints.
