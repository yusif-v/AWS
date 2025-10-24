#AWS #Service 
### AWS Shield

Managed DDoS protection service safeguarding AWS applications. Includes **Shield Standard** (free, automatic protection against common Layer 3/4 attacks for all AWS customers) and **Shield Advanced** (paid, with enhanced mitigation, 24/7 DDoS Response Team, cost protection, and Layer 7 filtering). Protects services like CloudFront, ELB, and Route 53.

|Feature|AWS Shield Standard|AWS Shield Advanced|
|---|---|---|
|**Cost**|Free for all AWS customers|Paid subscription|
|**Protection Level**|Common Layer 3/4 attacks (e.g., SYN/UDP floods)|Advanced Layer 3/4 and Layer 7 attacks|
|**DDoS Response Team (DRT)**|Not available|24/7 access for mitigation support|
|**Cost Protection**|None|Covers scaling costs during attacks|
|**Attack Diagnostics**|Basic metrics|Detailed analytics and reports|
|**AWS WAF Integration**|Limited|Full integration with custom rules|
|**Coverage**|Automatic for CloudFront, ELB, Route 53|Enhanced for CloudFront, ELB, Route 53, EC2, and more|

### Related Services

- [[AWS WAF]]: Integrates with Shield Advanced for Layer 7 attack filtering.
- [[Amazon CloudFront]]: Protected by Shield for content delivery.
- Elastic Load Balancing (ELB): Shield ensures availability during attacks.
- [[Amazon Route 53]]: Shields DNS infrastructure from DDoS.
- [[Amazon CloudWatch]]: Monitors Shield events and metrics.

### Related Concepts

- Distributed Denial of Service (DDoS): Attacks disrupting service availability.
- Layer 3/4 vs. Layer 7 Attacks: Network/transport vs. application-level threats.
- Cost Protection: Shield Advanced covers scaling costs during attacks.
- Always-On Protection: Automatic mitigation with no configuration for Standard.