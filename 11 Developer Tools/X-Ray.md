#AWS #Service #DevTools
### X-Ray

AWS X-Ray traces requests as they flow through distributed applications. It maps the services and calls behind each request, identifies latency bottlenecks and errors, and integrates with Lambda, API Gateway, and EC2 via the X-Ray SDK.

### How It Works
- Instruments applications with the X-Ray SDK, which generates traces and forwards them to X-Ray.
- Each trace represents an end-to-end request split into segments and subsegments per service call.
- Combines traces from multiple services into a service map showing dependencies.
- Supports sampling rules to control how much traffic is traced.
- Integrates with AWS services (Lambda, API Gateway, ECS, EC2) for automatic trace collection.

### Key Features
- **End-to-End Tracing**: Follows requests across microservices and AWS services.
- **Service Map**: Visual dependency graph of services and calls per request.
- **Segments & Subsegments**: Granular timing for each service hop and downstream call.
- **Sampling Rules**: Configurable sampling to balance cost and coverage.
- **Annotations & Metadata**: Add custom labels for filtering and analysis.
- **Error Tracing**: Identifies HTTP errors, exceptions, and faults in the flow.

### Common Use Cases
- Debugging latency and bottlenecks in serverless and microservice applications.
- Visualizing dependencies between services during incident investigation.
- Measuring the impact of slow downstream calls (databases, third-party APIs).
- Monitoring request errors and error rates across an application.
- Correlating traces with [[CloudWatch]] logs and metrics for deeper diagnosis.

### Pricing & Limits
- Billed per trace recorded and per trace scanned per month.
- Free tier includes a limited number of traces per month.
- Costs scale with sampling rate and request volume.

### Related Services
- [[Lambda]]: Automatic tracing integration.
- [[API Gateway]]: Traces API request paths.
- [[CloudWatch]]: Metrics and logs alongside traces.
- [[EC2]]: Hosts instrumented applications for tracing.
- [[ECS]]: Traces containerized workloads.
- [[DynamoDB]]: Traces downstream database calls.
- [[S3]]: Traces object access within a request flow.
- [[CloudTrail]]: Logs the API calls that X-Ray analyzes.

### Related Concepts
- Trace: End-to-end request path.
- Segment/Subsegment: Service-level trace units.
- Service Map: Visual dependency graph.
- Distributed Tracing: Following requests across multiple services.
- Sampling: Tracing a subset of requests to control cost.
