#AWS #Service #Security
### GuardDuty

Intelligent threat detection service that continuously monitors AWS accounts and workloads for malicious activity and unauthorized behavior. Uses machine learning, anomaly detection, and threat intelligence to identify threats like compromised instances or reconnaissance. Generates findings with remediation recommendations.

### How It Works

- Analyzes continuous streams of VPC flow logs, DNS query logs, and CloudTrail management events.
- Applies machine learning, anomaly detection, and threat intelligence feeds.
- Produces findings with severity, confidence, and recommended remediation.
- Sends findings to CloudWatch Events/EventBridge for automated response.
- Coverage includes EC2, S3, EKS, RDS, and Lambda workloads.

### Key Features

- 30-day free trial; thereafter billed per data source analyzed.
- GuardDuty protection for S3 data events and EKS audit logs.
- Malware protection that scans suspicious files in EC2 and containers.
- Threat intelligence on malicious IPs, domains, and behaviors.
- Centralized multi-account management via a delegated administrator.

### Common Use Cases

- Detecting compromised EC2 instances communicating with command-and-control servers.
- Identifying credential compromise or unusual API activity.
- Spotting S3 data-exfiltration patterns and unusual object access.
- Automating responses (isolate instance, revoke key) via Lambda/EventBridge.
- Meeting compliance requirements with continuous threat monitoring.

### Pricing & Limits

- Billed per GB of analyzed log data per service analyzed.
- Separate charges for S3 data event analysis and EKS audit log analysis.
- No minimum commitment; pay only for the data analyzed.

### Related Services

- [[CloudWatch]]: Monitors and triggers actions based on GuardDuty findings.
- [[CloudTrail]]: Provides API and user activity logs for GuardDuty analysis.
- [[S3]]: Stores GuardDuty findings and logs.
- [[Lambda]]: Automates responses to GuardDuty alerts.
- [[IAM]]: Secures access to GuardDuty resources and findings.
- [[Detective]]: Deep-dives into GuardDuty findings for investigation.
- [[Security Hub]]: Aggregates GuardDuty findings into one console.
- [[AWS Organizations]]: Enables multi-account GuardDuty deployment.

### Related Concepts

- Threat Detection: Identifies suspicious activities using ML and threat intelligence.
- Security Monitoring: Continuous analysis of VPC flow logs, DNS logs, and CloudTrail events.
- Findings: Detailed alerts on potential threats with severity and remediation steps.
- Compliance: Supports regulatory requirements like GDPR and PCI-DSS.
- Threat Intelligence: Feeds of known-bad indicators used for detection.
