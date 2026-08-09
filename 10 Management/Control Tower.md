#AWS #Service #Management
### Control Tower

AWS Control Tower establishes a multi-account environment with guardrails. It creates accounts via AWS Organizations, applies preventive and detective controls (SCPs + Config rules), and provides a landing zone with centralized logging and identity. It is the recommended starting point for a well-governed, multi-account AWS environment.

### How It Works

- Control Tower builds a **landing zone** — a baseline multi-account setup using AWS Organizations as the underlying structure.
- Accounts are provisioned through **Account Factory**, which applies standard network, logging, and identity configuration to each new account.
- **Preventive guardrails** use Service Control Policies to block disallowed actions (e.g., preventing public S3 buckets or disabling CloudTrail).
- **Detective guardrails** use AWS Config rules to monitor for and flag non-compliant resources.
- Centralized logging collects CloudTrail, Config, and activity data into designated log archives; IAM Identity Center provides centralized identity.

### Key Features

- **Landing Zone**: Automated baseline of accounts, logging, identity, and guardrails.
- **Account Factory**: Standardized, repeatable account creation with pre-configured baselines.
- **Guardrails**: One-click preventive (SCP) and detective (Config) controls with compliance reporting.
- **Centralized Logging**: Aggregates audit and configuration logs across all accounts.
- **Account Factory for Terraform (AFT)**: Terraform-based alternative for account customization.
- **Guardrail Monitoring**: CloudWatch and dashboards track guardrail violations across the organization.

### Common Use Cases

- Standing up a new multi-account organization with governance from day one.
- Enforcing company-wide security baselines (e.g., deny root user actions, restrict regions).
- Enabling finance, security, and audit teams with cross-account visibility.
- Scaling account creation for many teams while keeping consistent guardrails.

### Pricing & Limits

- No additional charge for Control Tower itself; you pay for the underlying services it configures (Organizations, Config, CloudTrail, IAM Identity Center, etc.).
- Some services may incur costs once set up, such as Config rules and CloudTrail log storage.
- Managed organizations have limits on the number of accounts and guardrail count per landing zone.

### Related Services

- [[AWS Organizations]]: Account structure underneath.
- [[IAM Identity Center]]: Identity for the landing zone.
- [[Security Hub]]: Aggregates guardrail findings.
- [[CloudFormation]]: Powers the landing zone automation under the hood.
- [[CloudTrail]]: Centralized activity logging across accounts.
- [[Config]]: Detective guardrails and compliance monitoring.
- [[CloudWatch]]: Monitors guardrail status and environment health.
- [[SNS]]: Notifications for account and guardrail events.
- [[Artifact]]: Provides compliance documentation for the environment.

### Related Concepts

- Landing Zone: Baseline multi-account setup.
- Guardrails: Preventive/detective controls.
- Account Factory: Standardized account creation.
- Preventive vs Detective Controls: SCP-based blocking vs Config-rule detection.
- Centralized Logging and Identity: Aggregated logs plus SSO across accounts.
- Account Factory for Terraform (AFT): Customized account provisioning via Terraform.
