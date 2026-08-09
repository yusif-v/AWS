#AWS #Service #Management
### CloudWatch

Monitoring and observability service for AWS resources and applications. Collects metrics, logs, and events, providing dashboards, alarms, and insights for performance tracking and troubleshooting. Enables real-time monitoring, automated responses, and log analysis across AWS services. CloudWatch is the central pillar of observability in AWS.

### How It Works

- Services publish time-series **metrics** (CPU, network, request counts) to CloudWatch automatically, with more detailed metrics available for an extra fee.
- Logs are collected from EC2, Lambda, containers, and applications into log groups with configurable retention and encryption.
- Alarms watch a metric, evaluate it against a threshold over a period, and trigger actions such as SNS notifications or Auto Scaling events.
- Dashboards combine metrics and logs from many sources into a single custom view.
- CloudWatch Events (now EventBridge) routes state-change and schedule events to targets for automation.

### Key Features

- **Metrics & Alarms**: Unified metric storage, math, anomaly detection, and threshold-based alarms.
- **Logs & Logs Insights**: Collect, query, and analyze log data with a SQL-like query language.
- **Dashboards**: Custom widgets for a single pane of glass across services.
- **Contributor Insights**: Identify the top contributors to log patterns (e.g., error producers).
- **Synthetics Canaries**: Scheduled scripted checks that monitor endpoints and capture screenshots.
- **CloudWatch Agent**: Collects system-level metrics and logs from EC2 and on-premises servers.
- **Automated Actions**: Alarms can trigger Auto Scaling, SNS, EventBridge, and other automation.

### Common Use Cases

- Capacity planning and right-sizing by tracking CPU and memory utilization over time.
- Application troubleshooting by correlating metrics, logs, and alarms during an incident.
- Cost control — alarms that alert on spend anomalies or unusual usage.
- Compliance and auditing by centralizing application and audit logs with retention policies.
- Keeping services healthy by automatically scaling on load thresholds.

### Pricing & Limits

- Billed per metric, per log gigabyte ingested and stored, per alarm, and per dashboard; pricing varies by region.
- Basic monitoring is free (5-minute granularity); detailed monitoring (1-minute) is paid.
- Log data has configurable retention (default unlimited) and can be exported to S3 or archived to S3 Glacier.

### Related Services

- [[EC2]]: Monitors instance metrics like CPU and network usage.
- [[Lambda]]: Tracks function performance and invocation logs.
- [[S3]]: Logs bucket access and storage metrics.
- [[RDS]]: Monitors database performance and health.
- [[Auto Scaling]]: Uses CloudWatch metrics to trigger scaling actions.
- [[EventBridge]]: Consumes CloudWatch events for automation.
- [[SNS]]: Delivers alarm notifications.
- [[X-Ray]]: Provides traces that complement CloudWatch metrics and logs.
- [[ELB]]: Publishes load balancer metrics to CloudWatch.
- [[Step Functions]]: Automates workflows triggered by alarms.
- [[DynamoDB]]: Publishes table and index metrics.
- [[CloudTrail]]: Logs AWS account API activity, separate from application metrics.

### Related Concepts

- Metrics: Time-series data (e.g., CPU usage, request counts) for monitoring.
- Alarms: Automated notifications or actions based on metric thresholds.
- Logs Insights: Queries and analyzes log data for troubleshooting.
- Observability: Combines metrics, logs, and traces for full system visibility.
- Dashboards: Custom aggregated views of metrics and widgets.
- Log Groups & Retention: Organization and lifecycle of collected logs.
- Basic vs Detailed Monitoring: Granularity of EC2 metric collection.
