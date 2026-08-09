#AWS #Service #Analytics
### QuickSight

Fully managed business intelligence (BI) service for creating interactive dashboards and visualizations. Connects to AWS data sources (e.g., S3, RDS, Redshift) and external databases. Supports ad-hoc analysis, machine learning insights, and sharing with users. Pay-per-session pricing for scalable analytics.

### How It Works

- Authors create analyses and dashboards in a web-based interface.
- Data sources connect directly or via SPICE, an in-memory caching engine that accelerates query performance.
- SPICE imports data once and serves dashboard readers at sub-second speeds without re-querying source systems.
- Dashboards are shared with readers via the web or embedded into applications.
- Row-level security and IAM integration control who sees what.

### Key Features

- Interactive dashboards with drag-and-drop authoring.
- SPICE: Fast in-memory analytics for scalable performance.
- ML Insights: Anomaly detection, forecasting, and narrative summaries.
- Embedded analytics: Embed dashboards into apps with the QuickSight SDK/API.
- Native connectors to AWS services such as S3, RDS, Redshift, Athena, and OpenSearch.
- Pay-per-session pricing for dashboard readers.

### Common Use Cases

- Executive and operational dashboards across business teams.
- Ad-hoc exploratory analysis for analysts.
- Embedded BI inside customer-facing applications.
- Real-time monitoring dashboards from streaming sources.
- Forecasting and anomaly detection on business metrics.
- Sharing interactive reports with stakeholders.

### Pricing & Limits

- Authors billed per month per user; reader access is pay-per-session.
- SPICE capacity is billed per GB per month and can be increased as needed.
- Editions: Standard and Enterprise (Enterprise adds ML Insights, row-level security, and embedded analytics).
- No infrastructure to provision or manage.

### Related Services

- [[S3]]: Stores data for QuickSight analysis.
- [[RDS]]: Provides relational data for dashboards.
- [[Redshift]]: Integrates for large-scale data warehousing queries.
- [[Athena]]: Queries S3 data for QuickSight visualizations.
- [[IAM]]: Manages access to QuickSight dashboards and data sources.
- [[OpenSearch]]: Query source for log dashboards.

### Related Concepts

- Business Intelligence (BI): Transforms data into actionable insights via visualizations.
- Serverless Analytics: QuickSight requires no infrastructure management.
- SPICE Engine: In-memory engine for fast query performance.
- Embedded Analytics: Integrates dashboards into applications for end-user access.
- Row-Level Security: Restricts dashboard data per user.
