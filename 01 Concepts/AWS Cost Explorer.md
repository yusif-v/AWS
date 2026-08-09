#AWS #Service #Concept
### AWS Cost Explorer

AWS Cost Explorer provides interactive charts and reports for analyzing historical and forecasted AWS spend. It supports filtering by service, region, tag, and dimension, and includes a cost anomaly detection feature to surface unexpected charges.

### How It Works
- Cost Explorer ingests daily cost and usage data from the AWS billing pipeline.
- Users build queries across time ranges, groupings, and filters (service, region, AZ, linked account, tag).
- Results render as interactive charts and can be saved as reports for reuse.
- A forecasting model projects future spend from historical patterns, with configurable confidence intervals.

### Key Features
- Customizable dashboards and saved reports.
- Filtering and grouping by service, region, linked account, and cost allocation tags.
- Forecasts of monthly spend up to 12 months ahead.
- Cost anomaly detection that flags unusual spend and likely causes.
- Right-sizing recommendations and [[EC2 Pricing Models]] guidance.

### Common Use Cases
- Analyzing monthly bills to identify which services drive cost.
- Comparing spend across accounts or cost centers.
- Forecasting budget needs for the coming quarter.
- Detecting and investigating cost anomalies quickly.

### Pricing & Limits
- Cost Explorer is free to use; data is available within about 24 hours of activity.
- Data is retained for 13 months (current month plus 12 months of history).
- Forecasting is available for the upcoming 12 months.

### Related Services

- [[AWS Budgets]]: Sets alerts on the spend Cost Explorer tracks.
- [[AWS Organizations]]: Aggregates cost across accounts.
- [[AWS Pricing Models]]: Context for interpreting costs.

### Related Concepts

- Cost Anomaly Detection: Automated identification of unusual spend.
- Forecasting: Projecting future costs from history.
- [[Total Cost of Ownership]]: Long-term cost modeling beyond usage analysis.
