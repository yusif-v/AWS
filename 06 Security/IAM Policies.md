#AWS #Service #Security
### IAM Policies

IAM Policies are JSON documents that define permissions — which actions are allowed or denied on which resources under which conditions. Policies attach to IAM users, groups, or roles, and support managed, inline, and customer-managed policy types.

### How It Works

- A policy is a JSON document with Version, Statement, and one or more statements.
- Each statement contains Effect (Allow/Deny), Action, Resource, and optional Condition.
- Policies attach to users, groups, or roles; identity-based policies grant permissions.
- Explicit Deny always overrides Allow during evaluation.
- The combined effect of all applicable policies yields the effective permissions.

### Key Features

- Managed policies (AWS managed and customer managed) are reusable and versioned.
- Inline policies are embedded directly in a single user, group, or role.
- Resource-based policies (e.g., S3 bucket policy) grant cross-account access.
- Conditions (IP, time, MFA, principal tag) add granular access control.
- IAM Policy Simulator validates the effect of a policy before deployment.

### Common Use Cases

- Granting least-privilege access to users and roles.
- Denying access outside a corporate IP range or without MFA.
- Delegating permissions across accounts using resource-based policies.
- Enforcing service-specific constraints (e.g., read-only EC2 access).

### Pricing & Limits

- IAM itself is free; policies incur no direct cost.
- Limits include the number of managed policies per account and policy document size (5 KB for most, 10 KB for S3).
- Over-permissioned policies increase operational and security risk.

### Related Services

- [[IAM]]: The service enforcing policies.
- [[IAM Roles]]: Identities that carry policies.
- [[STS]]: Evaluates policies when issuing credentials.
- [[IAM Identity Center]]: Applies policies via permission sets across accounts.
- [[AWS Organizations]]: Uses SCPs to cap what IAM policies can grant.

### Related Concepts

- Allow vs Deny: Explicit deny overrides allow.
- Policy Elements: Effect, Action, Resource, Condition.
- Least Privilege: Grant minimal permissions.
- Identity-Based vs Resource-Based Policies: Attached to principals vs resources.
- SCP (Service Control Policy): Organization-level permission boundaries.
- Condition Keys: Contextual requirements in policy statements.
