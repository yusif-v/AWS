#AWS #Concept #Concept
### Regions & Availability Zones

Regions are separate geographic areas containing two or more Availability Zones. AZs are isolated data centers within a region with independent power, networking, and cooling, connected by low-latency links. Deploying across AZs provides fault tolerance and high availability.

### How It Works
- A region is a self-contained geographic area isolated from other regions for failure containment.
- Each region contains multiple AZs; each AZ has independent power, networking, and cooling.
- AZs in a region connect over low-latency, redundant fiber, enabling synchronous replication.
- Selecting a region governs data residency, latency, and available services.

### Key Features
- Multi-AZ redundancy for high availability within a region.
- Regional isolation to support disaster recovery across regions.
- Low-latency connectivity between AZs for replication and clustering.
- Data residency control for compliance and regulatory requirements.

### Common Use Cases
- Deploying production applications across two or more AZs.
- Using [[RDS Multi-AZ]] or [[ELB]] to survive AZ failures.
- Replicating data to another region for disaster recovery.
- Placing workloads in regions near users to reduce latency.

### Pricing & Limits
- Cross-AZ traffic within a region is charged; cross-region traffic costs more.
- Pricing varies by region; services may be unavailable in some regions.
- AZs are physically separate; a region guarantees at least two AZs.

### Related Services

- [[EC2]]: Places instances in specific AZs.
- [[VPC]]: Spans AZs within a region.
- [[RDS Multi-AZ]]: Replicates databases across AZs.
- [[ELB]]: Distributes traffic across AZs for resilience.

### Related Concepts

- [[AWS Global Infrastructure]]: The overall physical layout.
- Fault Tolerance: Survives single-AZ failure.
- Low Latency: Data centers close to users.
- [[Shared Responsibility Model]]: AWS maintains the physical AZ infrastructure.
