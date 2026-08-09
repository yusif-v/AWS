#AWS #Service #Compute
### EC2 Pricing Models

EC2 offers On-Demand (pay per second, no commitment), Reserved Instances (discount for 1- or 3-year commitment), Savings Plans (flexible usage-based discounts), Spot Instances (steeply discounted spare capacity), and Dedicated Hosts. Choosing the right model balances cost and flexibility.

### How It Works

- On-Demand charges for compute time with no upfront payment or commitment; ideal for unpredictable or short-lived workloads.
- Reserved Instances (RIs) lock in capacity and price for 1 or 3 years, with Standard (firm) and Convertible (flexible) classes.
- Savings Plans offer a discount in exchange for a consistent hourly spend commitment over 1 or 3 years across Compute or EC2 usage.
- Spot Instances use idle AWS capacity at a steep discount; AWS can reclaim them with a short warning.
- Dedicated Hosts and Dedicated Instances isolate capacity on dedicated physical hardware for licensing compliance.

### Key Features

- Per-second billing for most On-Demand and Reserved Linux instances reduces costs for short runs.
- EC2 Savings Plans cover instance usage across families and regions with automatic instance-size flexibility.
- Spot capacity is interruptible but cost-effective for fault-tolerant, stateless workloads; diversifying across capacity pools reduces risk.
- Reserved Instance Marketplace allows resale of unused reservations.
- Combining an On-Demand baseline with Spot overflow optimizes both cost and availability.

### Common Use Cases

- Steady-state production fleets: Reserved Instances or Savings Plans for predictable discounts.
- Fault-tolerant and batch workloads: Spot for the lowest cost.
- Unknown or spiky demand: On-Demand for full flexibility.
- Compliance and licensing: Dedicated Hosts for bring-your-own-license (BYOL).

### Pricing & Limits

- Pricing varies by instance family, region, and commitment term; check the pricing page for exact figures.
- Spot prices fluctuate with supply and demand across pools; capacity-optimized allocation minimizes interruption.
- AWS Cost Explorer, AWS Budgets, and Compute Optimizer help monitor and right-size usage.

### Related Services

- [[EC2]]: The compute service these models price.
- [[AWS Pricing Models]]: General AWS pricing concepts.
- [[Auto Scaling]]: Uses spot and on-demand capacity.
- [[AWS Cost Explorer]]: Analyzes and forecasts EC2 spend.
- [[AWS Budgets]]: Alerts on cost thresholds.
- [[Compute Optimizer]]: Recommends type and pricing changes.

### Related Concepts

- On-Demand: Flexible, no commitment.
- Spot: Interruptible, low-cost capacity.
- Reserved/Savings Plans: Commitment for discounts.
- [[Total Cost of Ownership]]: Comparing on-premises versus cloud cost.
