#Amazon #Service 
### Amazon SNS

Fully managed messaging service for sending notifications and messages to a large number of subscribers or endpoints. Uses a publish-subscribe (pub/sub) model, supporting topics for broadcasting messages via email, SMS, HTTP, mobile push, SQS, or Lambda. Scales automatically and ensures reliable, low-latency delivery.

### Related Services

- [[AWS Lambda]]: Processes SNS messages for event-driven workflows.
- [[Amazon SQS]]: Receives SNS messages for queue-based processing.
- [[Amazon CloudWatch]]: Monitors SNS metrics and delivery status.
- [[AWS IAM]]: Controls access to SNS topics and subscriptions.
- [[Amazon S3]]: Triggers SNS notifications for bucket events.

### Related Concepts

- Publish-Subscribe Messaging: Publishers send messages to topics; subscribers receive them.
- Fan-Out Architecture: Distributes messages to multiple endpoints simultaneously.
- Message Filtering: Subscribers receive only relevant messages based on filters.
- Scalability: Handles high message volumes with automatic scaling.