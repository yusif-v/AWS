#AWS #Service #Security
### ACM

AWS Certificate Manager (ACM) provisions, manages, and renews public and private SSL/TLS certificates for use with CloudFront, ALB, and API Gateway. Certificates integrate with Route 53 DNS validation and are automatically renewed.

### How It Works

- Requests, validates, and issues X.509 SSL/TLS certificates on your behalf.
- Supports DNS and email validation, with DNS validation via Route 53 recommended for automation.
- Stores certificates encrypted; private keys are managed by AWS and never exposed.
- Automatically renews certificates before expiry, removing manual renewal tasks.
- Integrates directly with HTTPS-facing services so no manual cert upload is needed.

### Key Features

- Automated issuance, deployment, and renewal of public certificates.
- Supports wildcard and multiple-domain (SAN) certificates.
- Optional ACM Private CA for issuing private certificates for internal use.
- Public certificates are free; you pay only for the AWS resources they protect.
- Managed private-key storage with lifecycle handled by AWS.

### Common Use Cases

- Enabling HTTPS on CloudFront distributions and Application Load Balancers.
- Securing API Gateway custom domain names with TLS.
- Issuing private certificates for internal services or mutual TLS between microservices.
- Centralizing certificate lifecycle management for fleet-wide TLS consistency.

### Pricing & Limits

- Public certificates issued by ACM are free of charge.
- ACM Private CA bills per private CA and per certificate issued.
- Public ACM certificates can only be used with AWS-integrated services; private keys cannot be exported.
- Imported certificates (e.g., from a third-party CA) do not get automated renewal.

### Related Services

- [[CloudFront]]: Serves HTTPS content with ACM certs.
- [[ELB]]: Terminates TLS with ACM certs.
- [[Route 53]]: DNS validation for cert issuance.
- [[API Gateway]]: Terminates TLS for custom domains using ACM certs.
- [[KMS]]: The related key-management service for encrypting data at rest.

### Related Concepts

- TLS/SSL: Encrypts traffic in transit.
- Auto-Renewal: Managed certificate lifecycle.
- Public vs Private CA: ACM public certs vs Private CA.
- Public Key Infrastructure (PKI): The trust framework ACM operates within.
- Certificate Validation: DNS or email proof of domain ownership.
