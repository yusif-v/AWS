#AWS #Service #Networking
### VPC Peering

VPC Peering connects two VPCs via a private, encrypted route so they can communicate as if on the same network. Peering is not transitive (no A→B→C), does not require a gateway, and can connect VPCs across accounts or regions.

### Related Services

- [[VPC]]: The networks being connected.
- [[Transit Gateway]]: Hub-and-spoke alternative for many VPCs.
- [[Route 53]]: Optional DNS integration.

### Related Concepts

- Non-Transitive: A-B peering does not reach C.
- Private Connectivity: No internet exposure.
- CIDR Overlap: Cannot peer overlapping ranges.
