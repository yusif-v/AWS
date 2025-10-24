#AWS #Service 
### AWS Security Token Service (STS)

Service for granting temporary, limited-privilege credentials for AWS IAM users or federated users. Issues short-lived access tokens for accessing AWS resources, supporting role assumption and identity federation. Enhances security by reducing long-term credential exposure.

### Related Services

- AWS IAM: Manages users, roles, and policies integrated with STS.
- [[Amazon Cognito]]: Uses STS for temporary credentials in identity pools.
- [[AWS Single Sign-On (SSO)]]: Leverages STS for federated access to AWS accounts.
- Amazon S3: Accesses resources using STS temporary credentials.
- AWS Lambda: Assumes roles via STS for function execution.

### Related Concepts

- Temporary Credentials: Short-lived tokens (minutes to hours) for secure access.
- Role Assumption: Allows users or services to assume IAM roles for specific tasks.
- Identity Federation: Enables access via external identity providers (e.g., SAML, OIDC).
- Principle of Least Privilege: STS ensures minimal permissions for temporary access.