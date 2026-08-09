#AWS #Service #Management
### CloudShell

AWS CloudShell is a browser-based shell with the AWS CLI and other tools pre-installed. It is authenticated with your console session, includes 1 GB of persistent storage, and lets you manage AWS resources without local setup. It is available for free to all customers in supported regions from within the Management Console.

### How It Works

- CloudShell runs as a terminal in the browser, launched from a button in the Management Console.
- It automatically inherits the IAM credentials and permissions of the currently signed-in user — no separate access keys are needed.
- Each region provides a dedicated shell with a persistent home directory for files, scripts, and shell history.
- Shells are isolated per region and per user; session state persists in the storage but the running terminal ends when you close it or after idle disconnection.
- Tools such as the AWS CLI, git, python, node, and common utilities are pre-installed and kept updated by AWS.

### Key Features

- **Zero Setup**: Nothing to install; works from any browser on any device.
- **Pre-Authenticated**: Uses your existing console identity, so no credential management.
- **Persistent Storage**: 1 GB of per-region storage for scripts and configuration.
- **File Upload/Download**: Transfer files between your local machine and the shell.
- **AWS CLI + SDKs**: Ready-to-use command-line tooling for automating tasks.
- **Free to Use**: No charge for the shell itself; you only pay for AWS resources you create.

### Common Use Cases

- Running quick AWS CLI commands to inspect or modify resources from any machine.
- Testing CLI commands and scripts before automating them elsewhere.
- Managing resources during incident response without installing tools locally.
- Keeping a small set of reusable scripts in the persistent storage across sessions.

### Pricing & Limits

- CloudShell is free; standard AWS usage charges apply to resources you create from it.
- Storage is capped at 1 GB per region per user.
- Sessions disconnect after a period of inactivity, and there are limits on concurrent sessions per user.

### Related Services

- [[AWS CLI]]: The command-line tool available in CloudShell.
- [[Management Console]]: Launches CloudShell.
- [[IAM]]: Uses your console identity.
- [[Cloud9]]: Browser-based IDE alternative with a terminal and code editor.
- [[IAM Policies]]: Scope the permissions the shell inherits.
- [[CloudTrail]]: Logs AWS API calls made from the shell.

### Related Concepts

- Browser Shell: No local install.
- Pre-Authenticated: Uses console credentials.
- Persistent Storage: 1 GB home directory.
- Region-Scoped Shells: A separate shell and storage per region.
- Idle Disconnect: Sessions end automatically after inactivity.
