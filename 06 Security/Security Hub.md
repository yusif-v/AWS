#AWS #Service #Security
### Security Hub

AWS Security Hub aggregates security findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, and third-party tools into one view. It runs continuous checks against AWS Foundational Security Best Practices and CIS standards, enabling centralized posture management.

### How It Works

- Receives findings from AWS services and third-party providers.
- Runs automated checks against security standards.
- Aggregates findings across accounts and regions via a delegated administrator.
- Generates insights by querying across all findings.
- Sends findings to EventBridge for automated response.

### Key Features

- Continuous checks against AWS FSBP, CIS, and PCI DSS standards.
- Centralized findings dashboard with severity and status.
- Multi-account, multi-region aggregation.
- Custom insights for cross-cutting queries.
- Integrations with PagerDuty, Slack, and ticketing tools.

### Common Use Cases

- One-pane-of-glass security posture across accounts.
- Meeting CIS Foundations Benchmark compliance.
- Automating remediation of failed checks.
- Tracking security score and coverage over time.

### Pricing & Limits

- Billed per security check per month and per finding ingestion event.
- First 10,000 findings per month are free.
- Costs scale with checks executed and finding volume.

### Related Services

- [[GuardDuty]]: Feeds threat detection findings.
- [[Inspector]]: Feeds vulnerability findings.
- [[Config]]: Supports compliance checks.
- [[Macie]]: Feeds sensitive-data findings.
- [[Detective]]: Investigates the aggregated findings.
- [[CloudWatch]]: Monitors and alerts on Security Hub events.
- [[EventBridge]]: Routes findings to automated response actions.

### Related Concepts

- Findings: Aggregated security events.
- Standards: AWS FSBP, CIS, PCI DSS.
- Insight: Cross-finding queries.
- Security Posture: The overall security state measured across accounts.
- Automated Remediation: Responding to findings programmatically.
