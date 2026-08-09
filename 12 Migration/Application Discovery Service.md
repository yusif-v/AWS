#AWS #Service #Migration
### Application Discovery Service

Service for collecting and analyzing data about on-premises applications and infrastructure to plan cloud migrations. Discovers servers, dependencies, and performance metrics, storing data in a centralized repository. Helps identify workloads for migration to AWS. Supports both agent-based and agentless discovery so nearly any on-premises environment can be surveyed before a single server is moved.

### How It Works

- Runs **agentless** discovery (via VMware vCenter / Hyper-V integration) or **agent-based** discovery (installing the AWS Agent on each host) to capture server inventory.
- Collects configuration, utilization, and performance data such as CPU, memory, disk, and network usage over time.
- Maps **dependencies** between servers and applications so related workloads can be planned and migrated together.
- Stores findings in a centralized data store that feeds into [[Migration Hub]] and the migration assessment tools.
- Exports data to [[S3]] for offline analysis, custom reports, or further processing.

### Key Features

- Agentless and agent-based discovery modes for heterogeneous on-premises environments.
- Continuous data collection that builds a utilization profile over weeks, not a one-time snapshot.
- Network and process dependency mapping to understand inter-service communication.
- Centralized repository shared with other migration services and assessment tools.
- Export capability for feeding downstream planning and cost estimation.

### Common Use Cases

- Building an accurate application portfolio before committing to a migration plan.
- Identifying which workloads are safe to rehost, replatform, or retire.
- Right-sizing EC2 instances based on real utilization rather than peak assumptions.
- Planning migration wave order by understanding dependencies between applications.

### Pricing & Limits

- Billed per hour per discovered server plus per-server per-hour for the agent-based mode.
- No upfront cost or minimum usage; pay only for what you discover.
- Data is retained in the discovery data store so it can be reused for planning and reassessment.

### Related Services

- [[Migration Hub]]: Centralizes discovery data and tracks migration progress.
- [[EC2]]: Target for migrating discovered applications.
- AWS Systems Manager: Integrates for agent-based discovery and management.
- [[S3]]: Stores discovery data exports.
- [[DMS]]: Migrates databases identified during discovery.
- [[MGN]]: Replicates and cuts over the servers discovered during planning.
- [[SCT]]: Converts schemas for databases flagged by discovery.
- [[Migration Strategies]]: Frames how discovery data informs each of the 7 Rs.

### Related Concepts

- Application Discovery: Maps on-premises workloads, dependencies, and resource usage.
- Migration Planning: Uses discovery data to design AWS migration strategies.
- Agent-Based vs. Agentless Discovery: Options for collecting data with or without software installation.
- Dependency Mapping: Identifies relationships between applications and infrastructure.
- Right-Sizing: Matches discovered utilization to the appropriate EC2 instance family.
- Total Cost of Ownership: Uses discovery telemetry to model TCO in the cloud.
