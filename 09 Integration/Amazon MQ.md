#AWS #Service #Integration
### Amazon MQ

Amazon MQ is a managed message broker for Apache ActiveMQ and RabbitMQ. It provides JMS and AMQP protocols for applications using open-source brokers, offering a migration path from self-managed brokers without rewriting applications.

### How It Works
- Runs managed broker instances for Apache ActiveMQ and RabbitMQ, handling provisioning, patching, and upgrades for you.
- ActiveMQ brokers support JMS, OpenWire, AMQP 1.0, MQTT, STOMP, and WebSocket; RabbitMQ supports AMQP 0-9-1 and MQTT.
- Choose single-instance brokers for development or active/standby deployment for high availability across Availability Zones.
- Storage is backed by EBS volumes, and brokers are deployed inside your VPC so network access is controlled with security groups.
- Standard broker concepts such as queues, topics, and dead-letter queues behave like their open-source counterparts.

### Key Features
- JMS 1.1 and 2.0 API compatibility, so existing JMS applications can move with minimal code change.
- Engine version selection and automatic minor-version upgrades within scheduled maintenance windows.
- Network isolation within a VPC plus IAM-based and broker-policy-based access control.
- CloudWatch integration for broker and queue/topic metrics and CloudTrail logging of API activity.
- Supports ActiveMQ broker persistence and RabbitMQ clusters with data replication.

### Common Use Cases
- Lift-and-shift migration of on-premises ActiveMQ or RabbitMQ infrastructure to AWS without rewriting applications.
- Connecting legacy enterprise systems that already speak JMS or AMQP to cloud workloads.
- Transactional messaging where queues and topics with acknowledgements are required rather than pull-based queuing.
- Prototyping or running hybrid estates that still need standards-compliant open-source brokers.

### Pricing & Limits
- Billed per broker instance based on instance type and storage; no free tier.
- Active/standby brokers cost more because two instances run for high availability.
- Limits are based on broker instance size and message size, similar to running the open-source engines yourself.
- Data transfer costs apply for traffic crossing the internet or between regions.

### Related Services

- [[SQS]]: Native AWS queue alternative.
- [[SNS]]: Pub/sub alternative.
- [[Kinesis]]: Streaming alternative for real-time data ingestion.
- [[EventBridge]]: Event bus for event-driven integration without brokers.
- [[Step Functions]]: Orchestration of messaging workflows.
- [[Lambda]]: Serverless processing of messages from queues and topics.

### Related Concepts

- JMS/AMQP: Standard messaging protocols.
- Broker: Server hosting queues/topics.
- Lift-and-Shift: Migrate existing brokers.
- Publish-Subscribe Messaging: Topics broadcast to multiple consumers.
- VPC: Network isolation for broker access.
