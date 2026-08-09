#AWS #Service #Compute
### Outposts

Hybrid cloud service that extends AWS infrastructure and services to on-premises data centers. Deploys fully managed racks with compute, storage, and networking, running services like EC2, EBS, and ECS locally. Ideal for low-latency, local data processing, or compliance needs, with seamless integration to AWS cloud.

### How It Works

- AWS installs and manages Outposts hardware (42U racks or 1U/2U servers) in your data center.
- The Outpost is connected to a parent AWS region, which provides the API, control plane, and management plane.
- You run services on Outposts using the same console, CLI, and APIs as in the region: EC2 instances, EBS volumes, ECS/EKS clusters, EMR, and more.
- Data stays local for low-latency access and data residency while still integrating with regional services.
- Local gateways control network connectivity, and AWS maintains the hardware.

### Key Features

- Runs a curated set of AWS services on-premises with a consistent experience.
- 42U rack and 1U/2U server form factors for different capacity and floor-space needs.
- EBS volumes with snapshot support; ECS/EKS for container workloads; EMR for data processing.
- Local data residency and low-latency processing without sacrificing AWS APIs.
- Connectivity to the parent region via Direct Connect or VPN with resilient network design.
- Hardware replacement and patching handled by AWS.

### Common Use Cases

- Workloads that must remain on-premises for latency, data residency, or compliance.
- Hybrid architectures spanning on-premises and regional AWS services.
- Local edge processing for factories, hospitals, retail, and telecom.
- Gradual migration of on-premises systems to AWS over time.

### Pricing & Limits

- You pay for the Outposts hardware (via purchase or monthly) plus usage of the services that run on it.
- Usage is billed like regional services, with data transfer between the Outpost and the parent region billed separately.
- Service availability on Outposts varies by service; check supported services for each form factor.

### Related Services

- [[EC2]]: Runs compute instances on Outposts hardware.
- [[EBS]]: Provides block storage for Outposts instances.
- [[ECS]]/[[EKS]]: Manages containerized workloads on Outposts.
- [[CloudFormation]]: Provisions and manages Outposts resources.
- [[CloudWatch]]: Monitors Outposts metrics and logs.
- [[Direct Connect]]: Dedicated connectivity to the parent region.
- [[S3]]: Object storage tiers available on Outposts.

### Related Concepts

- Hybrid Cloud: Combines on-premises and cloud environments for consistent operations.
- Local Data Processing: Supports low-latency or data residency requirements.
- AWS Regions Integration: Outposts connects to a parent AWS Region for management.
- Infrastructure as a Service (IaaS): Extends cloud-like infrastructure to on-premises.
- [[AWS Global Infrastructure]]: Extends regional services to on-premises locations.
