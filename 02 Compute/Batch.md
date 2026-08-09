#AWS #Service #Compute
### Batch

AWS Batch is a fully managed batch computing service for running large-scale parallel jobs. It dynamically provisions EC2 or Fargate resources based on job queue demand, supports containerized and native jobs, and is suited for rendering, analytics, and scientific workloads.

### How It Works

- Jobs are defined by job definitions (the runtime, image, command, memory, and CPU requirements) and then submitted to a job queue.
- A compute environment provides the capacity — managed EC2, Spot, or Fargate — that the service provisions and scales based on queue depth.
- A scheduler places queued jobs onto available compute resources, honoring priorities and dependencies between jobs.
- Array jobs run the same task many times across parallel compute, and multi-node jobs coordinate distributed workloads.
- Completed and failed jobs are tracked, with retry policies and job dependencies controlling execution order.

### Key Features

- Fully managed compute environments that provision and tear down EC2 or Fargate capacity automatically.
- Priority-based queueing with job dependencies and sequencing for multi-step pipelines.
- Array jobs and multi-node parallel jobs for embarrassingly parallel and tightly coupled workloads.
- Integration with S3 for input and output, EventBridge for job notifications, and CloudWatch for logs and metrics.
- Cost optimized by default using Spot capacity where interruption is acceptable.
- No cluster management: Batch handles scheduling, scaling, and fault tolerance.

### Common Use Cases

- Media rendering and video transcoding across large fleets.
- Genomics, drug discovery, and simulation workloads with massive parallelism.
- Extract, transform, and load (ETL) pipelines and data transformation jobs.
- Machine learning data preparation and post-processing jobs that run on a schedule.

### Pricing & Limits

- AWS Batch itself is free; you pay only for the EC2 instances, Fargate resources, and storage consumed by your jobs.
- Spot capacity offers steep discounts for interruptible batch work; managed compute environments track cost across instance types.
- Default quotas limit compute environments, job queues, and concurrent jobs per region and can be raised by request.

### Related Services

- [[EC2]]: Backs batch compute environments.
- [[Fargate]]: Serverless option for batch jobs.
- [[Step Functions]]: Orchestrates multi-step batch pipelines.
- [[S3]]: Stores job input and output data.
- [[EventBridge]]: Schedules and reacts to batch job lifecycle events.
- [[CloudWatch]]: Logs and monitors job execution.

### Related Concepts

- Job Queue: Pending jobs awaiting compute.
- Compute Environment: Managed capacity for jobs.
- Parallelism: Scales jobs across resources.
- [[EC2 Pricing Models]]: On-Demand versus Spot for interruptible batch work.
