#AWS #Service #DevTools
### CodeDeploy

Fully managed deployment service that automates application deployments to a variety of compute services, including EC2 instances, on-premises servers, Lambda functions, and ECS. Supports in-place and blue/green deployment strategies, automated rollbacks, and deployment configuration controls for reliable releases.

### How It Works
- Bundles application revisions and a deployment configuration (traffic routing, failure thresholds) for each release.
- Uses the CodeDeploy agent on EC2 and on-premises hosts to fetch and apply revisions from S3 or GitHub.
- For Lambda and ECS, orchestrates traffic shifting between the current and replacement versions.
- Uses an AppSpec file to define lifecycle events such as BeforeInstall, AfterInstall, and ApplicationStart.
- Tracks deployment progress and stops or rolls back on failure, reporting status to [[CloudWatch]].

### Key Features
- **Deployment Strategies**: In-place, blue/green, canary, and linear traffic shifting.
- **AppSpec File**: Declares lifecycle hooks and validation steps for each deployment.
- **Automated Rollbacks**: Rolls back to the last known-good revision when health checks fail.
- **Deployment Groups**: Manages fleets of instances or containers per environment.
- **Health Monitoring**: Validates target health before continuing or aborting a deployment.
- **Integration**: Works with [[CodePipeline]], [[CodeBuild]], and GitHub Actions.

### Common Use Cases
- Automating web and application server deployments to EC2 fleets behind an [[ELB]].
- Releasing serverless functions to [[Lambda]] with gradual traffic shifts.
- Deploying containerized apps on [[ECS]] and [[Fargate]] with blue/green updates.
- Rolling back risky releases automatically when health checks fail.
- Deploying to on-premises servers via the on-premises agent.

### Pricing & Limits
- No charge for deployments to EC2, on-premises, or Lambda (free tier applies).
- ECS deployments and automated rollback are billed per deployment.
- Concurrent deployment limits apply per account; raise them via a support request.

### Related Services
- [[CodePipeline]]: Orchestrates deployments in CI/CD workflows.
- [[CodeBuild]]: Produces the artifacts CodeDeploy ships.
- [[CodeCommit]]: Stores source code used for revisions.
- [[S3]]: Stores application revisions and deployment artifacts.
- [[Lambda]]: Targets serverless deployments.
- [[ECS]] / [[Fargate]]: Container targets for blue/green deployments.
- [[Auto Scaling]]: Manages the EC2 fleet that receives in-place deployments.
- [[ELB]]: Routes traffic during blue/green switchover.
- [[CloudWatch]]: Monitors deployment health and metrics.
- [[IAM]]: Controls who can start and manage deployments.

### Related Concepts
- Continuous Delivery: Automated, reliable releases to production.
- Blue/Green Deployment: Switching traffic between two parallel environments.
- Lifecycle Hooks: Scripted validation and configuration steps during deployment.
- Rollback Strategy: Restoring the last known-good revision on failure.
