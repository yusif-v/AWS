#AWS #Service #Security
### Cognito

Fully managed identity service for secure user authentication, authorization, and user management in web and mobile applications. Provides user pools for sign-up/sign-in and identity pools for access to AWS resources. Supports social logins, MFA, and federation with SAML/OIDC.

### How It Works

- User pools manage sign-up, sign-in, and profile data for application users.
- Identity pools exchange tokens for temporary AWS credentials via STS.
- Issues JWTs (ID token, access token, refresh token) after successful authentication.
- Supports a hosted UI for login plus custom authentication flows via Lambda triggers.
- Federates with external identity providers (Google, Facebook, SAML, OIDC).

### Key Features

- Built-in user directory with sign-up, verification, and password management.
- MFA enforcement including TOTP and SMS.
- Advanced security features such as adaptive authentication and compromised-credential detection.
- Role-based access to AWS resources through identity pools.
- Integration with API Gateway authorizers for protecting APIs.

### Common Use Cases

- Customer-facing authentication for web and mobile apps.
- Social login (Google, Facebook, Apple) without building OAuth flows from scratch.
- Granting authenticated or unauthenticated users scoped access to AWS resources.
- Enterprise SSO into an application via SAML or OIDC federation.

### Pricing & Limits

- Free tier includes a monthly allotment of monthly active users (MAU).
- Charged per MAU beyond the free tier; advanced security features are extra.
- No upfront cost; billed as a managed service based on active users.

### Related Services

- [[API Gateway]]: Integrates with Cognito for securing API access.
- [[IAM]]: Works with Cognito identity pools to grant AWS resource access.
- [[Lambda]]: Triggers custom authentication workflows or processes Cognito events.
- [[S3]]: Stores user data or integrates with identity pools for access.
- [[STS]]: Issues the temporary credentials behind identity pools.
- [[IAM Identity Center]]: Employee/workforce identity, distinct from Cognito's customer identity.

### Related Concepts

- User Authentication: Verifies user identities via credentials or social providers.
- User Authorization: Controls access to resources using tokens or roles.
- Identity Federation: Integrates external identity providers (e.g., Google, SAML) for single sign-on.
- JWT Tokens: Cognito issues JSON Web Tokens for secure user sessions.
- Identity Pool: Maps authenticated identities to temporary AWS credentials.
