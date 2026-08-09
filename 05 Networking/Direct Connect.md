#AWS #Service #Networking
### Direct Connect

Service providing a dedicated network connection from on-premises to AWS, bypassing the public internet. Offers consistent, low-latency, high-bandwidth connectivity (1 Gbps to 100 Gbps) for secure data transfer. Ideal for hybrid cloud, large data migrations, or latency-sensitive applications.

### How It Works
- A physical fiber connection is established between your data center and an AWS Direct Connect location (often via a colocation provider or partner).
- The connection terminates on AWS hardware and is mapped into virtual interfaces (VIFs) that attach to VPCs or AWS services.
- Private VIFs connect to VPCs; transit VIFs connect to a Transit Gateway or Direct Connect Gateway; public VIFs reach public AWS services.
- Traffic never traverses the public internet, providing consistent performance and reduced jitter.

### Key Features
- Dedicated bandwidth from 1 Gbps up to 100 Gbps, or lower-cost hosted connections from partners.
- Reduced data transfer costs: egress over Direct Connect is often cheaper than internet egress.
- MACsec encryption support for data in transit (IEEE 802.1AE).
- Link aggregation groups (LAGs) to scale bandwidth and add resilience.
- Private routing with BGP for dynamic route exchange.

### Common Use Cases
- Hybrid cloud networking connecting on-premises infrastructure to VPCs.
- Large-scale data migration and periodic bulk data transfer to S3 or databases.
- Latency-sensitive applications that cannot tolerate internet variability.
- Backups, disaster recovery, and database replication between sites.
- Centralized network management via Transit Gateway for many VPCs.

### Pricing & Limits
- Billed per port-hour for the dedicated connection plus data transfer out (egress).
- Data transfer pricing is lower than standard internet egress for most regions.
- Requires a physical connection at a Direct Connect location; a second connection is recommended for redundancy.
- No data transfer charge for inbound traffic over the connection.

### Related Services
- [[VPC]]: Connects to AWS resources via Direct Connect for private networking.
- AWS Transit Gateway: Simplifies routing between VPCs and Direct Connect.
- [[CloudWatch]]: Monitors Direct Connect performance and metrics.
- AWS VPN: Complements Direct Connect for encrypted, internet-based connections.
- [[S3]]: Transfers large datasets via Direct Connect.
- [[Transit Gateway]]: Hub for transit VIF connections to many VPCs.
- [[Route 53]]: Optional DNS integration for hybrid environments.

### Related Concepts
- Hybrid Cloud: Integrates on-premises infrastructure with AWS for seamless operations.
- Dedicated Connection: Physical link (e.g., fiber) for predictable performance.
- Virtual Interfaces (VIFs): Logical connections for public or private AWS services.
- Bandwidth Optimization: Reduces latency and jitter compared to internet-based transfers.
- BGP: Border Gateway Protocol used for route exchange over the connection.
