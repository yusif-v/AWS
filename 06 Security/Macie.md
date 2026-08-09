#AWS #Service #Security
### Macie

Fully managed data security service using machine learning and pattern matching to discover sensitive data, provide visibility into risks, and enable automated protection in Amazon S3. Automates bucket inventory, monitors for access issues, generates findings for public access or sensitive data (e.g., PII), and supports automated/targeted discovery jobs.

### How It Works

- Automates an inventory of S3 buckets and their security posture.
- Runs automated or scheduled sensitive-data discovery jobs.
- Uses managed and custom identifiers with machine learning and pattern matching.
- Generates findings when sensitive data or policy risks are detected.
- Sends findings to EventBridge and Security Hub for response.

### Key Features

- Sensitive data discovery for PII, financial data, and credentials.
- Bucket policy and encryption posture monitoring.
- Managed data identifiers plus custom regex identifiers.
- Allow lists to exclude benign patterns from analysis.
- Multi-account coverage via a delegated administrator.

### Common Use Cases

- Locating PII stored in S3 for privacy compliance (GDPR, HIPAA).
- Detecting buckets that are publicly accessible.
- Verifying encryption status across the data estate.
- Auditing sensitive-data exposure before an audit.

### Pricing & Limits

- Billed per GB of data processed for discovery.
- Bucket policy findings are billed separately by bucket-month.
- Free 30-day trial of the full service.

### Related Services

- [[S3]]: Primary storage for data scanning and protection.
- [[EventBridge]]: Routes findings to targets like Lambda or SNS.
- [[Security Hub]]: Aggregates Macie findings for security posture.
- [[Lambda]]: Automates remediation based on findings.
- [[AWS Organizations]]: Enables multi-account management.
- [[GuardDuty]]: Complements with threat detection.
- [[S3 Access Control]]: Controls who can read the data Macie inspects.

### Related Concepts

- Sensitive Data Discovery: Automated sampling or jobs using managed/custom identifiers.
- Findings: Detailed reports on sensitive data or policy risks.
- Data Classification: ML-based detection of PII, financial info, credentials.
- Allow Lists: Excludes specific text/patterns from analysis.
- Data Privacy: Governing how personal data is stored and accessed.
