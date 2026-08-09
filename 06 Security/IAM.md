#AWS #Service #Security
### IAM

Fully managed service for securely controlling access to AWS resources. Defines users, groups, roles, and policies (JSON documents) to grant permissions. Supports multi-factor authentication (MFA), identity federation, and temporary credentials via STS.

### How It Works

- IAM is global; policies apply across all regions by default.
- Principals (users, groups, roles) are granted permissions through policies.
- IAM evaluates all applicable identity-based and resource-based policies.
- Access keys for users are long-lived; roles provide temporary credentials via STS.
- Service control policies in AWS Organizations cap what IAM can grant.

### Key Features

- Users, groups, roles, and policies for fine-grained access control.
- Multi-factor authentication (MFA) for privileged accounts.
- Identity federation with SAML 2.0 and OIDC providers.
- Password policies, access key rotation, and credential reports.
- IAM Access Analyzer identifies resources shared outside the account.

### Common Use Cases

- Defining least-privilege access for humans and workloads.
- Enforcing MFA on administrator accounts and the root user.
- Delegating temporary access via role assumption.
- Auditing permissions and detecting excessive or unused access.

### Pricing & Limits

- IAM is free of charge; no cost for users, groups, roles, or policies.
- Quotas include role count, group count, and policy document size.
- Reliance on long-lived access keys raises risk; prefer roles and temporary credentials.

### Related Services

- AWS Single Sign-On (SSO): Centralizes access across AWS accounts and applications.
- [[AWS Organizations]]: Applies centralized IAM policies across multiple accounts.
- [[Cognito]]: Handles user authentication for apps, integrating with IAM.
- AWS STS: Issues temporary credentials for roles and federation.
- [[CloudWatch]]: Monitors IAM events and access patterns.
- [[IAM Identity Center]]: Replaces per-account IAM users with centralized SSO.
- [[STS]]: Issues the temporary credentials behind role assumption.

### Related Concepts

- Principle of Least Privilege: Grants minimal permissions needed for tasks.
- IAM Policies: JSON rules defining actions, resources, and conditions.
- Role Assumption: Allows temporary access via roles for users or services.
- Identity Federation: Integrates external providers (e.g., SAML, OIDC) for SSO.
- Shared Responsibility Model: AWS manages infrastructure; customers manage IAM.
- AWS Account & Root User: The account root is the most powerful identity.

### Policies & Roles

- [[IAM Policies]]: JSON documents that define permissions.
- [[IAM Roles]]: Temporary credentials for users and services.

### Federated Access

- [[IAM Identity Center]]: Centralized SSO across AWS accounts and apps.
- [[STS]]: Issues the temporary credentials behind roles.
