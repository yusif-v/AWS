#AWS #Service 
### AWS Key Management Service (KMS)

Fully managed service for creating, managing, and controlling cryptographic keys used to encrypt and decrypt data. Supports symmetric and asymmetric keys, integrates with AWS services, and enforces access policies. Ideal for securing sensitive data and ensuring compliance.

### Related Services

- [[Amazon S3]]: Encrypts objects using KMS keys.
- [[Amazon EBS]]: Secures volume data with KMS encryption.
- [[AWS Lambda]]: Uses KMS for encrypting environment variables.
- [[Amazon RDS]]: Encrypts databases with KMS keys.
- [[AWS CloudTrail]]: Logs KMS key usage for auditing.

### Related Concepts

- Cryptographic Keys: Symmetric (single key) and asymmetric (public/private key pairs) for encryption.
- Key Rotation: Automatically or manually rotates keys for security.
- Envelope Encryption: Protects data keys with KMS master keys.
- Access Policies: JSON-based policies control key usage and permissions.