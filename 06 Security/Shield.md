#AWS #Service #Security
### Shield

Managed DDoS protection service safeguarding AWS applications. Includes **Shield Standard** (free, automatic protection against common Layer 3/4 attacks for all AWS customers) and **Shield Advanced** (paid, with enhanced mitigation, 24/7 DDoS Response Team, cost protection, and Layer 7 filtering). Protects services like CloudFront, ELB, and Route 53.

|Feature|AWS Shield Standard|AWS Shield Advanced|
|---|---|---|
|**Cost**|Free for all AWS customers|Paid subscription|
|**Protection Level**|Common Layer 3/4 attacks (e.g., SYN/UDP floods)|Advanced Layer 3/4 and Layer 7 attacks|
|**DDoS Response Team (DRT)**|Not available|24/7 access for mitigation support|
|**Cost Protection**|None|Covers scaling costs during attacks|
|**Attack Diagnostics**|Basic metrics|Detailed analytics and reports|
|**AWS WAF Integration**|Limited|Full integration with custom rules|
|**Coverage**|Automatic for CloudFront, ELB, Route 53|Enhanced for CloudFront, ELB, Route 53, EC2, and more|

### How It Works

- Always-on detection monitors for volumetric and protocol attacks.
- Shield Standard applies mitigation automatically at AWS edge locations.
- Shield Advanced adds near-real-time attack visibility and proactive mitigations.
- The DDoS Response Team (DRT) assists with complex or sustained attacks.
- Health-based detection and protection groups refine mitigation behavior.

### Key Features

- Always-on network and transport-layer protection for all customers.
- Advanced includes Layer 7 (application) protection via WAF.
- Cost protection that credits scaling charges incurred during attacks.
- Detailed attack diagnostics, metrics, and post-event reports.
- Protection for CloudFront, ELB, Route 53, EC2, and Global Accelerator.

### Common Use Cases

- Defending public-facing web applications from SYN/UDP floods.
- Protecting against application-layer (Layer 7) DDoS with WAF.
- Mitigating large volumetric attacks with a DDoS Response Team.
- Meeting availability requirements for critical services.

### Pricing & Limits

- Shield Standard is free and included with all AWS accounts.
- Shield Advanced is a monthly subscription plus a one-year commitment.
- Advanced also charges per protected resource.
- Cost protection covers some usage spikes but not all charges.

### Related Services

- [[WAF]]: Integrates with Shield Advanced for Layer 7 attack filtering.
- [[CloudFront]]: Protected by Shield for content delivery.
- Elastic Load Balancing (ELB): Shield ensures availability during attacks.
- [[Route 53]]: Shields DNS infrastructure from DDoS.
- [[CloudWatch]]: Monitors Shield events and metrics.
- [[AWS Global Accelerator]]: Gains additional DDoS mitigation with Advanced.
- [[Security Hub]]: Aggregates Shield findings for posture management.

### Related Concepts

- Distributed Denial of Service (DDoS): Attacks disrupting service availability.
- Layer 3/4 vs. Layer 7 Attacks: Network/transport vs. application-level threats.
- Cost Protection: Shield Advanced covers scaling costs during attacks.
- Always-On Protection: Automatic mitigation with no configuration for Standard.
- DDoS Response Team (DRT): Expert 24/7 mitigation support for Advanced.
- Edge Locations: Where AWS absorbs volumetric attacks.
