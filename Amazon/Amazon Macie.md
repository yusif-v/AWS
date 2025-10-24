#Amazon #Service 
### Amazon Macie

Fully managed data security service using machine learning and pattern matching to discover sensitive data, provide visibility into risks, and enable automated protection in Amazon S3. Automates bucket inventory, monitors for access issues, generates findings for public access or sensitive data (e.g., PII), and supports automated/targeted discovery jobs.

### Related Services

- [[Amazon S3]]: Primary storage for data scanning and protection.
- [[Amazon EventBridge]]: Routes findings to targets like Lambda or SNS.
- [[AWS Security Hub]]: Aggregates Macie findings for security posture.
- [[AWS Lambda]]: Automates remediation based on findings.
- [[AWS Organizations]]: Enables multi-account management.
- [[Amazon GuardDuty]]: Complements with threat detection.

### Related Concepts

- Sensitive Data Discovery: Automated sampling or jobs using managed/custom identifiers.
- Findings: Detailed reports on sensitive data or policy risks.
- Data Classification: ML-based detection of PII, financial info, credentials.
- Allow Lists: Excludes specific text/patterns from analysis.