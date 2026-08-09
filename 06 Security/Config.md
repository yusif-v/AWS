#AWS #Service #Security
### Config

Service for tracking and auditing AWS resource configurations and compliance. Records resource changes, relationships, and histories, enabling evaluation against desired configurations. Supports compliance monitoring, change management, and troubleshooting with detailed resource timelines.

### How It Works

- Continuously records configuration items for supported AWS resources.
- Evaluates resources against AWS managed rules or custom Lambda-backed rules.
- Tracks resource relationships to understand configuration dependencies.
- Delivers configuration snapshots and change history to an S3 bucket.
- Triggers notifications via SNS or EventBridge when resources change.

### Key Features

- Config Rules for automated compliance evaluation.
- Conformance packs to manage rules across accounts and regions.
- Configuration history and change timelines for every tracked resource.
- Multi-account, multi-region aggregation.
- Resource inventory with relationship graphing.

### Common Use Cases

- Enforcing tagging policies and resource standards.
- Detecting configuration drift from a desired state.
- Auditing against internal or regulatory compliance baselines.
- Troubleshooting by seeing when and how a resource changed.
- Continuous compliance reporting integrated with Security Hub.

### Pricing & Limits

- Charged per configuration item recorded and per rule evaluation.
- Some managed rules and the first 100,000 configuration items are covered by free tier.
- Costs scale with resource count and rule evaluation frequency.

### Related Services

- [[CloudTrail]]: Logs API activity, complementing Config’s resource tracking.
- [[CloudWatch]]: Monitors Config rules and triggers alerts for non-compliance.
- [[Lambda]]: Automates responses to configuration changes detected by Config.
- [[IAM]]: Manages access to Config data and rules.
- [[S3]]: Stores Config snapshots and change histories.
- [[Security Hub]]: Aggregates Config-based compliance checks across accounts.
- [[AWS Organizations]]: Enables multi-account Config aggregation and conformance packs.

### Related Concepts

- Configuration Management: Tracks resource states to ensure consistency and compliance.
- Compliance Auditing: Evaluates resources against predefined rules or standards.
- Resource Inventory: Maintains a detailed catalog of AWS resources and relationships.
- Change Tracking: Captures configuration changes for auditing and rollback.
- Configuration Drift: Divergence between actual and desired resource state.
