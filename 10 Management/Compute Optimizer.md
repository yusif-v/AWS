#AWS #Service #Management
### Compute Optimizer

AWS Compute Optimizer uses machine learning to recommend optimal EC2 instance types, Auto Scaling configurations, EBS volumes, and Lambda memory. Recommendations reduce cost while maintaining performance based on utilization history. It is an opt-in service that analyzes usage patterns over a lookback period to suggest right-sizing changes.

### How It Works

- After you opt in, Compute Optimizer reads utilization metrics from CloudWatch for EC2 instances, Auto Scaling groups, EBS volumes, Lambda functions, and ECS services on Fargate.
- Its machine-learning models evaluate usage history, hardware generation, and workload characteristics to score candidate resource configurations.
- Recommendations are ranked by potential cost savings and marked with confidence levels and reasons.
- You can review, filter, and apply suggestions, then track savings over time with recommendation history.
- Enhanced infrastructure metrics and external metric import can improve recommendation accuracy.

### Key Features

- **Right-Sizing Recommendations**: Instance type and size changes based on real utilization, not just CPU.
- **Multi-Workload Coverage**: Supports EC2, Auto Scaling groups, EBS volumes, Lambda memory, and Fargate.
- **Savings Estimates**: Projects monthly savings for each recommendation.
- **Confidence Scores & Reasons**: Helps prioritize which changes to apply.
- **Recommendation Preferences**: Exclude instance families or set performance-risk thresholds.
- **Suppression Rules**: Mute recommendations that are not actionable.

### Common Use Cases

- Continuously optimizing EC2 fleets to match actual workload demand.
- Reducing spend on over-provisioned EBS volumes by recommending smaller sizes or different volume types.
- Tuning Lambda memory settings to improve both cost and performance.
- Validating Auto Scaling group instance types as workloads change over time.

### Pricing & Limits

- The service itself is free to use for standard metrics; enabling enhanced infrastructure metrics or exporting custom metrics can incur CloudWatch charges.
- Recommendations require a sufficient lookback period of metric history to be generated.
- You must opt in per account and per region.

### Related Services

- [[EC2]]: Instance right-sizing recommendations.
- [[Auto Scaling]]: Configuration guidance.
- [[Trusted Advisor]]: Complementary cost checks.
- [[CloudWatch]]: Sources the utilization metrics used by the ML models.
- [[EBS]]: Volume type and size recommendations.
- [[Lambda]]: Memory configuration recommendations.
- [[EC2 Pricing Models]]: Informs purchase-option recommendations.
- [[AWS Cost Explorer]]: Cost analysis alongside recommendations.
- [[AWS Budgets]]: Set budgets against projected savings.

### Related Concepts

- Right-Sizing: Match resources to usage.
- Utilization Analysis: ML on CloudWatch metrics.
- Savings: Cost reduction recommendations.
- Opt-In Service: Must be enabled before analysis begins.
- Lookback Period: The historical window of metrics used for analysis.
- Recommendation History: Tracks applied recommendations and verified savings.
