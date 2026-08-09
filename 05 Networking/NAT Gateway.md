#AWS #Service #Networking
### NAT Gateway

A NAT (Network Address Translation) Gateway enables instances in private subnets to access the internet (or AWS services) without receiving unsolicited inbound traffic. It is managed by AWS, scales automatically, and provides predictable outbound connectivity.

### Related Services

- [[VPC]]: The network where NAT Gateways live.
- [[Security Groups vs NACLs]]: The security layers applied around NAT.
- [[Route 53]]: Not directly related; use [[VPC]] routing instead.

### Related Concepts

- Private Subnet: No direct internet access.
- Outbound Only: Initiated connections only.
- Elastic IP: Stable source address.
