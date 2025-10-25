#AWS #Service 
### AWS Lambda

Serverless compute service that runs code in response to events without managing servers. Supports languages like Python, Node.js, Java, and Go. Automatically scales, charges per execution time, and integrates with AWS services for event-driven applications like automation, data processing, and APIs.

### Related Services

- [[Amazon API Gateway]]: Triggers Lambda for HTTP-based APIs.
- [[Amazon S3]]: Invokes Lambda on object events (e.g., uploads).
- [[Amazon DynamoDB]]: Processes table updates via streams.
- [[Amazon CloudWatch]]: Monitors Lambda metrics, logs, and triggers scheduled events.
- AWS SNS/SQS: Sends messages to Lambda for event handling.

### Related Concepts

- Serverless Computing: Eliminates server management with pay-per-use pricing.
- Event-Driven Architecture: Executes code in response to triggers like HTTP requests or data changes.
- Function as a Service (FaaS): Runs stateless, short-lived functions for specific tasks.
- Cold Start: Initial latency for function initialization affecting performance.