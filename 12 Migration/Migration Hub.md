#AWS #Service #Migration
### Migration Hub

Centralized service for tracking and managing application migrations to AWS. Provides a unified view of migration progress across tools like AWS Application Discovery Service, AWS Application Migration Service (MGN), and AWS Database Migration Service (DMS). Supports planning, monitoring, and managing migrations from on-premises or other clouds to AWS. Offers a single pane of glass for tracking migrations even when they span multiple tools and accounts.

### How It Works

- Discover applications on-premises using [[Application Discovery Service]] and import them into Migration Hub.
- Link discovered servers and databases to the migration tools used for each: [[MGN]] for servers, [[DMS]] for databases.
- Migration Hub aggregates status, progress, and metrics from those tools into a unified dashboard.
- Track application status through a defined **migration status** lifecycle from discovery to complete.
- Use Migration Hub to coordinate migration waves and report on overall portfolio health.

### Key Features

- Single dashboard for tracking all application migrations regardless of tool.
- Centralized application inventory from discovery and migration tools.
- Status and progress aggregation across [[MGN]], [[DMS]], and partner tools.
- Grouping of servers into applications for wave-based planning.
- Home region model for consolidating migration data and APIs.

### Common Use Cases

- Managing a large portfolio of applications through a phased migration.
- Coordinating server ([[MGN]]) and database ([[DMS]]) migrations for the same application.
- Reporting migration progress to stakeholders in one place.
- Tracking rehosted, replatformed, and refactored workloads side by side.

### Pricing & Limits

- No additional charge for Migration Hub itself; you pay for the underlying tools.
- Some features are free only when used through Migration Hub; others bill per the service.
- Available in specific home regions; data is aggregated into the home region you select.

### Related Services

- [[Application Discovery Service]]: Collects on-premises application data for migration planning.
- [[MGN]]: Automates server migrations, tracked in Migration Hub.
- [[DMS]]: Migrates databases, monitored via Migration Hub.
- [[CloudWatch]]: Tracks migration task performance and metrics.
- [[CloudFormation]]: Provisions resources for migrated applications.
- [[Migration Strategies]]: Defines the rehost/replatform/refactor choices tracked here.

### Related Concepts

- Migration Tracking: Centralizes status and metrics across migration tools.
- Application Portfolio: Organizes and assesses applications for cloud readiness.
- Hybrid Cloud Migration: Manages transitions from on-premises to AWS.
- Dependency Mapping: Visualizes application relationships to streamline migrations.
- Migration Wave: A group of applications migrated together in a controlled phase.
