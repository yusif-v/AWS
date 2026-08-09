#AWS #Service #Compute
### EC2 Instance Types

EC2 instance types are grouped into families: general purpose, compute optimized, memory optimized, storage optimized, and accelerated computing. Each family balances CPU, memory, storage, and network to match workload needs, with size tiers scaling resources within a family.

### How It Works

- Instance types are named by family letter, generation number, and size, e.g. m5.large or r6g.2xlarge.
- Sizes within a family scale vCPU, memory, and network bandwidth proportionally (small through 48xlarge).
- Newer generations add features like instance store NVMe, higher baseline performance, and improved security.
- Graviton-based types (Arm processors) offer better price-performance for many workloads.
- An instance type is chosen at launch time and, for most types, can be changed later only by stopping the instance.

### Key Families

- General purpose (M, T, A): balanced compute and memory; T types are burstable for variable workloads.
- Compute optimized (C): high CPU-to-memory ratio for batch, media transcoding, and high-performance web servers.
- Memory optimized (R, X, High Memory, z): large memory for in-memory databases, caches, and analytics.
- Storage optimized (I, D, H): high I/O and dense storage for databases and HDFS workloads.
- Accelerated computing (P, G, Inf, Trn, F): GPUs for ML and graphics, Inferentia for inference, Trainium for training, FPGAs for custom silicon.
- HPC optimized (Hpc): high-performance computing with high network throughput.

### Common Use Cases

- Right-sizing web and application servers to the general purpose family.
- Compute-heavy rendering and encoding on C family instances.
- In-memory caches and databases (Redis, SAP HANA) on memory optimized types.
- Machine learning training and inference on accelerated computing types.
- Dense data processing on storage optimized instances.

### Pricing & Limits

- Billed per second (Linux) or per hour based on the chosen type and size; larger sizes cost more.
- On-Demand, Reserved, Spot, and Savings Plans apply across all instance families.
- Default quotas cap the number of vCPUs you can run per region, but you can request increases.

### Related Services

- [[EC2]]: The service that launches these instances.
- [[EC2 Pricing Models]]: How instance usage is billed.
- [[Auto Scaling]]: Adjusts instance counts by type.
- [[Compute Optimizer]]: Recommends instance type changes for efficiency.

### Related Concepts

- vCPU: Virtual CPU sizing.
- Instance Families: Purpose-built resource balances.
- [[EC2 AMIs]]: The images instances are launched from.
- [[Regions & Availability Zones]]: Placement affects latency and pricing of instance types.
