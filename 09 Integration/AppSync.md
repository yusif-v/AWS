#AWS #Service #Integration
### AppSync

AWS AppSync is a managed GraphQL service that builds real-time and offline-capable APIs. It resolves queries against DynamoDB, Lambda, and other data sources, supports subscriptions for live updates, and authenticates with Cognito, IAM, or API keys.

### How It Works
- Define a GraphQL schema with types, queries, mutations, and subscriptions that describe the API contract.
- Attach resolvers to each field, mapping requests and responses to backing data sources.
- Data sources include DynamoDB, Lambda, RDS, OpenSearch, Neptune, HTTP endpoints, and other AWS services.
- Subscriptions are delivered over WebSocket connections for real-time data updates.
- Client SDKs cache data locally and sync in the background, enabling offline-capable apps.

### Key Features
- Real-time subscriptions push updates to connected clients as data changes.
- Offline sync with automatic conflict resolution when devices come back online.
- Multiple authorization modes per API, including Cognito user pools, IAM, API keys, and OIDC.
- Fine-grained access control at the field level using authorization directives in the schema.
- Resolver caching and request-level caching to reduce latency and data source load.
- Schemas can be built with VTL or JavaScript resolver templates.

### Common Use Cases
- Mobile and web apps that need live data and reliable offline behavior.
- Aggregating several backends (databases, microservices, legacy APIs) behind a single typed endpoint.
- Real-time dashboards, chat, collaboration tools, and live IoT feeds.
- Serverless APIs combined with Lambda, DynamoDB, and Cognito for a fully managed stack.
- Progressive rollout and schema evolution with GraphQL introspection.

### Pricing & Limits
- Billed per API operation (queries and mutations) and for real-time subscription connection minutes.
- Includes a monthly free tier of operations for most accounts, keeping small apps inexpensive.
- No charge for data transfer between AppSync and other AWS services in the same region.
- Costs grow with payload complexity and subscription concurrency rather than fixed monthly fees.

### Related Services

- [[DynamoDB]]: Common data source.
- [[Lambda]]: Custom resolvers.
- [[Cognito]]: User authentication.
- [[API Gateway]]: REST/WebSocket alternative for API frontends.
- [[S3]]: Static assets and offline data for mobile clients.
- [[OpenSearch]], [[Neptune]]: Search and graph data sources.

### Related Concepts

- GraphQL: Typed query language.
- Resolvers: Map fields to data sources.
- Subscriptions: Real-time push updates.
- Schema-First Development: API contract defined before implementation.
- Offline Sync: Local caching with background reconciliation.
