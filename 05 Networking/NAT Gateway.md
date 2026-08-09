#AWS #Service #Networking
### NAT Gateway

A NAT (Network Address Translation) Gateway enables instances in private subnets to access the internet (or AWS services) without receiving unsolicited inbound traffic. It is managed by AWS, scales automatically, and provides predictable outbound connectivity.

### How It Works
- A NAT Gateway sits in a public subnet with an Elastic IP and translates private instance addresses to its public address for outbound traffic.
- A route in the private subnet's route table points the default route (0.0.0.0/0) to the NAT Gateway.
- Return traffic is matched to the originating connection, but unsolicited inbound traffic is blocked.
- One NAT Gateway per Availability Zone provides redundancy; AWS recommends one per AZ in active use.

### Key Features
- Fully managed: no patching or instance management required.
- Automatic bandwidth scaling, starting at 5 Gbps and scaling up to 45 Gbps per gateway.
- Elastic IP-based stable source address for allowlisting.
- Supports up to 55,000 concurrent connections to a single destination.
- Integrates into the AWS network without needing a Security Group.
- Idle timeout of 350 seconds by default.

### Common Use Cases
- Private subnet internet access for software updates and package downloads.
- Outbound calls from databases or app servers to external APIs and services.
- Accessing public AWS services from private subnets where a VPC Endpoint is not used.
- Hybrid architectures that keep data-plane instances isolated.

### Pricing & Limits
- Billed per hour that the gateway exists plus per GB of data processed.
- No free tier; charges accrue even when idle.
- One NAT Gateway per AZ is typical; each supports one or more Elastic IPs.
- Compare with NAT instances (EC2-based) for legacy or special-case needs.

### Related Services
- [[VPC]]: The network where NAT Gateways live.
- [[Security Groups vs NACLs]]: The security layers applied around NAT.
- [[Route 53]]: Not directly related; use [[VPC]] routing instead.
- [[EC2]]: The instances that use the NAT Gateway.
- [[VPC Endpoints]]: Alternative private access to AWS services without NAT.
- [[Transit Gateway]]: Can route outbound traffic through centralized NAT.

### Related Concepts
- Private Subnet: No direct internet access.
- Outbound Only: Initiated connections only.
- Elastic IP: Stable source address.
- Internet Gateway: Required in the VPC for the NAT Gateway to reach the internet.
- NAT vs NAT Instance: Managed service versus EC2-based gateway.
