#AWS #Service #Compute
### Lightsail

Simplified platform for launching and managing virtual private servers (VPS) with fixed pricing. Offers preconfigured instances with compute, memory, storage, and networking for small-scale applications, websites, or dev environments. Includes built-in features like load balancers, databases, and snapshots for backups.

### How It Works

- You choose a blueprint (OS or application stack such as WordPress, LAMP, Node.js) and an instance plan with fixed CPU, memory, storage, and data transfer.
- Instances launch in minutes with a simplified management console, SSH/RDP access, and static IPs.
- Add-ons such as load balancers, managed databases, DNS zones, and block storage are created through the same simple interface.
- Snapshots create point-in-time backups you can use to restore or clone instances and databases.
- Resources live in the Lightsail platform but can interoperate with a wider AWS network through VPC peering.

### Key Features

- Predictable, flat monthly pricing with no usage-based surprises for small workloads.
- One-click blueprints for common applications (WordPress, LAMP, MEAN, Node.js, and more).
- Managed databases (MySQL, PostgreSQL) as a simpler alternative to full RDS.
- Built-in load balancer, managed DNS, static IPs, and snapshots.
- Free monthly data transfer included with each plan.
- Simple console and CLI tailored for beginners and small teams.

### Common Use Cases

- Small business websites, blogs, and portfolios.
- Development and test environments that need fast provisioning.
- Lightweight web apps and internal tools without AWS complexity.
- Prototyping before graduating to EC2 for larger scale.

### Pricing & Limits

- Fixed monthly price per plan, billed at a flat hourly rate.
- Data transfer is included in the plan, with overages billed separately.
- Each plan has a maximum instance size and storage; migrate to EC2 when scaling beyond Lightsail's bounds.

### Related Services

- [[EC2]]: Provides more advanced, customizable compute options compared to Lightsail’s simplicity.
- [[RDS]]: Lightsail databases are a simplified alternative for relational storage.
- [[Route 53]]: Manages DNS for Lightsail-hosted applications.
- [[CloudWatch]]: Monitors Lightsail instance metrics and performance.
- [[VPC]]: Peering connects Lightsail resources to a wider AWS network.

### Related Concepts

- Virtual Private Server (VPS): Preconfigured virtual machines for quick deployment.
- Fixed Pricing: Predictable, low-cost billing for small workloads.
- Snapshots: Point-in-time backups for Lightsail instances and databases.
- Simplified Cloud: Lightsail abstracts complex AWS configurations for beginners.
- [[PaaS]]: Simplifies provisioning while retaining instance-level control.
