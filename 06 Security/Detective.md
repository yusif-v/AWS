#AWS #Service #Security
### Detective

Managed security service for investigating potential security issues. Analyzes and visualizes data from AWS resources (e.g., CloudTrail logs, VPC Flow Logs, GuardDuty findings) to identify root causes, without data movement or code. Provides graphs, summaries, and insights for faster triage.

### How It Works

- Ingests and pre-processes security telemetry into a behavior graph.
- Correlates GuardDuty findings with historical activity and network data.
- Builds entity graphs showing users, resources, IP addresses, and their interactions.
- Requires no agents or code; data is copied into the graph for analysis.
- Investigators drill into timelines, summaries, and flagged events.

### Key Features

- Automatic, multi-account behavior graph in Security Hub-enabled environments.
- Visual investigation with entity pages and finding timelines.
- Summaries that surface root causes and related activity.
- One-click links between findings and the underlying evidence.
- No data retention or storage management on your side.

### Common Use Cases

- Triaging GuardDuty findings to confirm or dismiss a threat.
- Root-cause analysis of compromised credentials or instances.
- Investigating unusual network flows or API activity.
- Supporting incident response and post-incident forensics.

### Pricing & Limits

- Billed per GB of data processed into the behavior graph.
- Cost scales with the volume of analyzed telemetry.
- Requires GuardDuty or Security Hub enablement as a data source.

### Related Services

- [[GuardDuty]]: Generates findings analyzed by Detective.
- [[CloudTrail]]: Provides API logs for Detective investigations.
- [[VPC]]: Supplies flow logs for network analysis.
- AWS Security Hub: Centralizes findings for Detective integration.
- [[CloudWatch]]: Monitors metrics related to investigations.
- [[EventBridge]]: Streams findings for automated investigation workflows.

### Related Concepts

- Security Investigation: Automates root cause analysis of threats.
- Data Visualization: Graphs and timelines for issue exploration.
- Threat Detection: Aggregates data for anomaly identification.
- Compliance: Supports auditing and forensic analysis.
- Entity Graph: The relational model Detective builds for analysis.
