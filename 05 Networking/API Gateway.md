#AWS #Service #Networking
### API Gateway

Fully managed service for creating, publishing, maintaining, monitoring, and securing APIs at any scale. Acts as the "front door" for applications, routing requests to backends such as Lambda functions, EC2 instances, or on-premises services. Supports REST, HTTP, and WebSocket APIs with integrated security, throttling, and monitoring.

### How It Works
- Clients call an API Gateway endpoint; the gateway authenticates, validates, transforms, and routes each request to a configured backend integration.
- Three API types: **REST APIs** (full-featured with API keys and usage plans), **HTTP APIs** (low-latency and lower cost), and **WebSocket APIs** (persistent two-way connections).
- Native proxy integration invokes Lambda functions directly from an HTTP method + path without managing servers.
- Deployments are managed through stages (e.g., dev, prod), each with its own endpoint URL and environment settings.
- Every request generates CloudWatch logs and metrics for monitoring, debugging, and cost allocation.

### Key Features
- Request/response transformation, including payload mapping between client and backend formats (e.g., JSON to XML).
- Throttling and rate limiting with configurable burst and steady-state limits.
- Multiple authentication options: IAM, Cognito user pools, Lambda authorizers, and mutual TLS.
- Response caching to reduce latency and backend load.
- Swagger/OpenAPI import and export for API definition management.
- CORS support and WebSocket connection lifecycle management.

### Common Use Cases
- Serverless backends where API Gateway fronts Lambda for event-driven microservices.
- API proxy/aggregation layer that exposes many backend services behind one stable endpoint.
- Real-time apps such as chat, collaborative editing, and live dashboards via WebSocket APIs.
- Monetizing APIs through usage plans, API keys, and per-client throttling.
- Exposing legacy or on-premises services through a managed, secure edge.

### Pricing & Limits
- Billed per API request, with HTTP APIs costing less per call than REST APIs.
- WebSocket APIs billed per connection-minute plus per-message data transfer.
- Account-level throttling limits apply by default; increases can be requested.
- No additional charge for API Gateway data transfer; standard AWS data transfer rates apply for egress.

### Related Services
- [[Lambda]]: The most common backend integration for API Gateway.
- [[Route 53]]: DNS and custom domains for API endpoints.
- [[CloudFront]]: CDN in front of APIs for edge caching and lower latency.
- [[WAF]]: Web application firewall protection for APIs.
- [[CloudWatch]]: Logs and metrics for every API call.
- [[Cognito]]: User authentication for API access.
- [[ACM]]: Free TLS certificates for custom domains.

### Related Concepts
- REST, HTTP, and WebSocket API types.
- Stages and deployments for versioning.
- Usage plans and API keys for access control.
- Throttling and caching for scale and performance.
