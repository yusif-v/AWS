#AWS #Service 
### AWS Identity and Access Management (IAM)

Fully managed service for securely controlling access to AWS resources. Defines users, groups, roles, and policies (JSON documents) to grant permissions. Supports multi-factor authentication (MFA), identity federation, and temporary credentials via STS.

### Related Services

- AWS Single Sign-On (SSO): Centralizes access across AWS accounts and applications.
- AWS Organizations: Applies centralized IAM policies across multiple accounts.
- Amazon Cognito: Handles user authentication for apps, integrating with IAM.
- AWS STS: Issues temporary credentials for roles and federation.
- [[Amazon CloudWatch]]: Monitors IAM events and access patterns.

### Related Concepts

- Principle of Least Privilege: Grants minimal permissions needed for tasks.
- IAM Policies: JSON rules defining actions, resources, and conditions.
- Role Assumption: Allows temporary access via roles for users or services.
- Identity Federation: Integrates external providers (e.g., SAML, OIDC) for SSO.