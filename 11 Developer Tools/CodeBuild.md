#AWS #Service #DevTools
### CodeBuild

Fully managed build service that compiles source code, runs tests, and produces artifacts for deployment. Supports custom environments, parallel builds, caching, and integration with CI/CD pipelines. Pay-per-minute based on compute usage.

### How It Works
- Reads source from [[CodeCommit]], S3, GitHub, or Bitbucket based on a build project configuration.
- Runs builds in a fresh, managed compute container with a buildspec (YAML) that defines phases.
- Executes install, pre-build, build, and post-build phases with a chosen runtime image.
- Uploads output artifacts and logs to [[S3]] and [[CloudWatch]].
- Scales build capacity automatically with no servers to provision.

### Key Features
- **Managed Runtimes**: Pre-built images for popular languages (Java, Python, Node.js, Go, .NET).
- **Custom Environments**: Bring your own Docker image or use AWS-managed images.
- **Parallel Builds**: Run multiple build batches concurrently for faster feedback.
- **Buildspec**: YAML/JSON file controlling each build phase and command.
- **Caching**: Cache dependencies in S3 to speed up repeat builds.
- **Integration**: Native actions inside [[CodePipeline]] and [[CodeStar]] workflows.

### Common Use Cases
- Compiling and unit-testing application source code on every commit.
- Producing deployable artifacts for [[CodeDeploy]] and ECS.
- Running static analysis, linting, and security scans in the pipeline.
- Building container images and publishing to registries.
- Generating and packaging documentation and reports.

### Pricing & Limits
- Billed per minute of compute used, based on instance type and size.
- Free tier provides a limited number of build minutes per month.
- Charges are based on the selected compute (e.g., general, large, GPU classes).

### Related Services
- [[CodePipeline]]: Orchestrates builds in CI/CD workflows.
- [[CodeCommit]]: Sources code repositories for builds.
- [[CodeDeploy]]: Deploys CodeBuild artifacts.
- [[S3]]: Stores build artifacts and logs.
- [[Lambda]]: Executes custom build tasks.
- [[CloudWatch]]: Captures build logs and metrics.
- [[CodeArtifact]]: Supplies and publishes packages during the build.

### Related Concepts
- Continuous Integration (CI): Automates code compilation and testing.
- Buildspec: YAML file defining build phases (install, pre-build, build, post-build).
- Artifacts: Output files from builds for deployment.
- Caching: Speeds builds by storing dependencies.
- CI/CD: Automated build-test-deploy pipelines.
