#AWS #Service #Security
### CloudHSM

AWS CloudHSM provides dedicated hardware security modules (HSMs) for generating and storing cryptographic keys. Unlike KMS's shared, AWS-managed service, CloudHSM gives customers exclusive control over the HSM and keys, satisfying compliance requirements for hardware key custody.

### How It Works

- Deploys dedicated, single-tenant HSMs in your VPC, reachable via elastic network interfaces.
- Customers control the HSMs directly, including key management and HSM client software.
- Keys never leave the tamper-resistant hardware; crypto operations run on the HSM.
- FIPS 140-2 Level 3 validated hardware protects the key material.
- Integrates with applications via industry-standard APIs (PKCS#11, JCE, OpenSSL).

### Key Features

- Exclusive customer ownership of the HSM appliance and its keys.
- Full control over the key lifecycle, including deletion and backup.
- High availability by clustering multiple HSMs across Availability Zones.
- FIPS 140-2 Level 3 compliance for regulated workloads.
- No AWS access to keys; customers export and manage their own backups.

### Common Use Cases

- Meeting regulatory requirements (PCI, HIPAA) for hardware key custody.
- Protecting the CA root keys of your own private PKI.
- Offloading TLS or code-signing private-key operations to hardware.
- Applications that require a dedicated HSM for compliance or security policy.

### Pricing & Limits

- Billed per HSM instance per hour.
- Requires customer-managed clusters and redundancy for high availability.
- Pay for dedicated hardware regardless of actual usage.

### Related Services

- [[KMS]]: Managed alternative for key storage.
- [[ACM]]: Can integrate with private CA.
- [[CloudTrail]]: Logs management events for HSM cluster activity.
- [[VPC]]: Hosts the HSM endpoints for private network access.
- [[IAM]]: Controls access to CloudHSM cluster management.

### Related Concepts

- HSM: Tamper-resistant hardware for keys.
- Key Custody: Exclusive customer control.
- FIPS: Validated hardware modules.
- Envelope Encryption: A KMS pattern; CloudHSM offers direct hardware control instead.
- Single-Tenancy: Dedicated hardware not shared with other customers.
