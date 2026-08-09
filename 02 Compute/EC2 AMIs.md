#AWS #Service #Compute
### EC2 AMIs

An Amazon Machine Image (AMI) is a template containing the OS, applications, and configuration used to launch EC2 instances. AMIs can be created from existing instances, imported, or selected from the Marketplace, and include metadata like block-device mapping and permissions.

### How It Works

- An AMI packages a root volume (an EBS snapshot or instance-store template) with a launch permission policy and block-device mapping.
- When you launch an instance, EC2 uses the AMI to create the root volume and any additional volumes defined in the mapping.
- AMIs are regional: an image in one region must be copied to another region before use there.
- Launch permissions control which accounts can use an AMI; Marketplace AMIs bring their own licensing terms.

### Key Features

- Golden images: standardized, pre-hardened images with patches, agents, and configuration baked in for consistent fleet launches.
- Cross-region and cross-account sharing via image copy and launch permissions.
- Create Image from a running instance captures a point-in-time snapshot as a new AMI.
- EBS-backed and instance-store-backed variants; EBS-backed images support stop/start and smaller root volumes.
- AMI versions let you track and roll back standardized configurations over time.
- Snapshots backing the AMI are stored incrementally in S3, keeping storage cost low.

### Common Use Cases

- Standardizing operating-system baselines across development, staging, and production environments.
- Disaster recovery by copying critical AMIs to another region.
- Fast horizontal scaling: Auto Scaling launches new instances from the same image for consistency.
- Distributing preconfigured software or images through the AWS Marketplace.

### Pricing & Limits

- No charge for the AMI itself; you pay for the EBS snapshot storage backing EBS-backed images.
- Default quotas limit the number of AMIs and snapshots per account per region, with higher limits available on request.

### Related Services

- [[EC2]]: Launches instances from AMIs.
- [[EC2 Storage]]: Block devices defined by the AMI.
- [[Backup]]: Creates instance backups as images.
- [[EBS]]: Snapshots store the root volume of EBS-backed AMIs.
- [[Auto Scaling]]: Launches consistent instances from a golden AMI.

### Related Concepts

- Golden Image: A standardized, pre-hardened AMI.
- Image Permissions: Sharing AMIs across accounts.
- [[EC2 Instance Types]]: Pairs an AMI with an instance type.
- [[Regions & Availability Zones]]: AMIs must be copied to each region where they are used.
