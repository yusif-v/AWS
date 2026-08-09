#AWS #Service #Compute
### EC2

Resizable virtual servers in the cloud for running applications and workloads. Choose from a wide range of instance types tuned for compute, memory, storage, and accelerated computing. Scales capacity up or down on demand and charges pay-as-you-go, with flexible pricing options for different usage patterns.

### How It Works

- You launch an instance by pairing an AMI (OS template) with an instance type (CPU/memory sizing) inside a VPC subnet.
- Each instance runs on virtualized or bare-metal hardware with EBS or instance store storage, key-pair SSH access, and security group filtering.
- Elastic IPs, user data scripts, IAM instance profiles, and placement groups control networking, boot-time configuration, and availability behavior.
- Instances can be stopped, started, rebooted, resized (for most types), snapshotted, and terminated; EBS-backed instances persist data across stops.
- Auto Scaling Groups and load balancers manage fleets of instances for scale and high availability.

### Key Features

- Deep instance-type catalog across Intel, AMD, and Arm (Graviton) covering general purpose, compute, memory, storage, accelerated, and HPC families.
- Elastic Block Store snapshots, fast snapshot restore, and data lifecycle management.
- Integration with VPC, Security Groups, IAM roles, CloudWatch, Systems Manager, and CloudTrail.
- Placement groups for low latency (cluster), high availability (spread), and partition isolation.
- Hibernate, Elastic IPs, and instance scaling for cost and flexibility control.
- The Nitro System underpins modern instance types with hardware acceleration, security, and consistent performance.

### Instance Types

- [[EC2 Instance Types]]: Families optimized for different workloads.
- [[EC2 Pricing Models]]: On-Demand, Reserved, Spot, and Savings Plans.

### AMIs & Storage

- [[EC2 AMIs]]: Pre-configured machine images for launching instances.
- [[EC2 Storage]]: EBS volumes and instance store options.

### Common Use Cases

- Traditional and cloud-native application servers, web servers, and databases.
- Container hosts for ECS and EKS worker fleets.
- Machine learning training and inference on GPU and Inferentia/Trainium instances.
- Batch, rendering, and high-performance computing workloads.
- Lift-and-shift migration of on-premises servers with broad OS and architecture support.

### Pricing & Limits

- Pay-as-you-go On-Demand per second; Reserved Instances and Savings Plans for committed discounts; Spot for interruptible capacity.
- Free tier includes 750 hours per month of eligible general purpose instances for 12 months.
- Billing stops when instances are stopped or terminated; unused reserved capacity can still be billed.
- Regional quotas cap vCPU limits by default and can be raised via a support request.
- EC2 provides a 99.99% availability SLA for instances running in multiple Availability Zones.

### Related Services

- [[Auto Scaling]]: Automatically adjusts instance counts.
- [[ELB]]: Distributes traffic across instances.
- [[EBS]], [[EFS]], [[S3]]: Block, file, and object storage for instances.
- [[CloudWatch]]: Metrics, alarms, and log collection.
- [[AWS Global Infrastructure]]: Regions and Availability Zones where instances run.
- [[Compute Optimizer]]: Recommends right-sizing.

### Related Concepts

- [[IaaS]]: Virtualized compute as a service.
- [[Shared Responsibility Model]]: AWS secures the host; you secure the guest OS and apps.
- [[Regions & Availability Zones]]: Placement options for resilience and latency.
- [[Security Groups vs NACLs]]: Instance-level and subnet-level traffic filtering.
- [[EC2 Pricing Models]]: How usage is billed.
