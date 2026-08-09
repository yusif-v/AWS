#AWS #Service #Compute
### Fargate

Serverless compute engine for containers, allowing you to run Docker containers without managing underlying EC2 instances. Works with Amazon ECS and EKS, handling resource provisioning, scaling, and infrastructure maintenance. Pay-per-use pricing based on CPU, memory, and runtime, ideal for microservices and batch jobs.

### How It Works

- Fargate runs each task or pod in an isolated, purpose-built runtime without you provisioning or managing EC2 instances.
- You define the task definition (containers, CPU, memory, networking) and Fargate provisions the resources on demand.
- For ECS, launch tasks into a Fargate cluster; for EKS, use Fargate profiles to schedule selected namespaces or workloads onto Fargate.
- Fargate handles patching, scaling, and infrastructure maintenance, abstracting the host entirely.
- Networking uses an elastic network interface in your VPC, giving each task an IP address and security group.

### Key Features

- No server or cluster management: no patching, node pools, or capacity planning.
- Pay only for the vCPU and memory your containers actually use, per second.
- Integration with ECS and EKS for orchestration; works with ELB and CloudWatch.
- Per-task isolation for security and predictable performance.
- Scales from zero to thousands of tasks automatically.
- Task-level IAM roles and Secrets Manager integration for credentials.

### Common Use Cases

- Microservices and web APIs with variable traffic and little ops overhead.
- One-off and scheduled batch jobs that need isolated, short-lived compute.
- EKS workloads on Fargate profiles for serverless pods.
- Migrating containerized apps from managed EC2 fleets to reduce maintenance.

### Pricing & Limits

- Billed per second of vCPU and memory consumed, with no minimum or upfront commitment.
- Additional charges apply for storage (e.g., EFS for persistent data) and data transfer.
- Default quotas limit running tasks per region and can be raised on request.

### Related Services

- [[ECS]] (Elastic Container Service): Orchestrates containers with Fargate as the launch type.
- [[EKS]] (Elastic Kubernetes Service): Manages Kubernetes workloads using Fargate.
- [[CloudWatch]]: Monitors Fargate container metrics and logs.
- [[ELB]] (Application Load Balancer): Distributes traffic to Fargate tasks.
- [[IAM]]: Controls access to Fargate resources.
- [[EC2 Storage]]: EFS provides persistent storage for Fargate tasks.

### Related Concepts

- Serverless Containers: Eliminates server management for containerized applications.
- Microservices Architecture: Fargate supports independent, scalable container deployments.
- Task Definitions: JSON configurations defining container settings for Fargate.
- Pay-per-Use Pricing: Charges based on resource usage, aligning with cost optimization.
- [[Shared Responsibility Model]]: AWS secures the runtime; you secure the containers.
