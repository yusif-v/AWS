#AWS #Concept #Concept
### Migration Strategies

Guides workload migration to AWS, optimizing speed, cost, and complexity.

### How It Works
- Workloads are assessed (via [[Application Discovery Service]]) to map dependencies and performance profiles.
- A target strategy is chosen per application based on business need, cost, and risk.
- Migration tools automate data and server transfer ([[MGN]], [[DMS]], [[DataSync]]).
- Post-migration validation confirms functionality and performance, then legacy systems are decommissioned.

### The 7 R's
- **Rehost**: Move workloads as-is to AWS (e.g., via [[MGN]]).
- **Replatform**: Migrate with optimizations (e.g., use [[RDS]]).
- **Refactor**: Rebuild for cloud-native (e.g., target [[Aurora]]).
- **Repurchase**: Switch to AWS solutions (e.g., [[QuickSight]]).
- **Retire**: Eliminate obsolete workloads.
- **Retain**: Keep workloads on-premises for now.
- **Relocate**: Transfer entire environments (e.g., to [[Outposts]]).

### Key Features
- Portfolio discovery and dependency mapping before migration.
- Automated server and database migration with minimal downtime.
- Application modernization options from lift-and-shift to full refactor.
- Central tracking of the migration wave via [[Migration Hub]].

### Common Use Cases
- Data center exits moving hundreds of servers to AWS.
- Modernizing a legacy database to a managed service.
- Consolidating or retiring redundant applications during migration.
- Phasing migrations by business priority and risk.

### Pricing & Limits
- Tools like [[MGN]] and [[DMS]] charge per source-server or per data volume.
- Strategy choice drives cost: rehost is fast but retains legacy footprint; refactor is cheaper to run long-term.
- Pilot migrations help validate cost and performance before scaling.

### Related Services

- [[Migration Hub]]: Tracks migration progress across tools.
- [[MGN]]: Automates rehost migrations.
- [[DMS]]: Handles database migrations.
- [[Application Discovery Service]]: Maps on-premises applications.
- [[CloudFormation]]: Sets up migration infrastructure.
- [[CloudWatch]]: Monitors migration performance.

### Related Concepts

- Lift-and-Shift: Fast migration with no changes (Rehost).
- Cloud-Native: Optimize for AWS (Refactor).
- Migration Tracking: Unified view via [[Migration Hub]].
- Dependency Mapping: Plans migrations with application relationships.
- [[CAF]]: Provides the overall methodology that migration strategies fit within.
- [[Total Cost of Ownership]]: Justifies migration with long-term cost comparison.
