#Amazon #Service 
### Amazon SQS

Fully managed message queuing service for decoupling and scaling microservices, distributed systems, and serverless applications. Supports standard queues (high throughput, at-least-once delivery) and FIFO queues (exactly-once processing, order preserved). Features visibility timeouts, dead-letter queues, long polling, and encryption.

### Related Services

- [[Amazon SNS]]: Publishes messages to SQS for fan-out scenarios.
- [[AWS Lambda]]: Triggers functions from SQS messages.
- [[Amazon EC2]]: Sends/receives messages for distributed apps.
- [[Amazon CloudWatch]]: Monitors queue metrics and alarms.
- AWS IAM: Controls access to queues.

### Related Concepts

- Message Queuing: Asynchronous communication between components.
- Decoupling: Reduces dependencies for fault tolerance.
- FIFO vs. Standard Queues: Ordered/exactly-once vs. high-throughput/at-least-once.
- Dead-Letter Queues: Handles failed message processing.