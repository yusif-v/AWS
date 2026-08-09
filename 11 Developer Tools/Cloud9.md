#AWS #Service #DevTools
### Cloud9

AWS Cloud9 is a cloud-based integrated development environment (IDE). It runs in the browser with terminal, code editor, and debugging tools, pairs with EC2 environments, and is often used for serverless development with Lambda.

### How It Works
- Runs a browser-based editor backed by an EC2 instance (or an existing server) that hosts the filesystem and runtime.
- Each environment gets a dedicated EC2 instance with a persistent file system and pre-configured runtimes.
- Embeds a terminal, debugger, and Git support in the same browser tab.
- Stores environment state so work persists between browser sessions.
- Uses IAM roles on the backing instance so code can call AWS APIs without hardcoded credentials.

### Key Features
- **Cloud IDE**: Full editor, terminal, and debugger in the browser with no local install.
- **EC2 Environments**: Automatically provisions the compute backing the workspace.
- **Lambda Support**: Run and debug serverless functions locally and deploy to AWS.
- **Collaboration**: Share environments for pair programming in real time.
- **Git Integration**: Clone, commit, and push to [[CodeCommit]] from the IDE.
- **Preview & Share**: Preview web apps and share links to running environments.

### Common Use Cases
- Developing and testing serverless applications before deploying to [[Lambda]].
- Editing code from any device with only a browser.
- Onboarding developers without local environment setup.
- Pair programming and mentoring through shared workspaces.
- Running one-off scripts against AWS resources from a pre-configured shell.

### Pricing & Limits
- Charges apply for the underlying EC2 instance, EBS storage, and data transfer.
- Environment sleep and shutdown help control cost when not in use.
- Stop environments when idle to avoid ongoing compute charges.

### Related Services
- [[EC2]]: Backs Cloud9 environments.
- [[Lambda]]: Serverless development workflow.
- [[CodeCommit]]: Git repositories from the IDE.
- [[CloudFormation]]: Provision environments as infrastructure as code.
- [[IAM]]: Grants environment instances permission to call AWS services.
- [[S3]]: Stores environment snapshots and build artifacts.

### Related Concepts
- Cloud IDE: Browser-based development.
- Environment: Provisioned workspace.
- Collaboration: Real-time pair programming.
- Serverless Development: Local authoring and deployment of Lambda functions.
- DevOps: Streamlined developer-to-production workflows.
