#AWS #Service #Security
### Secrets Manager

AWS Secrets Manager securely stores and rotates database credentials, API keys, and other secrets. It integrates with RDS and Lambda for automatic rotation, encrypts secrets with KMS, and enforces fine-grained access via IAM.

### How It Works

- Stores secrets as encrypted blobs under a KMS key.
- Rotation is configured via Lambda rotation functions.
- Retrieval happens through the API or SDK, authorized by IAM.
- Supports automatic rotation for RDS, Redshift, DocumentDB, and more.
- Versioned secrets retain history for rollback.

### Key Features

- Automatic secret rotation with built-in and custom Lambda rotations.
- Secret versioning and staged rotation for zero-downtime rollover.
- Fine-grained IAM access to individual secrets.
- Replication across regions for disaster recovery and latency.
- Retrieval caching in the SDK to reduce API costs.

### Common Use Cases

- Managing RDS database credentials without hardcoding them.
- Storing API keys and third-party tokens for applications.
- Enabling Lambda functions to retrieve secrets at runtime.
- Rotating credentials automatically to limit exposure.

### Pricing & Limits

- $0.40 per secret per month.
- $0.05 per 10,000 API calls.
- Rotation costs include Lambda function invocations.

### Related Services

- [[KMS]]: Encrypts secrets at rest.
- [[RDS]]: Credential rotation for databases.
- [[IAM]]: Authorizes secret access.
- [[Lambda]]: Runs rotation functions and retrieves secrets.
- [[CloudTrail]]: Logs secret access for auditing.
- [[Systems Manager]]: Alternative for parameter-style storage.

### Related Concepts

- Secret Rotation: Automated credential replacement.
- Secret Versioning: Multiple versions of a secret.
- Retrieval API: Get secret value with IAM.
- Envelope Encryption: KMS protects the secret encryption keys.
- Least Privilege: Scope IAM policies to specific secrets.
