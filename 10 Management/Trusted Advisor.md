#AWS #Service #Management
### Trusted Advisor

AWS Trusted Advisor inspects your environment against best practices for cost optimization, performance, security, fault tolerance, and service limits. Checks range from S3 bucket permissions to unused resources; core checks are free, with full checks on paid support plans. It gives prioritized, actionable recommendations in the console and via the AWS Support API.

### How It Works

- Trusted Advisor evaluates the account's live configuration against a library of best-practice checks across five categories.
- Each check returns a status of green (no issue), yellow (attention), or red (action recommended), with a priority ordering.
- Checks inspect resources such as S3 buckets, IAM users, EBS snapshots, EC2 instances, and service quotas in supported regions.
- Full check access depends on the active AWS Support Plan — core checks are available to all, advanced checks to Business and Enterprise support.
- Findings can be refreshed on demand and exported through the console or the AWS Support API.

### Key Features

- **Cost Optimization**: Detects idle or underutilized resources, underutilized EBS volumes, and over-provisioned RDS instances.
- **Security Checks**: Flags publicly accessible S3 buckets, MFA not enabled on root accounts, and security group issues.
- **Fault Tolerance**: Surfaces missing multi-AZ deployments, unprotected EC2 instances, and stale EBS snapshots.
- **Performance**: Identifies under-provisioned or misconfigured resources, such as high-utilization EBS volumes.
- **Service Limits**: Alerts when usage is approaching service quotas in the current region.
- **Priority Status & History**: Green/yellow/red triage plus a log of previous checks.

### Common Use Cases

- Running a periodic cost review to find idle resources and potential savings.
- Auditing for common security misconfigurations such as open S3 buckets or missing root MFA.
- Preparing for AWS Well-Architected reviews with a preliminary scan.
- Tracking approaching service limits before they block launches.

### Pricing & Limits

- Core Trusted Advisor checks are free for all accounts.
- Full check set and priority access are included with Business, Enterprise On-Ramp, and Enterprise Support plans.
- Some checks run only in supported regions, and refresh is limited on basic plans.

### Related Services

- [[AWS Support Plans]]: Defines which checks are available.
- [[Security Hub]]: Broader security posture checks.
- [[Compute Optimizer]]: Deeper cost recommendations.
- [[S3]]: Bucket permission and access checks.
- [[IAM]]: Root MFA and user configuration checks.
- [[EBS]]: Snapshot and under-utilization checks.
- [[EC2]]: Idle and under-utilized instance checks.
- [[AWS Organizations]]: Checks that can span the organization.
- [[CloudWatch]]: Utilized metrics that inform cost checks.
- [[AWS Well-Architected Tool]]: Structured review companion.
- [[Well-Architected Framework]]: The principles behind many checks.
- [[Total Cost of Ownership]]: Context for cost optimization recommendations.

### Related Concepts

- Best Practices: Automated checks across categories.
- Service Limits: Alerts on approaching quotas.
- Core Checks: Free subset for all accounts.
- Five Check Categories: Cost optimization, performance, security, fault tolerance, and service limits.
- Priority Status: Red/yellow/green triage of recommendations.
- AWS Support API: Programmatic access to check results.
