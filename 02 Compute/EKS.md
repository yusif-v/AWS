#AWS #Service #Compute
### EKS

Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service. AWS runs the control plane for high availability, integrates with IAM, ELB, and CloudWatch, and supports self-managed nodes, managed node groups, and Fargate for running pods.

### How It Works

- AWS operates a highly available Kubernetes control plane (API server, etcd, scheduler) across multiple Availability Zones.
- Worker capacity runs as managed node groups (EC2), self-managed nodes, or Fargate profiles, registered with the control plane.
- You use standard kubectl and the Kubernetes API; the cluster stays compatible with upstream Kubernetes.
- IAM is integrated via OIDC for Kubernetes RBAC and IAM Roles for Service Accounts (IRSA).
- Load balancers, persistent volumes (EBS/EFS), and monitoring (CloudWatch Container Insights) are wired through controllers and add-ons.

### Key Features

- Managed control plane with automatic upgrades, patching, and high availability for the API server.
- Managed node groups that handle EC2 worker provisioning, updates, and scaling.
- Fargate profiles run serverless pods without managing nodes.
- Integration with CloudWatch Container Insights, ELB (ALB/NLB via controllers), and CloudTrail.
- EKS add-ons for networking (VPC CNI), storage (EBS/EFS CSI), and observability.
- Support for both x86 and Graviton (Arm) node types.

### Common Use Cases

- Standardizing on Kubernetes for portability across environments and clouds.
- Running microservices, service mesh, and event-driven workloads.
- Machine learning training and inference with GPU node groups.
- Migrating existing Kubernetes clusters from other platforms to AWS.

### Pricing & Limits

- Billed per cluster-hour (control plane) plus the cost of the underlying EC2 or Fargate resources.
- Managed node groups and add-ons carry no additional service charge beyond the compute they use.
- Each cluster has default quotas for nodes, pods, and resources that can be raised on request.

### Related Services

- [[ECS]]: AWS's own container orchestrator.
- [[Fargate]]: Run EKS pods without managing nodes.
- [[CloudWatch]]: Monitoring and logging for clusters.
- [[EC2]]: Worker nodes for managed node groups.
- [[EBS]], [[EFS]]: Persistent storage via CSI drivers.
- [[ELB]]: Load balancing for services and ingress.

### Related Concepts

- Kubernetes: Open-source container orchestration.
- Control Plane: Managed by AWS in EKS.
- Node Group: Worker nodes running pods.
- [[IaC]]: Cluster and workload definitions with CloudFormation or CDK.
- [[IAM Roles]]: Pod-level permissions through IRSA.
