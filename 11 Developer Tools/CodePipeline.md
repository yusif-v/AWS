#AWS #Service #DevTools
### CodePipeline

Fully managed CI/CD service for automating build, test, and deploy pipelines for applications and infrastructure. Supports source integration, parallel/serial stages, approvals, and artifact management for reliable releases.

### How It Works
- Models a pipeline as an ordered set of stages (source, build, test, deploy).
- Pulls source from [[CodeCommit]], S3, GitHub, or Bitbucket in the source stage.
- Runs actions such as [[CodeBuild]] builds and [[CodeDeploy]] deployments at each stage.
- Passes artifacts between stages through encrypted S3 buckets.
- Watches for source changes and starts the pipeline automatically or on a schedule.

### Key Features
- **Stage-Based Model**: Serial or parallel stages with manual approval gates.
- **Artifact Management**: Passes build outputs between stages via [[S3]].
- **Approval Actions**: Pause pipelines for manual review before production deployment.
- **Automated Triggers**: Start pipelines on source pushes, schedules, or events.
- **CloudFormation Actions**: Deploy infrastructure as code directly in the pipeline.
- **Integration**: Native actions for CodeBuild, CodeDeploy, ECS, and Lambda.

### Common Use Cases
- Automating end-to-end software delivery from commit to production.
- Enforcing approval gates before production deployments.
- Deploying infrastructure with [[CloudFormation]] alongside application code.
- Running test suites and quality gates in a repeatable sequence.
- Coordinating multi-account or multi-environment release processes.

### Pricing & Limits
- Billed per active pipeline per month after the first free pipeline.
- Charges are per pipeline, with no per-action or per-build fees.
- Free tier includes one active pipeline per month.

### Related Services
- [[CodeBuild]]: Builds and tests code in pipelines.
- [[CodeDeploy]]: Deploys applications from pipelines.
- [[CodeCommit]]: Provides source repositories for pipelines.
- [[S3]]: Stores pipeline artifacts.
- [[Lambda]]: Executes custom actions in pipelines.
- [[CloudFormation]]: Deploys infrastructure as a pipeline action.
- [[CloudWatch]]: Monitors pipeline execution and state changes.
- [[ECS]]: Target for container-based pipeline deployments.

### Related Concepts
- Continuous Integration/Continuous Delivery (CI/CD): Automates software delivery processes.
- Pipeline Stages: Source, build, test, deploy phases.
- Artifacts: Outputs passed between pipeline stages.
- Automation: Reduces manual intervention for releases.
- Approval Gates: Manual checkpoints before high-risk deployments.
