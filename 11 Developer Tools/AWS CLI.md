#AWS #Service #DevTools
### AWS CLI

Command-line interface for managing AWS services and resources. Enables automation, scripting, and interaction with AWS APIs from a terminal. Supports configuration profiles, credentials management, and output formats (JSON, text, table). Ideal for developers and administrators to streamline AWS operations.

### How It Works
- Installs as a Python-based tool (version 1) or a native binary (version 2) that wraps AWS REST APIs in simple commands.
- Authenticates through the default credential chain: environment variables, config files, IAM roles, or [[STS]] temporary credentials.
- Uses named profiles (default, dev, prod) to switch between accounts, roles, and regions.
- Returns output in JSON, text, or table format for scripting and readability.
- Provides auto-prompting, command completion, and JMESPath filtering via `--query`.

### Key Features
- **Profiles & Configuration**: Multiple named profiles and region settings managed with `aws configure`.
- **Credential Management**: Sources credentials from env vars, config files, IAM roles, or federated identity.
- **Output Formats**: JSON (default), text, and table for flexible parsing.
- **Scripting**: Works in bash, PowerShell, and CI/CD pipelines for repeatable operations.
- **Querying**: `--query` with JMESPath shapes output into exactly the data you need.
- **Integration**: Shares credential configuration with [[CloudShell]], SDKs, and the [[Management Console]].

### Common Use Cases
- Automating resource provisioning across [[EC2]], [[S3]], and other services.
- Deploying and managing [[CloudFormation]] stacks from the terminal.
- Querying [[CloudWatch]] metrics, logs, and alarms for monitoring.
- Auditing API activity through [[CloudTrail]] event lookups.
- Building operational runbooks and CI/CD pipeline scripts.

### Pricing & Limits
- The CLI itself is free; you pay only for the AWS services you invoke.
- Distributed via pip, Homebrew, or installers, with frequent version releases.

### Related Services
- [[IAM]]: Manages credentials and permissions for CLI access.
- [[EC2]]: Executes CLI commands to manage instances.
- [[S3]]: Performs file uploads/downloads via CLI.
- [[CloudFormation]]: Deploys and manages stacks using CLI commands.
- [[CloudWatch]]: Queries metrics and logs through CLI.
- [[CloudShell]]: Browser-based shell pre-configured with the AWS CLI.
- [[STS]]: Supplies temporary credentials for CLI sessions.
- [[Systems Manager]]: Runs CLI-managed automation and parameter tasks.
- [[IAM Identity Center]]: Provides short-term credentials for CLI sessions via SSO login.

### Related Concepts
- Automation: Scripts CLI commands for repetitive tasks or workflows.
- API Interaction: Direct access to AWS service APIs via command-line.
- Credential Management: Uses access keys or IAM roles for secure authentication.
- Cross-Platform: Runs on Windows, macOS, and Linux for broad compatibility.
- JMESPath Querying: Filters and shapes command output for precise data extraction.
