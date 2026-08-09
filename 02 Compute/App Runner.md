#AWS #Service #Compute
### App Runner

AWS App Runner is a fully managed service for deploying containerized web applications directly from a source repo or image. It handles scaling, load balancing, TLS, and deployment automatically, making it one of the simplest ways to run web apps and APIs on AWS.

### How It Works

- Builds and runs containers directly from source (GitHub, CodeCommit, Bitbucket) or from an existing container image stored in a registry such as Amazon ECR.
- Automatically builds, deploys, and provisions the runtime infrastructure, including the network, load balancing, and HTTPS/TLS certificates.
- A service configuration defines the port, runtime, start command, and environment variables; App Runner then maintains the running service for you.
- Scaling is automatic based on concurrent requests, with configurable minimum and maximum instance counts.
- Private networking options connect services to resources inside a VPC using VPC connectors and VPC ingress.

### Key Features

- Source-to-service deployment: pushes trigger automatic builds and new versions with zero manual configuration.
- Automatic TLS certificate provisioning and HTTPS termination; custom domains can be attached easily.
- Built-in traffic management including instance health checks, rolling deployments, and safe version promotion.
- Automatic scaling to zero or to a configured minimum, controlled by concurrency targets.
- Supports both web services and long-running background workers via a separate service type.
- Integrated observability through CloudWatch metrics, logs, and trace propagation.

### Common Use Cases

- Quick deployment of web applications and REST APIs without managing servers or clusters.
- Internal tools and dashboards that need fast, low-friction hosting.
- Containerized microservices where the extra control of ECS or EKS is not required.
- Graduating from a managed platform experience while staying inside the AWS ecosystem with IAM and CloudWatch.

### Pricing & Limits

- Billed for provisioned vCPU and memory per hour, regardless of actual utilization.
- No charge for the service itself; costs are driven by the running capacity of each service.
- Default quotas limit the number of App Runner services per region per account, with larger limits available on request.

### Related Services

- [[ECS]]: More control for container orchestration.
- [[Fargate]]: Serverless containers with more configuration.
- [[ELB]]: Load balancing for App Runner services.
- [[Lambda]]: Event-driven alternative for short-lived workloads.
- [[CloudWatch]]: Metrics and logs for App Runner services.

### Related Concepts

- Containerized Apps: Deploy from source or image.
- Auto Scaling: Managed, no capacity planning.
- Serverless: No infrastructure to manage.
- [[PaaS]]: Fully managed platform abstracting the runtime.
