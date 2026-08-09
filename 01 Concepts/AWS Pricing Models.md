#AWS #Concept #Concept
### AWS Pricing Models

AWS offers flexible pricing including On-Demand, Reserved Instances, Savings Plans, and Spot. On-Demand is pay-per-use with no commitment; Reserved and Savings Plans trade upfront commitment for discounts; Spot provides steep discounts on unused capacity. Pricing varies by service and region.

### How It Works
- On-Demand charges per-second or per-hour usage with no upfront commitment or termination penalty.
- Reserved Instances and Savings Plans require a 1- or 3-year commitment in exchange for lower rates.
- Spot instances bid on unused EC2 capacity and can be reclaimed with short notice.
- Service-specific pricing adds data transfer, storage, and request-based charges on top of compute.

### Key Features
- Pay-as-you-go (On-Demand) for flexibility and variable workloads.
- Reserved capacity with Standard or Convertible RIs for predictable workloads.
- Savings Plans (Compute, EC2, SageMaker) that apply across eligible services.
- Spot capacity for cost-insensitive, interruptible workloads.
- Volume-based discounts and consolidated billing across [[AWS Organizations]] accounts.

### Common Use Cases
- Running steady-state production fleets on Reserved or Savings Plans.
- Handling spiky, short-lived jobs on Spot to cut costs dramatically.
- Keeping new or experimental workloads on On-Demand.
- Mixing models within an account to balance cost and reliability.

### Pricing & Limits
- Discounts depend on commitment term, payment option (all/partial/no upfront), and region.
- Spot pricing fluctuates with supply and demand; no SLA guarantees.
- [[AWS Cost Explorer]] and [[AWS Budgets]] help monitor and control effective rates.

### Related Services

- [[AWS Cost Explorer]]: Analyzes and forecasts spend.
- [[AWS Budgets]]: Sets thresholds and alerts on cost.
- [[AWS Free Tier]]: Free usage to get started.
- [[EC2 Pricing Models]]: Compute-specific pricing options.

### Related Concepts

- On-Demand: Pay for what you use, no commitment.
- Reserved/Savings Plans: Discounts for commitment.
- Spot: Variable pricing on spare capacity.
- [[Total Cost of Ownership]]: Comparing cloud vs on-premises cost.
