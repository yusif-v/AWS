#AWS #Service #Compute
### Lambda

Serverless compute service that runs code in response to events without managing servers. Supports languages like Python, Node.js, Java, and Go. Automatically scales, charges per execution time, and integrates with AWS services for event-driven applications like automation, data processing, and APIs.

### How It Works

- You package code (or a container image) into a function with an entry point, runtime, memory setting, and timeout.
- The function is invoked by an event source: HTTP via API Gateway, object changes in S3, stream records from DynamoDB or Kinesis, messages from SQS/SNS, or schedules from EventBridge.
- Lambda provisions the execution environment, runs the code, and tears the environment down, scaling in parallel to the rate of events.
- Execution is stateless: durable data lives in services like S3 or DynamoDB, and each invocation is independent.
- Cold starts occur when a new environment initializes; provisioned concurrency keeps environments warm for low-latency workloads.

### Key Features

- Broad runtime support: Python, Node.js, Java, Go, Ruby, .NET, and custom runtimes via provided Amazon Linux bases or container images.
- Automatic scaling from a single invocation to thousands of concurrent executions.
- Pay only for requests and compute time, billed in millisecond increments.
- Integration with many AWS services as event sources and destinations.
- Function versions, aliases, and weighted traffic shifting for safe deployments.
- Environment variables, secrets from Secrets Manager, and ephemeral storage for function-local state.

### Common Use Cases

- Web and mobile backends behind API Gateway.
- Automated image processing, video transcoding, and data transformation on object upload.
- Real-time stream processing from DynamoDB Streams, Kinesis, and SQS.
- Infrastructure automation, security remediation, and scheduled jobs via EventBridge.
- Glue and ETL glue code in data pipelines.

### Pricing & Limits

- Free tier includes 1 million requests and 400,000 GB-seconds of compute per month.
- Billed per request plus duration in GB-seconds, with a timeout of up to 15 minutes.
- Memory configurable up to 10 GB, with proportional vCPU allocation.
- Default concurrency limits apply per account and region and can be raised on request.
- Provisioned concurrency incurs an additional hourly charge for keeping environments warm.

### Related Services

- [[API Gateway]]: Triggers Lambda for HTTP-based APIs.
- [[S3]]: Invokes Lambda on object events (e.g., uploads).
- [[DynamoDB]]: Processes table updates via streams.
- [[CloudWatch]]: Monitors Lambda metrics, logs, and triggers scheduled events.
- [[SNS]]/[[SQS]]: Sends messages to Lambda for event handling.
- [[EventBridge]]: Event bus and schedule-based invocations.

### Related Concepts

- Serverless Computing: Eliminates server management with pay-per-use pricing.
- Event-Driven Architecture: Executes code in response to triggers like HTTP requests or data changes.
- Function as a Service (FaaS): Runs stateless, short-lived functions for specific tasks.
- Cold Start: Initial latency for function initialization affecting performance.
- [[IAM Roles]]: The execution role granting function permissions.

### Runtime & Limits

Lambda supports multiple runtimes and charges per invocation and compute time. Event sources include S3, DynamoDB Streams, Kinesis, SQS, and API Gateway. Functions can run up to 15 minutes, use up to 10 GB of memory, and scale to account concurrency limits. See the Related Services and Related Concepts sections below.
