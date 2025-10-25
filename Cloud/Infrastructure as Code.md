#Concept 
### Infrastructure as Code (IaC)

Practice of managing and provisioning infrastructure through code and automation tools, enabling version control, repeatability, and consistency. In AWS, uses declarative templates to define resources, reducing manual errors and speeding deployments.

### Related Services

- [[AWS CloudFormation]]: Automates resource provisioning with JSON/YAML templates.
- [[AWS CDK]]: Defines IaC using programming languages like Python or TypeScript.
- AWS SAM: Simplifies serverless IaC for Lambda and API Gateway.
- [[AWS Config]]: Monitors IaC-managed resource configurations.
- AWS OpsWorks: Manages IaC for Chef/Puppet configurations.

### Related Concepts

- Declarative Programming: Specifies desired state; tool handles implementation.
- Version Control: Tracks IaC changes with Git or CodeCommit.
- Automation: Integrates with CI/CD pipelines for deployment.
- Drift Detection: Identifies deviations from defined IaC state.