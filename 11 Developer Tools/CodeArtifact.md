#AWS #Service #DevTools
### CodeArtifact

AWS CodeArtifact is a fully managed artifact repository for storing and sharing packages (npm, Maven, PyPI, NuGet). It integrates with CodeBuild and CodePipeline for secure package delivery, supports proxying upstream registries, and provides private package hosting.

### How It Works
- Hosts private package repositories scoped to a domain and repository hierarchy.
- Proxies public upstream registries (npm, Maven Central, PyPI, NuGet) with caching.
- Resolves dependencies at build time by querying repositories in a configured order.
- Authenticates clients with temporary credentials from [[STS]] or IAM.
- Audits package access and downloads through [[CloudTrail]].

### Key Features
- **Package Types**: Supports npm, Maven, PyPI, NuGet, and generic package formats.
- **Upstream Repositories**: Caches public packages while keeping them discoverable.
- **Domains**: Group repositories to centralize policies and share packages across accounts.
- **Asset Lifecycle**: Versioning and immutable package versions prevent overwrite.
- **Access Control**: Granular IAM policies and external connections for fine-grained sharing.
- **Integration**: Feeds [[CodeBuild]] and [[CodePipeline]] with dependencies and publish targets.

### Common Use Cases
- Hosting proprietary or internal packages that must not be public.
- Speeding builds by caching third-party dependencies near the build environment.
- Publishing build outputs from [[CodeBuild]] for later consumption.
- Enforcing consistent, versioned dependencies across an organization.
- Replacing self-managed Nexus or Artifactory infrastructure.

### Pricing & Limits
- Billed per GB of storage and per GB of data transferred.
- On-demand and cached package downloads are metered separately.
- No upfront fees; pay-as-you-go storage and request costs.

### Related Services
- [[CodeBuild]]: Resolves packages from CodeArtifact.
- [[CodePipeline]]: Automates package deployment.
- [[CodeCommit]]: Source control alongside packages.
- [[STS]]: Issues temporary credentials for artifact authentication.
- [[S3]]: Durable storage backing artifact content.
- [[CloudTrail]]: Logs package and repository API activity.

### Related Concepts
- Repository: Logical package store.
- Upstream: Proxy to public registries.
- Package Resolution: Dependency fetching.
- Software Supply Chain: Secure management of dependencies and artifacts.
- Dependency Caching: Reusing fetched packages to accelerate builds.
