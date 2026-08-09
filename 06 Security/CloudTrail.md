#AWS #Service #Security
### CloudTrail

AWS CloudTrail records API activity across your AWS account, producing an auditable history of who did what, when, and from where. It is the primary source of audit, governance, and operational data for security analysis and incident investigation in AWS.

### How It Works

- Captures management events (control plane) such as IAM, EC2, and S3 configuration changes.
- Can capture data events (e.g., S3 object-level activity, Lambda invocations) when enabled.
- Delivers log files as JSON to an S3 bucket and can stream events to CloudWatch Logs.
- Trails can be single-region, multi-region, or organization-wide.
- Events include caller identity, source IP, timestamp, service, and the API action.

### Key Features

- Multi-region and organization-wide trails via AWS Organizations.
- Log file integrity validation using SHA-256 hashing and chain-of-custody.
- Event history: 90 days of free, searchable recent activity in the console.
- Optional delivery to CloudWatch Logs and EventBridge for real-time alerting.
- Integration with Athena for querying historical activity at scale.

### Common Use Cases

- Security auditing and forensic investigation after a security event.
- Detecting unauthorized access or privilege escalation attempts.
- Supporting compliance (SOC, PCI DSS, HIPAA) with durable activity logs.
- Troubleshooting by correlating API calls with resource behavior.

### Pricing & Limits

- Management event trails are free for the first copy in each region.
- Data events and additional copies are billed per 100,000 events.
- Retention is customer-controlled via S3 object lock or a dedicated log bucket.
- CloudTrail Lake offers a managed, queryable event store at additional cost.

### Related Services

- [[Config]]: Tracks configuration state changes alongside CloudTrail activity logs.
- [[GuardDuty]]: Analyzes CloudTrail events for malicious API activity.
- [[Detective]]: Uses CloudTrail logs for root-cause investigations.
- [[CloudWatch]]: Receives CloudTrail events for monitoring and alerting.
- [[EventBridge]]: Routes CloudTrail events to automation targets.
- [[S3]]: Stores the delivered CloudTrail log files.
- [[IAM]]: The source of many audited API actions; IAM controls trail access.

### Related Concepts

- API Activity Logging: Recording every control-plane call for accountability.
- Management vs Data Events: Control-plane vs resource-level activity granularity.
- Audit Trail: The durable, ordered record CloudTrail produces.
- Shared Responsibility Model: AWS logs its actions; customers log and monitor theirs.
