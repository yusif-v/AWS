#AWS #Concept #Concept
### PaaS

Cloud computing model providing a managed platform for developing, deploying, and running applications without handling underlying infrastructure. AWS PaaS services like Elastic Beanstalk and App Runner automate server management, patching, and scaling, allowing developers to focus on code and application logic.

### How It Works
- The platform abstracts servers, operating systems, and middleware from developers.
- Developers deploy code or containers; the platform provisions and runs them.
- Scaling, patching, and health checks are handled automatically.
- Billing reflects the resources consumed rather than the platform itself.

### Key Features
- Managed runtime with automatic patching and scaling.
- Integrated deployment tooling and rollback support.
- Platform-level security and compliance baselines.
- Focus on application code instead of infrastructure operations.

### Common Use Cases
- Deploying web applications with [[Elastic Beanstalk]].
- Running containerized apps without cluster management via [[App Runner]].
- Using managed databases like [[RDS]] instead of self-hosted DBs.
- Building event-driven applications with [[Lambda]] and [[API Gateway]].

### Pricing & Limits
- Billed by the underlying resources (compute, storage, requests) rather than the platform.
- Less customer responsibility than IaaS under [[Shared Responsibility Model]].
- Platform constraints (supported runtimes, regions) may limit customization.

### Related Services

- [[Elastic Beanstalk]]: Deploys and manages web applications with minimal infrastructure setup.
- [[App Runner]]: Simplifies containerized application deployment and scaling.
- [[RDS]]: Manages relational databases, automating backups and patching.
- [[Lambda]]: Runs serverless code for event-driven applications.
- [[API Gateway]]: Creates and manages APIs for PaaS applications.

### Related Concepts

- Application Development: Simplifies coding by abstracting infrastructure management.
- Auto Scaling: Automatically adjusts resources based on application demand.
- [[Shared Responsibility Model]]: AWS manages platform infrastructure; customers manage application code and data.
- Serverless: Some PaaS offerings (e.g., Lambda) eliminate server management entirely.
- [[Cloud Computing Overview]]: PaaS is one of the three cloud service models.
