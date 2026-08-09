#AWS #Concept #Concept
### IaC

Practice of managing and provisioning infrastructure through code and automation tools, enabling version control, repeatability, and consistency. In AWS, uses declarative templates to define resources, reducing manual errors and speeding deployments.

### How It Works
- Infrastructure is described in declarative templates (JSON/YAML) or code.
- The IaC tool reconciles the desired state with the current environment.
- Changes flow through the same review and CI/CD process as application code.
- Environments are reproducible across accounts and regions from the same template.

### Key Features
- Declarative templates managed by [[CloudFormation]].
- Programming-language definitions with AWS CDK (Python, TypeScript, etc.).
- Serverless-focused tooling with AWS SAM.
- Configuration management for Chef/Puppet via AWS OpsWorks.
- Drift detection to identify manual changes from the defined state.

### Common Use Cases
- Provisioning full environments (VPC, compute, databases) repeatably.
- Enforcing consistent security baselines across accounts.
- Enabling CI/CD deployment pipelines with infrastructure stages.
- Building development environments that mirror production.

### Pricing & Limits
- IaC tools like CloudFormation are free; costs come from the resources created.
- Template size and resource-count limits apply per stack.
- Templates should be versioned in Git or [[CodeCommit]] for auditability.

### Related Services

- [[CloudFormation]]: Automates resource provisioning with JSON/YAML templates.
- AWS CDK: Defines IaC using programming languages like Python or TypeScript.
- AWS SAM: Simplifies serverless IaC for Lambda and API Gateway.
- [[Config]]: Monitors IaC-managed resource configurations.
- AWS OpsWorks: Manages IaC for Chef/Puppet configurations.

### Related Concepts

- Declarative Programming: Specifies desired state; tool handles implementation.
- Version Control: Tracks IaC changes with Git or CodeCommit.
- Automation: Integrates with CI/CD pipelines for deployment.
- Drift Detection: Identifies deviations from defined IaC state.
- [[Architecture Design Principles]]: IaC operationalizes automation and repeatability.
