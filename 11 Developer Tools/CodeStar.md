#AWS #Service #DevTools
### CodeStar

Discontinued service (as of July 31, 2024) for creating and managing software development projects with integrated CI/CD tools. Provided unified interface for CodeCommit, CodeBuild, CodeDeploy, and CodePipeline. Existing resources remain accessible, but no new projects or console access.

### How It Works
- Bootstrapped full project templates that combined source, build, and deploy resources.
- Provisioned a project dashboard wired to CodeCommit, CodeBuild, CodePipeline, and CodeDeploy.
- Generated project scaffolding and IAM roles for a unified development workspace.
- Tracked issues and project activity through an integrated dashboard.

### Key Features
- **Project Templates**: Pre-configured stacks for common web and serverless applications.
- **Unified Dashboard**: Single console view of repos, pipelines, and issues.
- **Automated Provisioning**: Created all CI/CD resources from a project template.
- **Team Access**: Managed IAM-based access for developers on a project.
- **Integration**: Wired CodeCommit, CodeBuild, CodePipeline, and CodeDeploy together.

### Common Use Cases
- Quickly scaffolding a new project with CI/CD already configured (historic).
- Providing teams a unified view of code, builds, and deployments.
- Onboarding developers into a working DevOps setup (historic).
- Evaluating CodeStar as the entry point to AWS DevOps tooling (historic).

### Pricing & Limits
- CodeStar itself had no separate charge; underlying AWS resources were billed normally.
- As of July 31, 2024, the service is discontinued for new usage.
- Existing projects continue to run but are managed through the individual services.

### Related Services
- [[CodePipeline]]: Orchestrates CI/CD workflows, replacing CodeStar pipelines.
- [[CodeBuild]]: Compiles and tests code, integrated in CodeStar.
- [[CodeDeploy]]: Deploys applications, used by CodeStar.
- AWS CodeCommit: Hosts repositories, part of CodeStar setup.
- Amazon CodeCatalyst: Modern replacement for end-to-end DevOps.
- [[CloudWatch]]: Monitors the resources CodeStar provisions.
- [[IAM]]: Manages developer permissions in a project.

### Related Concepts
- CI/CD Pipelines: Automated build, test, deploy processes.
- Integrated Development: Unified tools for project management.
- Service Deprecation: AWS phases out services; migrate to alternatives.
- DevOps: Practices for collaborative development and operations.
- Project Bootstrapping: Automating the creation of full application stacks.
