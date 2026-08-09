#AWS #Service #Security
### KMS

Fully managed service for creating, managing, and controlling cryptographic keys used to encrypt and decrypt data. Supports symmetric and asymmetric keys, integrates with AWS services, and enforces access policies. Ideal for securing sensitive data and ensuring compliance.

### How It Works

- Creates symmetric (AES-256) and asymmetric (RSA/ECC) customer master keys (KMS keys).
- Keys are stored in FIPS 140-2 validated hardware (HSM) and never leave KMS.
- Integrates with AWS services for transparent encryption at rest.
- Enables envelope encryption: encrypts data keys with a master key.
- Access is controlled via key policies combined with IAM and grants.

### Key Features

- Symmetric and asymmetric keys for encryption and signing.
- Automatic key rotation (yearly) for symmetric keys.
- Custom key stores backed by your own CloudHSM cluster.
- Grants and key policies for fine-grained key access.
- AWS-managed keys and customer-managed keys.

### Common Use Cases

- Encrypting S3 objects, EBS volumes, and RDS databases at rest.
- Encrypting secrets stored in Secrets Manager.
- Signing and verifying data using asymmetric keys.
- Multi-region keys for global encryption consistency.

### Pricing & Limits

- $1 per month per customer-managed KMS key.
- Pay per request (Encrypt, Decrypt, GenerateDataKey).
- Free tier includes AWS-managed keys and 20,000 requests per month.

### Related Services

- [[S3]]: Encrypts objects using KMS keys.
- [[EBS]]: Secures volume data with KMS encryption.
- [[Lambda]]: Uses KMS for encrypting environment variables.
- [[RDS]]: Encrypts databases with KMS keys.
- [[CloudTrail]]: Logs KMS key usage for auditing.
- [[Secrets Manager]]: Encrypts stored secrets with KMS keys.
- [[CloudHSM]]: Dedicated HSM alternative with full key custody.
- [[ACM]]: Manages TLS certificates, while KMS manages data encryption keys.

### Related Concepts

- Cryptographic Keys: Symmetric (single key) and asymmetric (public/private key pairs) for encryption.
- Key Rotation: Automatically or manually rotates keys for security.
- Envelope Encryption: Protects data keys with KMS master keys.
- Access Policies: JSON-based policies control key usage and permissions.
- FIPS 140-2: Validated HSM hardware backing key storage.
