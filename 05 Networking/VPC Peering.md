#AWS #Service #Networking
### VPC Peering

VPC Peering connects two VPCs via a private, encrypted route so they can communicate as if on the same network. Peering is not transitive (no A to B to C), does not require a gateway, and can connect VPCs across accounts or regions.

### How It Works
- A peering connection is requested by one VPC owner and accepted by the other; both VPCs must be in compatible regions.
- Route table entries in both VPCs point the peer's CIDR range to the peering connection.
- Traffic flows directly between the two VPCs using private IPs, never through a gateway or VPN.
- Works within a single account, across accounts, and across regions (inter-region peering).
- DNS resolution can be enabled for the peered VPCs to resolve private hostnames.

### Key Features
- Private, low-latency connectivity with no single point of failure.
- No bandwidth limit and no gateway hardware to manage.
- Cross-account and cross-region support.
- Traffic stays within the AWS network, keeping the public internet out of the path.
- No additional charge for the peering connection itself (data transfer rates apply).

### Common Use Cases
- Sharing services between a few VPCs (e.g., a shared database or Active Directory).
- Connecting application VPCs to a central services VPC within an account.
- Inter-region peering for disaster recovery and failover.
- Mergers/acquisitions connecting separate AWS environments.

### Pricing & Limits
- The peering connection itself is free; data transfer is billed (inter-region peering uses inter-region data rates).
- Peered VPCs cannot have overlapping CIDR blocks.
- Peering is not transitive; each pair of VPCs needs its own peering connection.
- For many VPCs, a Transit Gateway reduces connection and cost complexity.

### Related Services
- [[VPC]]: The networks being connected.
- [[Transit Gateway]]: Hub-and-spoke alternative for many VPCs.
- [[Route 53]]: Optional DNS integration.
- [[VPC Endpoints]]: Private access to AWS services from peered VPCs.
- [[Direct Connect]]: On-premises connectivity to peered VPCs.

### Related Concepts
- Non-Transitive: A-B peering does not reach C.
- Private Connectivity: No internet exposure.
- CIDR Overlap: Cannot peer overlapping ranges.
- Route Tables: Must be updated in both VPCs.
- Inter-Region Peering: Extends VPC Peering across regions.
