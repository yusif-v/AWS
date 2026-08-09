#AWS #Service #Compute
### Auto Scaling

AWS Auto Scaling maintains application availability by automatically adding or removing compute capacity to match demand. It spans EC2 Auto Scaling Groups, DynamoDB and Aurora capacity, and more, so you pay only for the resources you actually use.

### How It Works

- An Auto Scaling Group (ASG) defines a fleet of instances from a launch template (AMI, instance type, key pair, user data) with configured minimum, desired, and maximum sizes.
- The ASG continuously monitors instance health and replaces unhealthy instances to keep the fleet at the desired level.
- Scaling policies adjust capacity based on metrics such as CPU utilization, request counts, or custom CloudWatch alarms.
- Scaling activity is distributed across Availability Zones for fault tolerance, with an optional load balancer attached to route traffic.
- Predictive and scheduled scaling can anticipate demand patterns instead of reacting only after load changes.

### Key Features

- Dynamic scaling: target tracking, step scaling, and simple scaling policies respond to real-time metrics.
- Predictive scaling: machine-learning-based forecasts of future traffic reduce lag in capacity changes.
- Scheduled scaling: capacity changes at defined times for predictable workloads such as nightly batch or business hours.
- Fleet management: automatic health check replacement, instance refresh, and lifecycle hooks for graceful drains.
- Mixing On-Demand and Spot Instances via capacity rebalancing keeps cost low while preserving steady capacity.
- A single interface across EC2, ECS, DynamoDB, Aurora, and other services for scaling policy management.

### Common Use Cases

- Web and application fleets behind a load balancer that grow with traffic and shrink when idle.
- Cost optimization by diversifying into Spot capacity with capacity-optimized allocation.
- Maintaining minimum capacity for high availability even during zero traffic.
- Scheduled capacity for time-boxed workloads like reporting or trading windows.

### Pricing & Limits

- AWS Auto Scaling and EC2 Auto Scaling are free to use; you pay only for the underlying resources (EC2 instances, load balancers).
- Default quotas limit the number of Auto Scaling groups and launch configurations per region per account.
- Per-second billing applies to the On-Demand and Spot instances the group launches.

### Related Services

- [[EC2]]: The instances managed by Auto Scaling Groups.
- [[ELB]]: Distributes traffic across the scaled fleet.
- [[CloudWatch]]: Provides the metrics and alarms that drive scaling decisions.
- [[EC2 Pricing Models]]: How On-Demand, Reserved, and Spot capacity is billed.
- [[Compute Optimizer]]: Recommends right-sized instance configurations.
- [[ECS]]: Uses Auto Scaling capacity providers for container fleets.

### Related Concepts

- Elasticity: The ability to scale compute up and down with demand.
- Horizontal Scaling: Adding or removing instances to meet load.
- [[Regions & Availability Zones]]: Placement of the fleet across AZs for resilience.
- [[EC2 Instance Types]]: The instance sizes the group can launch.
