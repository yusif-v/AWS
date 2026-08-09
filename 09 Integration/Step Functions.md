#AWS #Service #Integration
### Step Functions

AWS Step Functions orchestrates workflows by coordinating Lambdas, ECS tasks, and other services as state machines. It handles retries, branching, parallel execution, and human approval steps, making it the standard way to build reliable multi-step serverless processes.

### Related Services

- [[Lambda]]: Common task type in workflows.
- [[SQS]]: Message queues for decoupling.
- [[EventBridge]]: Schedules workflow triggers.

### Related Concepts

- State Machine: Defined workflow of states.
- Standard vs Express: Long-running vs high-volume executions.
- Retries & Error Handling: Built-in resilience.
