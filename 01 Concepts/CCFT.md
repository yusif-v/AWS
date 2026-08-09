#AWS #Service #Concept
### CCFT

Free tool in the AWS Billing Console providing a dashboard for estimating and tracking carbon emissions from AWS usage. Visualizes Scope 1 and Scope 2 emissions (per GHG Protocol) at 0.001 MTCO2e resolution, with breakdowns by service, Region, and time. Updated v2.0 methodology includes overhead allocation and renewable energy savings; data published monthly with 3-month lag.

### How It Works
- Aggregates electricity and fuel usage across AWS data centers attributable to customer workloads.
- Applies GHG Protocol accounting to classify Scope 1 and Scope 2 emissions.
- Reports with a monthly cadence and a roughly three-month data lag.
- v2.0 methodology adds overhead allocation and separates market-based vs location-based figures.

### Key Features
- Per-service and per-Region emission breakdowns.
- Scope 1 and Scope 2 reporting at 0.001 MTCO2e granularity.
- Carbon savings metric reflecting renewable energy purchases (market vs location-based).
- Historical trends and monthly comparisons for goal tracking.

### Common Use Cases
- Reporting emissions to customers or regulators.
- Setting and tracking cloud sustainability targets.
- Comparing carbon intensity across regions for workload placement.
- Combining cost and emissions data to optimize both.

### Pricing & Limits
- CCFT is free within the AWS Billing Console.
- Data is published monthly and lags by ~3 months.
- Reports cover service-level aggregates rather than individual resource-level metering.

### Related Services

- AWS Billing and Cost Management: Hosts the CCFT dashboard and reports.
- [[AWS Cost Explorer]]: Analyzes costs alongside emissions for optimization.
- [[CloudWatch]]: Monitors resource metrics contributing to emissions.
- AWS Sustainability: Provides broader sustainability insights and guidance.

### Related Concepts

- Scope 1 Emissions: Direct emissions from AWS-owned sources (e.g., fuel combustion).
- Scope 2 Emissions: Indirect emissions from purchased electricity, using market-based (MBM) or location-based (LBM) methods.
- Carbon Savings: Difference between LBM and MBM, reflecting renewable energy impact.
- Sustainability Reporting: Aligns with GHG Protocol for compliance and goal-setting.
- [[AWS Pricing Models]]: Cost signals used alongside carbon data for placement decisions.
