#AWS #Service #Security
### IAM Identity Center

AWS IAM Identity Center (formerly AWS SSO) provides centralized single sign-on across AWS accounts and business applications. It connects to external identity providers (SAML/OIDC), manages permission sets for account access, and supports MFA policies.

### How It Works

- Defines users and groups in the Identity Center directory or syncs from an external IdP.
- Permission sets define role-like permissions applied per AWS account.
- Users sign in once and receive temporary credentials via STS for each account.
- Supports AWS account access, Identity Center-integrated apps, and SAML apps.
- Enforces MFA centrally across the federated environment.

### Key Features

- Single sign-on for multiple AWS accounts and accounts in AWS Organizations.
- Built-in support for Identity Center-integrated applications.
- Application assignments based on group membership.
- Centralized MFA policies and activity auditing.
- Synchronization from Microsoft Entra ID, Okta, and other identity providers.

### Common Use Cases

- Centralizing access for many AWS accounts without maintaining IAM users per account.
- Assigning developers and teams scoped permission sets per environment.
- SSO for third-party SaaS applications alongside AWS access.
- Auditing who signed in to which account and when.

### Pricing & Limits

- No additional charge for the core IAM Identity Center service.
- You pay only for the underlying AWS resources accessed.
- License costs may apply for certain third-party IdP connector features.

### Related Services

- [[IAM]]: Underlying account permissions.
- [[AWS Organizations]]: Scope of accounts for SSO.
- [[Cognito]]: Customer-facing app authentication (distinct use case).
- [[IAM Policies]]: Define the permissions inside permission sets.
- [[IAM Roles]]: Back the permission sets used per account.
- [[STS]]: Issues temporary credentials after SSO sign-in.

### Related Concepts

- SSO: Single sign-on for users.
- Permission Set: Role-like assignment per account.
- Identity Provider: External IdP federation.
- Workforce Identity: Employee access vs customer identities (Cognito).
- MFA Policy: Centrally enforced multi-factor requirements.
