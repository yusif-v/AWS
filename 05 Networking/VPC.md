#AWS #Service #Networking
### VPC

Virtual Private Cloud (VPC) is a logically isolated section of the AWS cloud where you launch resources in a virtual network that you define. Gives full control over IP addressing, subnets, route tables, gateways, and security. It is the foundation of nearly every AWS networking architecture.

### How It Works
- A VPC is defined by a CIDR block (e.g., 10.0.0.0/16) and lives within a single region, spanning all of its Availability Zones.
- The VPC is divided into subnets, each assigned to one Availability Zone; route tables determine subnet traffic direction.
- An internet gateway enables public connectivity; subnets with a default route to the gateway are public, others are private.
- NAT Gateways provide outbound-only internet access from private subnets.
- Security Groups and Network ACLs filter traffic at the instance and subnet levels respectively.

### Key Features
- Full control over IP address ranges, including IPv4 and IPv6 support.
- Public and private subnets for separating internet-facing and internal resources.
- Route tables, network ACLs, and Security Groups for routing and filtering.
- VPC Flow Logs capture IP traffic metadata for monitoring and analysis.
- Elastic IPs provide stable public addresses; DHCP options and DNS settings are configurable.
- Integrates with Peering, Transit Gateway, VPN, and Direct Connect for expanded connectivity.

### Common Use Cases
- Hosting multi-tier applications with public web tiers and private data tiers.
- Building isolated environments for development, testing, and production.
- Hybrid networking connecting on-premises data centers to AWS.
- Hosting databases and internal services with no public exposure.
- Serverless workloads that use VPC-enabled Lambda functions.

### Pricing & Limits
- The VPC itself is free; you pay only for attached resources and data transfer.
- Default limits include 5 VPCs per region and 200 subnets per VPC (both increaseable).
- NAT Gateways, VPN connections, and inter-region peering carry separate charges.
- AWS Free Tier includes a limited monthly data transfer allowance.

### Related Services
- [[EC2]]: The most common workload hosted inside a VPC.
- [[Security Groups vs NACLs]]: The two layers of traffic filtering.
- [[NAT Gateway]]: Outbound internet access from private subnets.
- [[VPC Peering]]: Private connection between two VPCs.
- [[Transit Gateway]]: Hub-and-spoke routing across many VPCs.
- [[VPC Endpoints]]: Private access to AWS services.
- [[Direct Connect]]: Dedicated hybrid connectivity into the VPC.
- [[Regions & Availability Zones]]: The geographic and AZ model behind subnets.

### Related Concepts
- CIDR Blocks: IP ranges defining the VPC and its subnets.
- Public vs Private Subnets: Internet-facing versus isolated segments.
- Route Tables: Control where subnet traffic is sent.
- Internet Gateway: The gateway providing public internet access.
- Elastic IPs: Static public IP addresses.
- VPC Flow Logs: Capture traffic metadata for security and analysis.
