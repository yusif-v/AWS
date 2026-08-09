#AWS #Service #Integration
### Step Functions

AWS Step Functions orchestrates workflows by coordinating Lambdas, ECS tasks, and other services as state machines. It handles retries, branching, parallel execution, and human approval steps, making it the standard way to build reliable multi-step serverless processes.

### How It Works
- Workflows are defined as state machines using the Amazon States Language (JSON).
- Common states include Task (run a unit of work), Choice (branching), Parallel, Map, Wait, Pass, Succeed, and Fail.
- Tasks invoke AWS services directly via SDK integrations, Lambda functions, or Activity workers.
- The service tracks state between steps, handles retries and errors, and logs execution history.
- Workflows run as Standard (long-running, exactly-once) or Express (high-volume, near real-time).

### Key Features
- Built-in retry policies with exponential backoff and error catching per state.
- Parallel and Map states to fan out work, including Distributed Map for very large workloads.
- Human-in-the-loop approvals using Callback tokens (TaskToken) that pause a workflow until confirmed.
- Activity tasks for long-running external workers that poll for work.
- Workflow Studio visual designer and integration with AWS SDK services and Lambda.
- Execution history, CloudWatch logging, and X-Ray tracing for observability.
- Integration with over 200 AWS services through optimized connectors.

### Common Use Cases
- Order processing, payment, and fulfillment pipelines with branching and approval steps.
- ETL and data-processing pipelines that move and transform data between services.
- Microservice orchestration that replaces brittle custom choreography.
- Media processing pipelines, document workflows, and report generation.
- Long-running business processes that require human review or timed waits.

### Pricing & Limits
- Standard workflows are billed per state transition, with a monthly free tier of 4,000 transitions.
- Express workflows are billed by duration and number of executions, ideal for high-volume short jobs.
- No infrastructure to manage; you pay only for executions, not idle time.
- Standard workflows support up to one year of execution time for long-running processes.

### Related Services

- [[Lambda]]: Common task type in workflows.
- [[SQS]]: Message queues for decoupling.
- [[EventBridge]]: Schedules workflow triggers.
- [[ECS]] / [[Fargate]]: Runs container tasks as workflow steps.
- [[S3]]: Stores inputs, outputs, and intermediate artifacts.
- [[API Gateway]]: Exposes state machines as REST endpoints.
- [[DynamoDB]]: Persists workflow state and results.
- [[X-Ray]]: Traces workflow executions end to end.
- [[CloudWatch]]: Monitors metrics and execution history.
- [[SNS]]: Notifications from workflow outcomes.
- [[Kinesis]]: Streaming input that triggers workflows.

### Related Concepts

- State Machine: Defined workflow of states.
- Standard vs Express: Long-running vs high-volume executions.
- Retries & Error Handling: Built-in resilience.
- Amazon States Language: JSON language for defining workflows.
- Orchestration vs Choreography: Central coordination versus distributed event passing.
- Human-in-the-Loop: Manual approvals inside automated workflows.
