#AWS #Concept #Concept
### Edge Locations

Edge locations are points of presence (PoPs) distributed around the world that cache content and accelerate delivery. Services like CloudFront and AWS Global Accelerator use them to serve users from the nearest location, reducing latency and improving throughput.

### How It Works
- Content is cached at PoPs near users so requests are served without reaching the origin.
- DNS and routing intelligence (e.g., [[Route 53]], [[AWS Global Accelerator]]) direct users to the nearest edge.
- Dynamic requests can be forwarded over AWS's low-latency backbone to the origin.
- Regional edge caches sit between edge locations and origins for larger objects.

### Key Features
- Hundreds of edge locations globally, far more numerous than regions.
- Both static caching ([[CloudFront]]) and network acceleration ([[AWS Global Accelerator]]).
- Offloads traffic from origin servers, reducing load and cost.
- Supports custom domains, SSL/TLS termination, and security features like [[WAF]] and [[Shield]].

### Common Use Cases
- Serving static assets, video, and downloads from the edge.
- Accelerating API traffic and dynamic content with Global Accelerator.
- Delivering live streaming and large file transfers.
- Protecting applications with DDoS mitigation and WAF at the edge.

### Pricing & Limits
- Edge location usage is billed per GB served and per request, varying by region.
- Caching incurs no separate fee; charges come from the service using the edge (e.g., CloudFront).
- Edge locations are not regions and cannot run customer compute directly.

### Related Services

- [[CloudFront]]: CDN serving cached content from edge locations.
- [[AWS Global Accelerator]]: Routes traffic through edge PoPs for performance.
- [[Route 53]]: Resolves DNS using edge-based anycast.

### Related Concepts

- Caching: Storing copies of content closer to users.
- CDN: Content delivery network built on edge locations.
- Latency: Minimized by geographic proximity.
- [[AWS Global Infrastructure]]: Edge locations are part of the broader footprint.
