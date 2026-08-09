#AWS #Service #Management
### CloudFormation

Service for provisioning and managing AWS resources using infrastructure-as-code. Defines resources, dependencies, and configurations in JSON or YAML templates. Automates stack creation, updates, and deletions for consistent, repeatable deployments across environments, ideal for DevOps and application management. CloudFormation is AWS's native Infrastructure-as-Code (IaC) service.

### How It Works

- A template declares the resources to create (EC2 instances, VPCs, S3 buckets, IAM roles, etc.) and their relationships.
- CloudFormation provisions resources in dependency order and rolls back the whole stack if a step fails, leaving a clean state.
- Stacks are the live, manageable units of resources created from a template; changes go through Change Sets for review.
- Nested stacks compose smaller, reusable stacks into larger architectures; StackSets deploy identical stacks across many accounts and regions.
- Custom resources backed by Lambda functions extend CloudFormation to anything you can script.

### Key Features

- **Drift Detection**: Compares the actual deployed configuration against the template and flags resources that changed out of band.
- **Change Sets**: Preview exactly what a stack update will add, modify, or delete before applying it.
- **StackSets**: Roll out consistent environments across multiple accounts and regions from one definition.
- **Registry & Public Extensions**: Reusable third-party resource types, including modules for common patterns.
- **Rollback Triggers & Capabilities**: Guard updates and require explicit acknowledgement for actions like creating IAM roles.
- **Template Designer**: Visual drag-and-drop authoring of templates in the console.

### Common Use Cases

- Bootstrapping entire environments (networking, compute, databases) in one repeatable deploy.
- Defining IAM roles and policies as code to review and version them like application code.
- Disaster recovery — redeploying a full stack in a new region from the same template.
- Integrating with CI/CD so CodePipeline deployments update stacks automatically.

### Pricing & Limits

- No charge for CloudFormation itself; you pay only for the resources the stacks create.
- Template size and stack resource count limits apply (e.g., a maximum number of resources and parameters per stack).
- StackSets have account and region quotas per operation.

### Related Services

- [[S3]]: Stores CloudFormation templates and artifacts.
- [[CloudTrail]]: Logs CloudFormation API activity for auditing.
- [[Config]]: Tracks resource configurations provisioned by CloudFormation.
- [[Lambda]]: Integrates for custom resource provisioning or automation.
- [[EC2]]: Common resource managed by CloudFormation.
- [[IaC]]: The broader infrastructure-as-code paradigm CloudFormation implements.
- [[IAM Roles]]: Roles often created and assumed by stacks during provisioning.
- [[CodePipeline]]: CI/CD orchestration that deploys CloudFormation stacks.
- [[EventBridge]]: Reacts to stack lifecycle events.
- [[Step Functions]]: Automates multi-step, multi-stack workflows.
- [[Control Tower]]: Uses CloudFormation internally to build landing zones.

### Related Concepts

- Infrastructure as Code (IaC): Manages infrastructure through code for automation and scalability.
- Stacks: Groups of AWS resources created and managed as a single unit.
- Change Sets: Previews proposed stack changes before execution.
- Drift Detection: Identifies discrepancies between actual and defined resource configurations.
- Nested Stacks: Reusable child stacks inside a parent template.
- StackSets: One template deployed across many accounts and regions.
- Custom Resources: Lambda-backed extensions for non-native resource types.
