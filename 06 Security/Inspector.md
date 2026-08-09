#AWS #Service #Security
### Inspector

Fully managed vulnerability management service that scans AWS workloads (EC2, Lambda, ECR) for software vulnerabilities and unintended network exposure. Provides risk scores, automated assessments, remediation recommendations, and integrations for security monitoring.

### How It Works

- Uses an agent on EC2 instances (or SSM agent integration) to collect telemetry.
- Continuously or on-demand scans software inventory and network reachability.
- Scores findings by severity and exploitability to prioritize fixes.
- Evaluates container images in ECR for common vulnerabilities and exposures.
- Supports Lambda function and layer scanning.

### Key Features

- Continuous vulnerability and network exposure scanning for EC2.
- ECR container image scanning for critical CVEs.
- Lambda function scanning for vulnerabilities and secrets.
- Network Reachability findings that reveal unintended exposure.
- Integration with Security Hub and EventBridge for automation.

### Common Use Cases

- Remediating known CVEs before an attacker can exploit them.
- Identifying internet-exposed resources with weak security groups.
- Meeting PCI DSS and NIST vulnerability management requirements.
- Automating patch workflows via Systems Manager integration.

### Pricing & Limits

- Billed per instance per month and per image scanned.
- Free trial available; costs scale with workload count.
- Requires Systems Manager (SSM) agent or Inspector agent on instances.

### Related Services

- [[Security Hub]]: Aggregates Inspector findings for centralized security.
- [[EC2]]: Scans instances for vulnerabilities.
- [[Lambda]]: Assesses functions and layers.
- Amazon ECR: Scans container images.
- [[CloudWatch]]: Monitors Inspector metrics and events.
- [[Systems Manager]]: Provides the agent and patch workflows.
- [[EventBridge]]: Routes findings to automation and alerting.

### Related Concepts

- Vulnerability Scanning: Continuous detection of security risks.
- Risk Prioritization: Scores findings based on severity and exploitability.
- Automated Remediation: Integrates with workflows for fixes.
- Compliance: Supports standards like PCI DSS and NIST.
- Network Exposure: Unintended reachability of resources from the internet.
