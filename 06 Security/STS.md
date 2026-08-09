#AWS #Service #Security
### STS

Service for granting temporary, limited-privilege credentials for AWS IAM users or federated users. Issues short-lived access tokens for accessing AWS resources, supporting role assumption and identity federation. Enhances security by reducing long-term credential exposure.

### How It Works

- Generates temporary credentials composed of an access key, secret key, and session token.
- Credentials have a default lifetime (typically 1 hour, up to 12 hours for roles).
- Roles are assumed via AssumeRole; federated users via AssumeRoleWithSAML or WebIdentity.
- The session carries a limited privilege set derived from the role's policies.
- Credentials are automatically rotated by AWS; no manual key management.

### Key Features

- Short-lived credentials that reduce exposure if leaked.
- Role assumption for services, users, and cross-account access.
- SAML and web identity federation (OIDC) support.
- Session policies to further restrict a role session.
- Global, region-agnostic service endpoint.

### Common Use Cases

- EC2 instances assuming a role via an instance profile.
- Lambda functions getting scoped execution credentials.
- Federated users signing in via SSO and receiving temporary keys.
- Cross-account delegation with AssumeRole.

### Pricing & Limits

- STS is free; no cost for issuing credentials.
- Session duration is configurable (15 minutes to 12 hours for roles).
- There are quotas on concurrent sessions per account.

### Related Services

- AWS IAM: Manages users, roles, and policies integrated with STS.
- [[Cognito]]: Uses STS for temporary credentials in identity pools.
- AWS Single Sign-On (SSO): Leverages STS for federated access to AWS accounts.
- Amazon S3: Accesses resources using STS temporary credentials.
- AWS Lambda: Assumes roles via STS for function execution.
- [[IAM]]: Defines the roles and policies STS acts upon.
- [[IAM Roles]]: The identities that produce STS credentials.
- [[IAM Policies]]: Bound the permissions of the session.

### Related Concepts

- Temporary Credentials: Short-lived tokens (minutes to hours) for secure access.
- Role Assumption: Allows users or services to assume IAM roles for specific tasks.
- Identity Federation: Enables access via external identity providers (e.g., SAML, OIDC).
- Principle of Least Privilege: STS ensures minimal permissions for temporary access.
- Session Token: The third credential component that scopes the session.
