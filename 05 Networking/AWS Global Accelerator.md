#AWS #Service #Networking
### AWS Global Accelerator

AWS Global Accelerator improves application availability and performance by directing traffic through AWS edge locations to optimal regional endpoints. It provides static IP addresses, fast failover via health checks, and acceleration over the AWS global network.

### How It Works
- Uses two static anycast IP addresses assigned to your accelerator, giving clients worldwide a single entry point.
- Traffic enters at the closest edge location and travels over the AWS global backbone network to the optimal regional endpoint.
- Health checks continuously monitor endpoints; unhealthy endpoints cause traffic to shift to healthy alternatives in seconds.
- Routes to Application Load Balancers, Network Load Balancers, EC2 instances, and Elastic IPs across multiple regions.

### Key Features
- Static anycast IPs that stay constant, simplifying firewall allowlisting and client configuration.
- Traffic dials to control the percentage of traffic sent to each endpoint or region.
- Integration with Shield for DDoS protection at the edge.
- Global performance improvement: lower latency, jitter, and packet loss versus the public internet.
- Fast failover (sub-second detection) using continuous health checks.
- Supports both TCP and UDP traffic.

### Common Use Cases
- Global applications serving users across many regions (gaming, streaming, SaaS).
- Latency-sensitive workloads such as real-time communication and trading platforms.
- Disaster recovery and blue/green failover across regions.
- IoT device traffic that benefits from a stable, accelerated path.

### Pricing & Limits
- Billed hourly for each accelerator plus data transferred through it.
- Data transfer is priced per GB and varies by source region, using the premium network path.
- No setup fees; charges accrue only while the accelerator is running.

### Related Services
- [[ELB]]: Common endpoint behind the accelerator.
- [[CloudFront]]: CDN counterpart (caching vs network path).
- [[Edge Locations]]: PoPs that route traffic.
- [[Route 53]]: DNS with health-based routing complementary to the accelerator.
- [[Shield]]: DDoS protection at edge locations.
- [[Regions & Availability Zones]]: Regional endpoints selected by the accelerator.

### Related Concepts
- Static IPs: Fixed anycast addresses.
- Health-Based Routing: Automatic failover.
- Network Acceleration: Optimized global path.
- Anycast: Same IP advertised from many locations.
- Traffic Dials: Fine-grained control over traffic distribution.
