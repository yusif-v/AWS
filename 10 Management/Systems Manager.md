#AWS #Service #Management
### Systems Manager

AWS Systems Manager gives you operational control across EC2 and on-premises resources. It includes Parameter Store (secure key-value storage), Run Command (remote commands), Patch Manager, Session Manager, and State Manager for unified configuration and automation. It provides a single pane of glass for operating large fleets without opening inbound ports.

### How It Works

- The **SSM Agent** runs on each managed instance (EC2 or on-premises via hybrid activations) and communicates with the Systems Manager service using a required IAM role.
- Fleet Manager, Run Command, and Session Manager send operations to instances through the agent using the AWS console or CLI — no SSH/RDP inbound ports required.
- Parameter Store stores configuration values and secrets as standard or advanced parameters, with SecureString values encrypted by KMS.
- Patch Manager defines baselines and schedules; State Manager enforces desired configurations; Maintenance Windows run tasks on a schedule.
- OpsCenter aggregates operational issues, while Automation and Change Manager run and approve runbook-style workflows.

### Key Features

- **Parameter Store**: Free tier of secure key-value storage for configs and secrets, with versions and hierarchies.
- **Run Command**: Execute shell commands or PowerShell scripts across many instances at once.
- **Session Manager**: Interactive shell and port-forwarding access to instances with no inbound ports and full audit logging.
- **Patch Manager**: Automated, scheduled OS patching with compliance reporting.
- **State Manager**: Enforce and maintain consistent instance configurations.
- **Maintenance Windows & Automation**: Schedule operational tasks and run multi-step runbooks.
- **Inventory & Compliance**: Collect and report software inventory and patch/config compliance.
- **OpsCenter**: Central hub for operational work items and related resources.

### Common Use Cases

- Rolling out a command or script to hundreds of instances simultaneously.
- Providing secure, audited shell access to instances for engineers without public SSH.
- Automating patching across environments during maintenance windows.
- Storing application configuration and secrets centrally and retrieving them at runtime.
- Enforcing consistent agent configuration, logging, and inventory across a fleet.

### Pricing & Limits

- The base service and Parameter Store standard tier are free; charges apply for advanced parameters, certain automation steps, and added capabilities.
- The SSM Agent must be installed and have an IAM role with permission to call Systems Manager APIs.
- On-premises servers are supported through hybrid activations and are billed by usage.

### Related Services

- [[EC2]]: Primary managed resource.
- [[CloudWatch]]: Monitoring alongside SSM.
- [[Lambda]]: Automation hooks.
- [[IAM Roles]]: Required for the SSM Agent and automation access.
- [[Secrets Manager]]: Alternative for higher-security, auto-rotated secrets.
- [[KMS]]: Encrypts SecureString parameters.
- [[S3]]: Stores patch baselines, documents, and inventory output.
- [[Config]]: Records and evaluates system configurations.
- [[CloudTrail]]: Logs Systems Manager API activity.
- [[EventBridge]]: Triggers automation on Systems Manager events.
- [[SQS]]: Queues commands and notifications for targets.

### Related Concepts

- Parameter Store: Secure config storage.
- Run Command: Execute commands at scale.
- Session Manager: Shell access without inbound ports.
- SSM Agent: The lightweight agent installed on managed instances.
- Patch Manager: Automated OS patching and compliance.
- State Manager: Desired-state configuration management.
- Maintenance Windows: Scheduled operational windows for large fleets.
- Hybrid Activations: Register on-premises servers as managed instances.
- OpsCenter: Centralized operational issue tracking.
