#AWS #Concept #Concept
### IaaS

Cloud computing model providing virtualized compute, storage, and networking resources over the internet. AWS delivers IaaS through services like EC2, allowing customers to rent infrastructure, manage operating systems, and deploy applications with flexibility and scalability, while AWS handles physical hardware and virtualization.

### How It Works
- AWS operates physical data centers, servers, storage, and networking hardware.
- Virtualization abstracts this hardware into on-demand virtual resources.
- Customers provision compute ([[EC2]]), storage ([[EBS]]), and network ([[VPC]]) through APIs.
- Customers retain control of the guest OS, runtime, and applications.

### Key Features
- Virtual machines with configurable CPU, memory, and storage.
- Block and object storage options.
- Virtual networking with subnets, routing, and security groups.
- Elastic scaling via [[Auto Scaling]] and load balancing with [[ELB]].
- Full control over the operating system and installed software.

### Common Use Cases
- Running traditional enterprise applications and legacy workloads.
- Hosting web servers, databases, and application tiers.
- Development and test environments that need flexible capacity.
- Lift-and-shift migrations that preserve the existing architecture.

### Pricing & Limits
- Billed by compute hours, storage, and data transfer; options include [[EC2 Pricing Models]].
- More management responsibility than PaaS or SaaS.
- Patching, hardening, and configuration are customer duties under [[Shared Responsibility Model]].

### Related Services

- [[EC2]]: Provides virtual servers for compute resources.
- [[EBS]]: Offers block storage for EC2 instances.
- [[VPC]]: Enables isolated network environments for IaaS resources.
- [[Auto Scaling]]: Adjusts IaaS resource capacity based on demand.
- [[CloudWatch]]: Monitors IaaS performance and metrics.

### Related Concepts

- Virtualization: Abstracts physical hardware into virtual resources.
- Scalability: Dynamically adjusts resources to meet workload needs.
- [[Shared Responsibility Model]]: AWS manages infrastructure; customers manage OS and applications.
- Pay-as-You-Go: Charges based on resource usage, no upfront costs.
- [[Cloud Computing Overview]]: IaaS is one of the three cloud service models.
