#AWS #Service #Networking
### Transit Gateway

AWS Transit Gateway is a hub-and-spoke network router that connects VPCs, VPNs, and Direct Connect attachments in one place. It supports transitive routing across many VPCs, simplifies network architecture, and centralizes route management.

### How It Works
- Acts as a regional hub; each VPC, VPN, or Direct Connect connection is an attachment to the gateway.
- Route tables are associated with attachments, with route propagation enabled to share routes between attachments.
- Traffic between any two attachments traverses the hub, enabling transitive routing (A to C via the hub).
- Inter-region peering between Transit Gateways extends connectivity across regions.
- Supports centralized egress and security inspection via a dedicated appliance VPC.

### Key Features
- Scales to thousands of VPCs and attachments, replacing complex VPC peering meshes.
- Centralized route management with per-attachment route tables and propagation.
- Network segmentation using route tables to isolate environments.
- Inter-region Transit Gateway peering for global connectivity.
- Support for multicast within the transit network.
- Integrates with VPN and Direct Connect (transit VIF) for hybrid connectivity.

### Common Use Cases
- Connecting many VPCs in one or more regions without a full mesh of peerings.
- Centralized internet egress, inspection, and firewall placement via an inspection VPC.
- Hybrid connectivity combining Direct Connect and VPN into one hub.
- Isolating development, test, and production VPCs with separate route tables.
- Multi-account architectures using shared Transit Gateways.

### Pricing & Limits
- Billed per attachment per hour plus data processing charges per GB.
- Inter-region peering incurs additional data transfer charges.
- High default attachment limits that can be increased on request.
- No charge for the gateway itself, only attachments and data processed.

### Related Services
- [[VPC]]: Spokes attached to the transit hub.
- [[Direct Connect]]: On-premises connectivity into the hub.
- [[VPC Peering]]: Mesh alternative for small numbers of VPCs.
- [[NAT Gateway]]: Centralized outbound egress through a hub.
- [[VPC Endpoints]]: Private service access from spoke VPCs.
- [[AWS Global Accelerator]]: Can route to endpoints within a hub network.

### Related Concepts
- Hub-and-Spoke: Central router model.
- Route Tables: Per-attachment routing.
- Transitive Routing: Traffic flows between spokes via the hub.
- Attachments: VPC, VPN, and Direct Connect connections to the gateway.
- Route Propagation: Automatically shares routes between attachments.
