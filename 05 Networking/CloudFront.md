#AWS #Service #Networking
### CloudFront

Content Delivery Network (CDN) service that accelerates delivery of static and dynamic content (e.g., web pages, videos, APIs) via a global network of edge locations. Caches content to reduce latency, supports HTTPS, and integrates with AWS services for secure, scalable content distribution.

### How It Works
- Content is cached at edge locations worldwide so users retrieve it from the nearest point of presence instead of the origin.
- A distribution ties CloudFront to an origin (S3 bucket, ELB, EC2, or custom server) and defines behaviors for caching and routing.
- Cache TTLs are controlled by Cache-Control/Expires headers or distribution defaults.
- Viewer and origin requests can be customized with CloudFront Functions (lightweight) or Lambda@Edge (full compute).
- Serves content from a global network of edge locations with HTTP/1.1, HTTP/2, and HTTP/3 support.

### Key Features
- Global low latency: content served from the closest edge location.
- HTTPS termination with free certificates from ACM and integration with S3 for secure static hosting.
- Lambda@Edge and CloudFront Functions to run code at the edge.
- Signed URLs and signed cookies for private content delivery.
- Cache invalidation to remove stale objects and geo-restriction for regional control.
- Integration with Shield and WAF for DDoS and Layer 7 protection.

### Common Use Cases
- Static website hosting (S3 + CloudFront + Route 53).
- Video streaming and large media delivery with on-demand or live workflows.
- API acceleration and caching for global applications.
- Software downloads and over-the-air updates at scale.
- E-commerce with dynamic content and TLS acceleration.

### Pricing & Limits
- Billed per GB of data transferred out plus per-request charges, varying by edge region.
- AWS Free Tier includes 1 TB of data transfer out and 10 million HTTP/HTTPS requests per month for 12 months.
- Cache invalidation is free for the first 1,000 paths per month, then billed per path.
- No upfront costs; pay-as-you-go.

### Related Services
- [[S3]]: Stores static content served by CloudFront.
- Elastic Load Balancing (ELB): Distributes traffic for dynamic content with CloudFront.
- AWS Lambda@Edge: Runs serverless code at edge locations for customized content delivery.
- [[Shield]]: Provides DDoS protection for CloudFront distributions.
- [[WAF]]: Filters malicious traffic for CloudFront-hosted content.
- [[Route 53]]: DNS routing to the distribution's CNAME/alias.
- [[ACM]]: Provides free SSL/TLS certificates for custom domains.

### Related Concepts
- Content Delivery Network (CDN): Reduces latency by caching content closer to users.
- Edge Locations: Global points of presence for caching and content delivery.
- Origin Servers: Source of content (e.g., S3, EC2) for CloudFront distributions.
- Cache Invalidation: Removes outdated content from edge caches for updates.
- Distributions and behaviors: Configuration objects that define caching and routing.
