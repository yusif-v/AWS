#AWS #Service #Networking
### Security Groups vs NACLs

Security Groups are stateful virtual firewalls at the instance/ENI level, allowing only rules that permit traffic (no explicit deny). NACLs are stateless, subnet-level firewalls with numbered allow/deny rules evaluated in order. Both are used together for defense in depth.

### How It Works
- Security Groups act as a virtual firewall for an EC2 instance or ENI; you add allow rules for inbound and outbound traffic.
- Because they are stateful, return traffic is automatically permitted without explicit rules.
- Network ACLs are attached to subnets and evaluate all traffic entering or leaving the subnet; because they are stateless, return traffic must be allowed explicitly.
- NACL rules are numbered and evaluated in ascending order; the first matching rule is applied (allow or deny).
- Security Groups enforce at the instance level, while NACLs filter at the subnet boundary.

### Key Features
- Security Groups: allow rules only, can reference other security groups, no explicit deny, default denies all inbound and outbound.
- NACLs: support both allow and deny rules, number-based evaluation, default NACL allows all traffic.
- Security Groups use five-tuple rules (protocol, port, source/destination).
- NACLs can explicitly block specific IPs or ranges at the subnet edge.
- Both work together: SG for granular instance protection, NACL as a coarse subnet-level backstop.

### Common Use Cases
- Restricting instance access to specific ports (e.g., SSH 22, HTTPS 443) with Security Groups.
- Blocking a known malicious IP range at the subnet boundary with a NACL deny rule.
- Building a defense-in-depth perimeter: NACL at subnet level, Security Group at instance level.
- Managing stateless protocols where return traffic rules are controlled explicitly.

### Pricing & Limits
- Both Security Groups and NACLs are free features of VPC.
- Each security group can have up to 60 inbound and 60 outbound rules by default.
- Each NACL supports up to 20 rules per direction by default (increaseable).
- A security group can be attached to multiple instances; each ENI can have up to 5 security groups.

### Related Services
- [[VPC]]: The network layer hosting both.
- [[EC2]]: Security Groups attach to instances.
- [[NAT Gateway]]: Traffic subject to these controls.
- [[VPC Endpoints]]: Interface endpoints use security groups.
- [[CloudWatch]]: Analyzes flow data via VPC Flow Logs.

### Related Concepts
- Stateful vs Stateless: SG auto-allows return traffic; NACL does not.
- Default Deny: SG has no traffic until rules added.
- Rule Evaluation: NACL rules processed by number.
- Defense in Depth: Layering SG and NACL controls.
- VPC Flow Logs: Captures accepted/rejected traffic metadata.
