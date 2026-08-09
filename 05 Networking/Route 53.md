#AWS #Service #Networking
### Route 53

Scalable, highly available Domain Name System (DNS) service for routing traffic to AWS and external resources. Provides domain registration, DNS resolution, health checks, and traffic management. Supports latency-based routing, geo-routing, and weighted routing for global applications.

### How It Works
- Hosted zones hold DNS records (A, AAAA, CNAME, MX, TXT, etc.) for one or more domains.
- Queries are answered from a global, distributed network of DNS servers for high availability.
- Alias records map a domain to AWS resources (ELB, CloudFront, S3, Global Accelerator) and update automatically when IPs change.
- Health checks monitor endpoints and drive failover routing policies.
- Route 53 Resolver provides DNS resolution between VPCs and on-premises networks.

### Key Features
- Domain registration with automatic renewal and transfer.
- Routing policies: simple, weighted, latency-based, failover, geolocation, geoproximity, and multivalue answer.
- Alias records: free and automatically track AWS resource IP changes.
- Private hosted zones for internal, VPC-only DNS.
- Traffic Flow visual editor and traffic policies for complex routing.
- DNSSEC signing and a 100% availability SLA for public DNS.

### Common Use Cases
- DNS resolution and domain registration for web applications.
- Global traffic routing based on user location or latency.
- Active/passive and active/active failover across regions using health checks.
- Static website hosting via S3 with a custom domain.
- Hybrid DNS resolution between VPCs and on-premises with the Resolver.

### Pricing & Limits
- Billed per hosted zone per month plus per million queries.
- Health checks billed monthly per check, with optional HTTPS and string-matching checks.
- Domain registration billed annually per domain.
- Alias records to AWS resources are free.

### Related Services
- [[CloudFront]]: Integrates with Route 53 for low-latency content delivery.
- Elastic Load Balancing (ELB): Routes traffic to load balancers for high availability.
- [[EC2]]: Directs DNS queries to EC2 instances.
- [[S3]]: Hosts static websites with Route 53 DNS.
- [[Shield]]: Protects Route 53 from DDoS attacks.
- [[AWS Global Accelerator]]: Static IP-based alternative for global routing.
- [[CloudWatch]]: Monitors health check status and drives alarms.

### Related Concepts
- Domain Name System (DNS): Translates domain names to IP addresses.
- Health Checks: Monitors endpoint availability for failover routing.
- Traffic Policies: Directs traffic based on latency, geography, or weights.
- High Availability: Multi-region DNS ensures reliable global access.
- Hosted Zones: Containers for DNS records.
- TTL: Time-to-live controlling how long resolvers cache answers.
