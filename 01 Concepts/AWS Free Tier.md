#AWS #Concept #Concept
### AWS Free Tier

AWS Free Tier provides free usage tiers to explore services: always-free services (e.g., certain Lambda requests, DynamoDB capacity), 12-month free services (e.g., 750 EC2 hours/month), and short-term trial offers. It is a way to learn and prototype without incurring costs.

### How It Works
- Each new account receives free-tier eligibility that starts at account creation.
- Always-free allowances (e.g., a monthly volume of Lambda requests and DynamoDB capacity) continue as long as the account exists.
- 12-month offers (e.g., 750 hours of eligible EC2 instances per month, EBS, S3) expire one year after signup.
- Short-term trials grant a fixed credit window for services like SageMaker or RDS.

### Key Features
- Three categories: always free, 12-month free, and limited-time trials.
- Covers foundational services including [[EC2]], [[S3]], [[Lambda]], [[DynamoDB]], and [[RDS]].
- Monitor usage in the AWS Free Tier dashboard to avoid surprise bills.
- Good for certifications, labs, and proof-of-concept projects.

### Common Use Cases
- Learning AWS with hands-on labs for exams like the Cloud Practitioner.
- Prototyping applications before committing to paid capacity.
- Testing migration or architecture ideas at no cost.

### Pricing & Limits
- Free within defined limits; exceeding them incurs standard on-demand charges.
- Unused free-tier allowances do not roll over month to month.
- Free tier applies per account, not per user, and is easiest to track with [[AWS Budgets]].

### Related Services

- [[AWS Budgets]]: Prevents surprise charges after free limits.
- [[EC2]]: Included in the 12-month free tier.
- [[Lambda]]: Always-free tier with monthly request allowance.
- [[S3]]: Always-free tier for a limited amount of standard storage.

### Related Concepts

- [[AWS Pricing Models]]: Understanding when free tiers end.
- Cost Control: Monitoring usage to stay within limits.
- [[AWS Account & Root User]]: Free tier is applied at the account level.
