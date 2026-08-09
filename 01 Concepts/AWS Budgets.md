#AWS #Service #Concept
### AWS Budgets

AWS Budgets lets you set custom cost and usage budgets with alerts sent via email or SNS when thresholds are reached. Budgets cover cost, usage, reserved-instance coverage and utilization, and Savings Plans, enabling proactive spend management.

### How It Works
- Define a budget for a dollar amount or usage quantity, scoped to the whole account, a service, or resource tags.
- Set actual and forecasted thresholds; alerts fire when spend crosses each threshold.
- Notifications are delivered via email and [[SNS]] topics, and can trigger automated actions.
- Budgets are created and tracked from the AWS Billing and Cost Management console.

### Key Features
- Cost budgets for monthly, quarterly, or annual amounts.
- Usage budgets for dimensions like instance count or data transfer.
- Reserved Instance coverage and utilization budgets.
- Savings Plans utilization and coverage tracking.
- Forecast-based alerts that warn before a limit is exceeded.

### Common Use Cases
- Capping spend on development and test accounts.
- Alerting on cost anomalies or unexpected service usage.
- Enforcing budgets in multi-account setups via [[AWS Organizations]].
- Tracking commitment discounts to maximize utilization.

### Pricing & Limits
- The first two budgets are free; additional budgets are charged a nominal monthly fee.
- Budget data lags actual billing by a few hours, so alerts are near-real-time rather than instant.
- The number of budgets per account is limited, with the limit scaling to account needs.

### Related Services

- [[AWS Cost Explorer]]: Visualizes the spend budgets track.
- [[CloudWatch]]: Delivers budget alarm notifications.
- [[SNS]]: Routes budget alerts to email, SMS, or other endpoints.

### Related Concepts

- Cost Alerts: Notifications at defined thresholds.
- Usage Tracking: Monitoring resource consumption.
- [[AWS Pricing Models]]: Understanding what drives cost.
- [[AWS Free Tier]]: Setting budgets prevents surprise charges when free limits end.
