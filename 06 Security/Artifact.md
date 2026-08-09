#AWS #Service #Security
### Artifact

Self-service portal for on-demand access to AWS compliance documents, such as SOC, PCI DSS, ISO, and Attestation of Compliance (AOC) reports. Enables customers to download reports, agreements, and certifications to verify AWS security and compliance for audits or regulatory requirements.

### How It Works

- AWS publishes compliance and security reports to a single self-service console.
- Customers sign in, accept the applicable NDA, and download the reports.
- Reports document AWS's security posture and serve as evidence during customer audits.
- Artifact also lists which AWS services are in scope for each compliance program.

### Key Features

- On-demand access to SOC 1/2/3, PCI DSS, ISO 27001/27017/27018, and FedRAMP reports.
- Artifact Agreements provides managed workflows for legal and compliance teams.
- Report versioning so auditors see the evidence relevant to the reporting period.
- Centralized access across the account with no per-report cost.

### Common Use Cases

- Gathering evidence for SOC 2 or ISO 27001 customer audits.
- Demonstrating PCI DSS scope and compliance of AWS-managed services.
- Pre-audit readiness reviews with security and legal stakeholders.
- Understanding which AWS services are in scope for a given compliance program.

### Pricing & Limits

- Artifact itself is free; access requires an AWS account.
- Some reports require acceptance of an NDA before download.
- Reports are delivered as PDFs with no per-download charge.

### Related Services

- AWS Audit Manager: Uses Artifact reports to automate compliance evidence collection.
- [[Config]]: Tracks resource configurations to support compliance referenced in Artifact documents.
- [[CloudTrail]]: Logs API activity for auditing, complementing Artifact’s compliance reports.
- AWS Security Hub: Centralizes compliance findings, leveraging Artifact documents.
- [[Security Hub]]: Provides continuous compliance checks that pair with Artifact evidence.
- [[GuardDuty]]: Threat detection that supports the audit and compliance story.

### Related Concepts

- Compliance Documentation: Provides evidence of AWS adherence to standards like PCI DSS, HIPAA, GDPR.
- Shared Responsibility Model: Artifact reports clarify AWS vs. customer compliance roles.
- Audit Readiness: Enables customers to prepare for regulatory audits with verified reports.
- Non-Disclosure Agreements (NDAs): Required for accessing certain sensitive reports.
- Governance: Using evidence and reports to satisfy organizational and regulatory policy.
