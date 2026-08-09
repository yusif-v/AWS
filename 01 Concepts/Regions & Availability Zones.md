#AWS #Concept #Concept
### Regions & Availability Zones

Regions are separate geographic areas containing two or more Availability Zones. AZs are isolated data centers within a region with independent power, networking, and cooling, connected by low-latency links. Deploying across AZs provides fault tolerance and high availability.

### Related Services

- [[EC2]]: Places instances in specific AZs.
- [[VPC]]: Spans AZs within a region.
- [[RDS Multi-AZ]]: Replicates databases across AZs.

### Related Concepts

- [[AWS Global Infrastructure]]: The overall physical layout.
- Fault Tolerance: Survives single-AZ failure.
- Low Latency: Data centers close to users.
