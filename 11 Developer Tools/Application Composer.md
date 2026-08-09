#AWS #Service #DevTools
### Application Composer

Visual builder (now AWS Infrastructure Composer) for composing serverless and modern applications via a drag-and-drop canvas. Connects AWS services, generates IaC templates (CloudFormation/SAM) with best practices. Supports import/export, local sync, and integrations like Step Functions Workflow Studio.

### How It Works
- Dragging resources onto the canvas builds a visual diagram that maps to underlying infrastructure code.
- Generates CloudFormation and SAM templates automatically, applying AWS-recommended best practices.
- Imports existing resources so the canvas reflects the currently deployed architecture.
- Synchronizes locally so edits made in code reflect back on the canvas.
- Launches editing tools such as Step Functions Workflow Studio directly from the canvas.

### Key Features
- **Visual Design**: Drag-and-drop composition of serverless and container-based architectures.
- **IaC Generation**: Produces CloudFormation/SAM templates instead of manual authoring.
- **Import & Export**: Imports existing projects and exports templates for reuse.
- **Local Sync**: Keeps canvas and code in sync for round-trip editing.
- **Integrations**: Connects with services like Lambda, VPC, and Step Functions.
- **Best Practices**: Applies secure, efficient defaults when composing resources.

### Common Use Cases
- Designing serverless applications before writing code.
- Onboarding teams on service relationships and architecture patterns.
- Prototyping event-driven data pipelines and API-backed applications.
- Converting an existing application into a well-structured CloudFormation/SAM project.

### Pricing & Limits
- The composer canvas itself is free; you pay for the underlying resources it provisions.
- Template output is subject to CloudFormation template and service quotas.

### Related Services
- [[CloudFormation]]: Generates and modifies IaC templates.
- AWS SAM: Builds serverless apps with simplified syntax.
- [[Lambda]]: Imports functions for composition.
- [[VPC]]: Configures networking resources visually.
- AWS Step Functions: Launches workflows from canvas.
- [[Cloud9]]: Author and test composed serverless code in a cloud IDE.
- [[CodePipeline]]: Deploys the IaC templates the composer generates.
- [[CodeCommit]]: Stores and versions the generated templates.

### Related Concepts
- Infrastructure as Code (IaC): Auto-generates templates for deployments.
- Serverless Architecture: Focuses on event-driven, scalable apps.
- Visual Design: Drag-and-drop for architecture building.
- Best Practices Automation: Ensures secure, efficient configurations.
- Event-Driven Architecture: Composing event sources and consumers on the canvas.
