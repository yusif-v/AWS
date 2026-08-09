#AWS #Service #Compute
### Elastic Beanstalk

Platform-as-a-Service (PaaS) for deploying and managing web applications and services without handling underlying infrastructure. Supports languages like Java, .NET, Node.js, Python, Ruby, Go, and Docker. Automates load balancing, auto-scaling, monitoring, and updates, allowing focus on code.

### How It Works

- You upload your application code (or a Docker image) and Beanstalk provisions the environment: EC2 instances, a load balancer, auto scaling, and monitoring.
- An environment is either a web server tier (fronted by a load balancer) or a worker tier (driven by an SQS queue).
- Beanstalk runs health checks and redeploys or replaces instances to maintain application health.
- Configuration is declarative via the EB CLI, console, and environment configuration files (YAML/JSON).
- Versioned application bundles make rollback and promotion between environments straightforward.

### Key Features

- Supports Java, .NET, Node.js, Python, Ruby, Go, PHP, and Docker containers.
- Managed environment updates including rolling, immutable, and blue/green deployment strategies.
- Built-in health monitoring and CloudWatch integration for metrics and logs.
- Environment cloning for staging and testing; saved configurations for reuse.
- Platform-managed updates keep runtimes and operating systems patched.
- Easy path from a fully managed PaaS to EC2, ECS, or Fargate as needs grow.

### Common Use Cases

- Quickly launching web applications and APIs without infrastructure design.
- Internal line-of-business apps and prototypes with low operational overhead.
- Worker tier applications that process jobs from an SQS queue.
- Gradual migration of a classic application to the cloud with minimal code changes.

### Pricing & Limits

- Elastic Beanstalk is free; you pay for the underlying EC2 instances, load balancers, storage, and data transfer.
- Worker tiers add SQS queue usage costs.
- Default limits cap environments per account and can be raised on request.

### Related Services

- [[EC2]]: Provides compute instances for Beanstalk environments.
- [[ELB]] (Elastic Load Balancing): Distributes traffic across application instances.
- [[Auto Scaling]]: Adjusts capacity based on demand.
- [[CloudWatch]]: Monitors application performance and logs.
- [[RDS]]: Integrates for relational database support.
- [[SQS]]: Drives worker tier processing.

### Related Concepts

- [[IaC]]: Deploys applications via configuration files.
- Environment Management: Manages web server and worker tiers for apps and tasks.
- Deployment Strategies: Supports rolling, immutable, and blue/green deployments.
- [[PaaS]]: Abstracts infrastructure for developer productivity.
- [[CloudFormation]]: Underpins Beanstalk environment resources.
