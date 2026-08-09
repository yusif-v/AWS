#AWS #Service #Security
### Secrets Manager

AWS Secrets Manager securely stores and rotates database credentials, API keys, and other secrets. It integrates with RDS and Lambda for automatic rotation, encrypts secrets with KMS, and enforces fine-grained access via IAM.

### Related Services

- [[KMS]]: Encrypts secrets at rest.
- [[RDS]]: Credential rotation for databases.
- [[IAM]]: Authorizes secret access.

### Related Concepts

- Secret Rotation: Automated credential replacement.
- Secret Versioning: Multiple versions of a secret.
- Retrieval API: Get secret value with IAM.
