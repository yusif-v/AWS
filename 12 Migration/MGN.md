#AWS #Service #Migration
### MGN

Fully managed service for lift-and-shift migrations of on-premises servers (physical, virtual, cloud) to AWS EC2 with minimal downtime. Automates continuous block-level replication, testing, and cutover. Supports OS like Windows/Linux; ideal for large-scale migrations. Successor to CloudEndure Migration, MGN keeps source and target synchronized until you are ready to launch in AWS.

### How It Works

- Install the **MGN agent** on each source server (or use agentless replication for VMware).
- The agent performs continuous **block-level replication** of the source disk to a staging area in AWS.
- Target EC2 instances are launched from replicated data only at test or cutover time, so no compute is consumed before then.
- Use **launch templates** and boot settings to control instance type, subnet, and security group for the cutover.
- Test launches produce isolated copies for validation; final cutover launches production and stops replication.

### Key Features

- Continuous block-level replication for near-zero RPO and minimal downtime.
- Rehosts physical, virtual, and cloud servers onto [[EC2]] without re-architecting.
- Supports Windows and Linux across major virtualization platforms.
- Automated testing of cutover in a sandboxed environment.
- Centralized management through the console, [[Migration Hub]], and APIs.
- Post-launch actions and lifecycle scripts to finalize the instance after cutover.

### Common Use Cases

- Large-scale rehosting campaigns moving hundreds or thousands of servers.
- Migrating virtual machines from VMware or Hyper-V to EC2.
- Emergency relocation of workloads with strict RTO/RPO requirements.
- Standardizing on AWS before deeper replatforming or refactoring.

### Pricing & Limits

- Billed per source server per hour for replication, plus staging storage and any EC2 used.
- No charge for the migration itself; costs accrue until source replication is stopped.
- Data transfer during initial sync and ongoing replication is billed at standard rates.

### Related Services

- [[Migration Hub]]: Centralizes tracking of MGN progress.
- Amazon EC2: Hosts migrated servers and applications.
- [[Application Discovery Service]]: Discovers on-premises servers for planning.
- [[CloudWatch]]: Monitors replication metrics and performance.
- [[CloudFormation]]: Provisions resources post-migration.
- [[EC2]]: Target instance platform for rehosted servers.

### Related Concepts

- Lift-and-Shift Migration: Relocates apps to cloud without redesign.
- Continuous Replication: Block-level sync for near-zero data loss.
- Cutover: Final switch to AWS environment.
- Application Modernization: Optimizes workloads after migration.
- RTO/RPO: Recovery objectives that MGN's replication targets keep minimal.
