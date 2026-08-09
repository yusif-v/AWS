#AWS #Service #Management
### AWS Organizations

AWS Organizations centrally manages multiple AWS accounts. It provides consolidated billing, Service Control Policies (SCPs) for guardrails, and organizational units (OUs) to organize accounts — the foundation for multi-account architecture. One account acts as the management account that owns the organization; all others are member accounts.

### How It Works

- Accounts are arranged in a hierarchy under a single management (root) account, with child OUs grouping related accounts (e.g., by environment or business unit).
- Policies such as SCPs attach to OUs or accounts and constrain the maximum permissions any IAM principal can receive.
- Consolidated billing aggregates usage across all member accounts onto one invoice, which can unlock volume pricing discounts.
- Invitations or the CreateAccount API add accounts; the management account can also create new accounts directly.
- With all features enabled, the organization can use centralized logging, security, and cross-account services such as IAM Identity Center.

### Key Features

- **Organizational Units (OUs)**: Hierarchical containers that simplify applying policies to groups of accounts.
- **Service Control Policies (SCPs)**: Preventative guardrails that deny or allow actions at the account level; they do not grant permissions.
- **Consolidated Billing**: One bill for the whole organization with cost visibility across member accounts.
- **Tag Policies**: Enforce consistent tagging across accounts and resources.
- **AI Services Opt-Out Policies**: Control whether member accounts can use AI services for certain purposes.
- **Backup Policies**: Centrally define backup plans applied via AWS Backup across accounts.

### Common Use Cases

- Enforcing separation of environments (prod, dev, test) into different OUs with different guardrails.
- Rolling out a company-wide baseline of SCPs to limit service usage and control regions.
- Centralizing billing and cost monitoring with tools like AWS Budgets and AWS Cost Explorer.
- Granting cross-account access for centralized security or networking teams via IAM roles.

### Pricing & Limits

- The service itself is free; you pay only for the AWS resources used within member accounts.
- Limits scale with account structure — up to thousands of accounts per organization, with default quotas on the number of OUs and SCPs per OU.
- Consolidated billing can qualify the organization for aggregate volume discounts.

### Related Services

- [[Control Tower]]: Automates Organizations-based landing zones.
- [[IAM]]: Permissions within each account.
- [[IAM Identity Center]]: SSO across organization accounts.
- [[AWS Budgets]]: Track and alert on consolidated spend.
- [[CloudTrail]]: Logs organization-level API activity.
- [[Security Hub]]: Aggregates security findings across member accounts.
- [[AWS Account & Root User]]: Root user access control within member accounts.
- [[Config]]: Aggregates compliance posture across accounts.

### Related Concepts

- OU: Organizational unit grouping accounts.
- SCP: Guardrails on account permissions.
- Consolidated Billing: Single bill for all accounts.
- Management vs Member Accounts: One management account owns the organization and manages all member accounts.
- All-Features vs Billing-Only Mode: Controls whether governance features like SCPs are available.
- Tagging Policies: Enforce consistent resource tagging across the organization.
