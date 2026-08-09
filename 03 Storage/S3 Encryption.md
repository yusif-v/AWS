#AWS #Service #Storage
### S3 Encryption

Amazon S3 encrypts data at rest with server-side or client-side encryption to protect objects from unauthorized access. Server-side options include SSE-S3 (S3-managed keys), SSE-KMS (AWS Key Management Service), and SSE-C (customer-provided keys), with default encryption enforceable at the bucket level.

### How It Works

- Server-side encryption (SSE) encrypts objects before they are written to disk and decrypts them transparently on read.
- SSE-S3 uses S3-managed AES-256 keys with no extra cost and no key management burden.
- SSE-KMS uses KMS customer managed or AWS managed keys, enabling envelope encryption, key rotation, and audit trails.
- SSE-C lets you supply your own encryption keys, which S3 uses for encryption and then discards.
- Client-side encryption encrypts data before upload, so AWS never sees plaintext; the client manages keys.
- Bucket default encryption enforces a chosen mode for all objects written without explicit encryption headers.

### Key Features

- Encryption at rest for all objects regardless of storage class.
- Encryption in transit via TLS/HTTPS, optionally enforced with bucket policies.
- Integration with [[KMS]] for centralized key management, rotation, and CloudTrail audit logging.
- Bucket policies can require encryption on upload (`s3:x-amz-server-side-encryption` condition).
- Works with replication so encrypted objects are replicated securely.
- Combines with S3 Object Lock for compliance and WORM requirements.

### Common Use Cases

- Compliance with PCI-DSS, HIPAA, and other regulations requiring encryption at rest.
- Protecting sensitive data such as PII, credentials, and financial records in data lakes.
- Enforcing encryption organization-wide via bucket defaults and service control policies.
- Using customer-managed KMS keys for fine-grained control over who can decrypt.
- Client-side encryption when the encryption key must never be held by AWS.

### Pricing & Limits

- SSE-S3 encryption is free; SSE-KMS adds a per-request KMS API cost.
- SSE-C has no additional charge beyond standard storage and request pricing.
- KMS requests for encrypt/decrypt are billed by KMS usage; each new object encryption typically incurs one KMS request.

### Related Services

- [[S3]]: The object storage service where encryption is applied.
- [[KMS]]: Provides the keys and envelope encryption for SSE-KMS.
- [[CloudTrail]]: Logs KMS key usage for auditing decryption events.
- [[S3 Access Control]]: Controls who can read (and therefore decrypt) objects.
- [[S3 Replication]]: Copies encrypted objects across buckets and regions.

### Related Concepts

- Encryption at Rest: Data is unreadable without the key while stored.
- Encryption in Transit: TLS protects data during transfer.
- Envelope Encryption: Data is encrypted with a data key, which is itself encrypted by a master key.
- Default Encryption: Bucket-level setting that ensures new objects are encrypted.
- Key Management: Rotation, access control, and auditing of encryption keys via KMS.
