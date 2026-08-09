#AWS #Concept #Concept
### AWS Global Infrastructure

The physical footprint of AWS spanning regions, Availability Zones (AZs), and edge locations. Regions are independent geographic areas; each region contains multiple AZs, and edge locations cache content closer to users. This design supports high availability, disaster recovery, and low-latency delivery.

### How It Works
- Regions are independent geographic areas, each isolated from others to contain failures.
- Each region contains multiple AZs; AZs are clusters of data centers with independent power, networking, and cooling.
- AZs within a region are connected by low-latency, redundant fiber links.
- Edge locations and regional edge caches sit outside regions to accelerate content delivery and DNS resolution.

### Key Features
- Global coverage across many regions and dozens of edge locations worldwide.
- Data sovereignty and compliance via choosing specific regions.
- [[AWS Global Accelerator]] and [[CloudFront]] extend the footprint to the network edge.
- Private, high-bandwidth backbone interconnecting regions and AZs.

### Common Use Cases
- Deploying workloads across multiple AZs for fault tolerance.
- Replicating data across regions for disaster recovery.
- Serving content globally from edge locations to reduce latency.
- Meeting data residency and regulatory requirements by region selection.

### Pricing & Limits
- Infrastructure costs vary by region; some regions are more expensive than others.
- Data transfer between AZs and regions incurs charges.
- Not every service is available in every region.

### Related Services

- [[Regions & Availability Zones]]: The core building blocks of the global footprint.
- [[Edge Locations]]: PoPs that accelerate content delivery.
- [[CloudFront]]: CDN that uses edge locations.

### Related Concepts

- High Availability: Redundant infrastructure across AZs.
- Disaster Recovery: Region replication for resilience.
- Latency: Reduced by geographic distribution.
- [[Cloud Computing Overview]]: Cloud delivery depends on this global footprint.
