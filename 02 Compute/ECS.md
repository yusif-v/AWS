#AWS #Service #Compute
### ECS

Amazon Elastic Container Service (ECS) is a fully managed container orchestration service for running Docker containers. It supports Fargate (serverless) and EC2 launch types, integrates with load balancers and Service Discovery, and uses task definitions to describe containers.

### How It Works

- A task definition (JSON) describes the containers, images, CPU/memory, networking, and volumes for an application.
- Tasks are placed on a cluster — either Fargate (serverless) or EC2 (your managed instances) — and launched as one or more containers.
- A service keeps a desired number of tasks running, performs rolling updates, and attaches a load balancer target group.
- The ECS scheduler balances tasks across instances based on available resources and constraints.
- Capacity providers manage the scaling of the underlying EC2 or Fargate capacity automatically.

### Key Features

- Fargate and EC2 launch types with capacity providers that can mix both.
- Service auto scaling driven by CloudWatch metrics and target tracking.
- Integration with ELB/ALB, Service Discovery, and CloudWatch for logs and metrics.
- Secrets and parameters injected from Secrets Manager and Systems Manager Parameter Store.
- Amazon ECR for storing and pulling container images; support for Docker and OCI images.
- Task placement strategies, anti-affinity rules, and startup and shutdown grace periods.

### Common Use Cases

- Running and scaling microservices without managing a control plane.
- Containerized batch or one-off jobs with ECS RunTask.
- Web applications composed of many containers fronted by a load balancer.
- Migrating Docker Compose or standalone containers to a managed orchestrator.

### Pricing & Limits

- ECS is free to use; you pay for the underlying EC2 instances or Fargate resources.
- Fargate pricing is per vCPU and per GB of memory consumed; EC2 pricing follows normal EC2 billing.
- Default quotas limit clusters, services, and tasks per region and can be increased on request.

### Related Services

- [[Fargate]]: Serverless compute for ECS tasks.
- [[EKS]]: Kubernetes alternative to ECS.
- [[ELB]]: Distributes traffic to container tasks.
- [[CloudWatch]]: Metrics, logs, and alarms for clusters and services.
- [[EC2]]: Hosts tasks under the EC2 launch type.
- [[Secrets Manager]]: Injects secrets into container environments.

### Related Concepts

- Task Definition: Blueprint for a container group.
- Container: Packaged application and dependencies.
- Service: Maintains desired task count.
- [[IaC]]: Defining clusters and services with CloudFormation or CDK.
- [[IAM Roles]]: Task-level permissions via task IAM roles.
