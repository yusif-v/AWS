#AWS #Service #Security
### ACM

AWS Certificate Manager (ACM) provisions, manages, and renews public and private SSL/TLS certificates for use with CloudFront, ALB, and API Gateway. Certificates integrate with Route 53 DNS validation and are automatically renewed.

### Related Services

- [[CloudFront]]: Serves HTTPS content with ACM certs.
- [[ELB]]: Terminates TLS with ACM certs.
- [[Route 53]]: DNS validation for cert issuance.

### Related Concepts

- TLS/SSL: Encrypts traffic in transit.
- Auto-Renewal: Managed certificate lifecycle.
- Public vs Private CA: ACM public certs vs Private CA.
