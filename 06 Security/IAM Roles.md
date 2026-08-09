#AWS #Service #Security
### IAM Roles

IAM Roles are identities with permissions that are assumed to obtain temporary credentials via STS. Roles have no permanent keys and are used by AWS services (e.g., Lambda execution roles), EC2 instances, and federated users to grant scoped, temporary access.

### Related Services

- [[IAM]]: The service that defines roles and policies.
- [[STS]]: Issues the temporary credentials when a role is assumed.
- [[IAM Policies]]: Attach permissions to roles.

### Related Concepts

- Trust Policy: Who can assume the role.
- Temporary Credentials: Short-lived access keys.
- Cross-Account Access: Roles for account delegation.
