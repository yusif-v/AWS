#AWS #Service #Security
### IAM Roles

IAM Roles are identities with permissions that are assumed to obtain temporary credentials via STS. Roles have no permanent keys and are used by AWS services (e.g., Lambda execution roles), EC2 instances, and federated users to grant scoped, temporary access.

### How It Works

- A role has a trust policy defining which principals may assume it.
- When assumed, STS returns temporary, rotating credentials.
- Permission policies attached to the role determine what it may do.
- No long-lived access keys; credentials expire automatically.
- Services or users switch into the role to act with its permissions.

### Key Features

- No permanent credentials; inherently safer than long-lived access keys.
- Service roles for EC2, Lambda, ECS, and other AWS services.
- Cross-account roles for delegating access between accounts.
- Federated role assumption for workforce identities via SSO.
- Role chaining for pass-role delegation patterns.

### Common Use Cases

- EC2 instances retrieving credentials from an instance profile.
- Lambda functions scoping permissions to their execution role.
- Granting a support or partner team scoped cross-account access.
- Federation where users sign in via SSO and assume a role.

### Pricing & Limits

- IAM roles are free.
- Default quota of 1,000 roles per account is adjustable.
- STS temporary credentials expire in minutes to hours (default 1 hour, max 12 hours).

### Related Services

- [[IAM]]: The service that defines roles and policies.
- [[STS]]: Issues the temporary credentials when a role is assumed.
- [[IAM Policies]]: Attach permissions to roles.
- [[IAM Identity Center]]: Grants SSO users permission sets backed by roles.
- [[EC2]]: Uses instance profiles to run with role credentials.
- [[Lambda]]: Runs functions with an execution role.
- [[AWS Organizations]]: Controls cross-account role usage with SCPs.

### Related Concepts

- Trust Policy: Who can assume the role.
- Temporary Credentials: Short-lived access keys.
- Cross-Account Access: Roles for account delegation.
- Least Privilege: Scope the role to the minimum needed.
- Pass Role: Delegating the right to pass a role to another principal.
