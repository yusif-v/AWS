#AWS #Service #Networking
### Security Groups vs NACLs

Security Groups are stateful virtual firewalls at the instance/ENI level, allowing only rules that permit traffic (no explicit deny). NACLs are stateless, subnet-level firewalls with numbered allow/deny rules evaluated in order. Both are used together for defense in depth.

### Related Services

- [[VPC]]: The network layer hosting both.
- [[EC2]]: Security Groups attach to instances.
- [[NAT Gateway]]: Traffic subject to these controls.

### Related Concepts

- Stateful vs Stateless: SG auto-allows return traffic; NACL does not.
- Default Deny: SG has no traffic until rules added.
- Rule Evaluation: NACL rules processed by number.
