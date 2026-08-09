#AWS #Service #DevTools
### CodeCommit

Fully managed source control service hosting secure, private Git repositories. Supports branching, pull requests, commits, and collaboration. Encrypts data at rest/transit, scales automatically, and integrates with AWS for CI/CD.

### How It Works
- Hosts Git repositories in the AWS cloud with no servers to manage.
- Authenticates over HTTPS or SSH using IAM-based credentials or Git credential helper.
- Encrypts repository data at rest with [[KMS]] and in transit with TLS.
- Replicates repositories across multiple Availability Zones for durability.
- Emits events on push, commit, and branch activity for automation.

### Key Features
- **Private Repositories**: Secure, scalable Git hosting without GitLab/GitHub management.
- **Pull Requests**: Review and comment on code before merging branches.
- **Fine-Grained Access**: IAM policies and repository-level permissions.
- **Notifications**: Trigger SNS or Lambda on commit and push events.
- **Integration**: Works with [[CodeBuild]], [[CodePipeline]], and the AWS CLI.
- **High Durability**: Data replicated across Availability Zones with no size limit.

### Common Use Cases
- Hosting internal application source code with encryption and access control.
- Implementing branch-based workflows (GitFlow, trunk-based) for teams.
- Acting as the source stage for CI/CD pipelines.
- Storing configuration, IaC templates, and infrastructure code.
- Complying with regulations requiring encrypted, regionally isolated Git hosting.

### Pricing & Limits
- No upfront costs; billed per active user per month (five free active users).
- Free tier includes a limited number of active users and storage.
- Large repositories and high storage usage may incur additional charges.

### Related Services
- [[CodePipeline]]: Sources code from CodeCommit for CI/CD.
- [[CodeBuild]]: Builds and tests CodeCommit repositories.
- [[CodeDeploy]]: Deploys applications from CodeCommit.
- AWS IAM: Controls repository access and permissions.
- [[CloudWatch]]: Monitors CodeCommit events and metrics.
- [[KMS]]: Encrypts repository data at rest.
- [[SNS]]: Notifies on repository events.

### Related Concepts
- Version Control: Tracks code changes using Git protocols.
- CI/CD Integration: Automates build/test/deploy workflows.
- Secure Collaboration: Encrypted repos with fine-grained access.
- Branching Models: Supports workflows like GitFlow for development.
- Pull Request Workflow: Code review before merging.
