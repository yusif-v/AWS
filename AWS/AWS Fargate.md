#AWS #Service 
### AWS Fargate

Serverless compute engine for containers, allowing you to run Docker containers without managing underlying EC2 instances. Works with Amazon ECS and EKS, handling resource provisioning, scaling, and infrastructure maintenance. Pay-per-use pricing based on CPU, memory, and runtime, ideal for microservices and batch jobs.

### Related Services

- Amazon ECS (Elastic Container Service): Orchestrates containers with Fargate as the launch type.
- Amazon EKS (Elastic Kubernetes Service): Manages Kubernetes workloads using Fargate.
- Amazon CloudWatch: Monitors Fargate container metrics and logs.
- AWS Application Load Balancer: Distributes traffic to Fargate tasks.
- AWS IAM: Controls access to Fargate resources.

### Related Concepts

- Serverless Containers: Eliminates server management for containerized applications.
- Microservices Architecture: Fargate supports independent, scalable container deployments.
- Task Definitions: JSON configurations defining container settings for Fargate.
- Pay-per-Use Pricing: Charges based on resource usage, aligning with cost optimization.