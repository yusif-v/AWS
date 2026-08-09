#AWS #Service #Networking
### ELB

Elastic Load Balancing (ELB) automatically distributes traffic across targets. Types include Application Load Balancer (HTTP/HTTPS, path-based routing), Network Load Balancer (TCP/UDP, extreme performance), and Gateway Load Balancer (third-party appliances). It integrates with Auto Scaling and Route 53.

### How It Works
- A load balancer receives traffic on configured listeners and routes each request to a healthy target in a target group.
- Application Load Balancers operate at Layer 7, evaluating HTTP/HTTPS attributes like paths, headers, and hostnames.
- Network Load Balancers operate at Layer 4, handling millions of requests per second with ultra-low latency and static IPs.
- Gateway Load Balancers transparently insert third-party appliances (firewalls, IDS/IPS) into the data path.
- Health checks continuously monitor target availability; only healthy targets receive traffic.

### Key Features
- Application Load Balancer: path-based and host-based routing, HTTP/2, WebSockets, and Lambda targets.
- Network Load Balancer: static IP support, extreme throughput, preservation of source IP.
- Gateway Load Balancer: transparent inline deployment of virtual appliances via GENEVE.
- TLS termination with free certificates from ACM.
- Sticky sessions, connection draining, and cross-zone load balancing.
- Integration with Auto Scaling to scale targets with demand.

### Common Use Cases
- Distributing traffic across EC2 instances or containers (ECS, EKS) in one or more Availability Zones.
- Microservices routing based on URL path or hostname to different backend services.
- Exposing Lambda functions over HTTP with ALB targets.
- TCP/UDP game servers and latency-critical workloads with NLB.
- Firewall and security appliance insertion with GLB.

### Pricing & Limits
- Billed per hour plus per load balancer capacity units (LCUs for ALB, NLB units for NLB, GLCUs for GLB).
- AWS Free Tier includes 750 hours of ALB/NLB time per month for 12 months.
- No per-target charges; costs scale with processed data.
- Costs vary by load balancer type and amount of traffic processed.

### Related Services
- [[EC2]]: Common targets for load-balanced traffic.
- [[Auto Scaling]]: Scales targets in response to load.
- [[Route 53]]: DNS routing to the load balancer.
- [[ACM]]: TLS certificates for HTTPS listeners.
- [[WAF]]: Layer 7 protection for ALB listeners.
- [[CloudWatch]]: Metrics and alarms for load balancer health.
- [[VPC]]: Where load balancers and targets reside.

### Related Concepts
- Health Checks: Monitor target availability.
- Target Group: Logical set of targets.
- Listener: Rules that route traffic.
- Cross-Zone Load Balancing: Distributes traffic evenly across AZs.
- Sticky Sessions: Pin a client to a target for session persistence.
