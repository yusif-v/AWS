#AWS #Concept 
### AWS Shared Responsibility Model

Framework defining the division of security and compliance responsibilities between AWS and customers. AWS manages the security of the cloud infrastructure (physical data centers, hardware, virtualization), while customers manage security in the cloud (data, applications, configurations). Responsibilities vary by service type (IaaS, PaaS, SaaS), ensuring a secure and compliant cloud environment.

### AWS Responsibilities

- **Physical Security**: Secures data centers with restricted access, surveillance, and environmental controls.
- **Hardware and Software**: Manages compute, storage, networking hardware, and virtualization layers.
- **Global Infrastructure**: Ensures availability of Regions, Availability Zones, and edge locations.
- **Service Operations**: Patches and maintains AWS-managed services (e.g., DynamoDB, Lambda).
- **Compliance Certifications**: Achieves standards like ISO 27001, SOC, PCI DSS via AWS Artifact.
- **Network Security**: Protects against DDoS (AWS Shield) and secures internal data transit.

### Customer Responsibilities

- **Data Protection**: Encrypts data at rest (KMS) and in transit (TLS/SSL).
- **IAM**: Configures users, roles, policies, and MFA for access control.
- **OS and Applications**: Patches guest OS and secures applications (e.g., EC2).
- **Network Configuration**: Manages VPCs, security groups, and network ACLs.
- **Compliance**: Configures resources for regulatory needs (e.g., GDPR, HIPAA).
- **Monitoring**: Uses CloudWatch and CloudTrail for resource oversight.

### Variation by Service

- **[[Infrastructure as a Service (IaaS)|IaaS]] (EC2)**: Customers manage guest OS, applications, and configurations.
- **[[Platform as a Service (PaaS)|PaaS]] (RDS, Elastic Beanstalk)**: AWS manages OS; customers handle data and access.
- **[[Software as a Service (SaaS)|SaaS]] (WorkSpaces)**: AWS manages most aspects; customers manage user access and data.

### Shared Controls

- **Patch Management**: AWS patches infrastructure; customers patch OS/apps.
- **Configuration**: AWS secures services; customers configure resources.
- **Training**: AWS provides compliance docs; customers train teams.

### Related Services

- [[AWS IAM]]: Manages user access and permissions for customer responsibilities.
- [[AWS Key Management Service (KMS)]]: Encrypts data at rest for customer-managed security.
- [[Amazon CloudTrail]]: Logs API activity for auditing customer actions.
- [[Amazon CloudWatch]]: Monitors resources for customer oversight.
- [[AWS Artifact]]: Provides compliance reports for AWS infrastructure certifications.
- [[AWS Shield]]: Protects infrastructure from DDoS attacks.

### Related Concepts

- Principle of Least Privilege: Grants minimal permissions for security.
- Compliance Frameworks: AWS supports GDPR, HIPAA, PCI DSS; customers configure compliance.
- Data Encryption: Protects data at rest and in transit for security.
- Monitoring and Logging: Tracks resource activity for security and compliance.