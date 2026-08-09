#AWS #Service #Migration
### Snowball Edge

Ruggedized device for edge computing, storage, and data transfer in remote or disconnected environments. Offers up to 210 TB storage, onboard compute (EC2 instances, Lambda), and clustering for local processing. Ships to customer for data loading, then returns to AWS for upload to S3; supports S3-compatible API for hybrid workflows. Designed for data center, remote, and field use where network transfer is impractical.

### How It Works

- Order a Snowball Edge device from the console and it is shipped to your location.
- Load data locally through the S3-compatible API or the File Gateway interface; onboard compute runs as needed.
- Devices can be **clustered** to scale storage and compute beyond a single unit.
- Run EC2 instances, [[Lambda]] functions, and Amazon S3-compatible workloads directly on the device.
- Ship the device back; AWS ingests the data into [[S3]] in the destination region and erases the device.

### Key Features

- Storage-optimized, compute-optimized, and GPU variants for different workloads.
- Onboard EC2 and Lambda compute enables local processing before transfer.
- Up to 210 TB of usable storage per device, clusterable for larger datasets.
- S3-compatible interface for drop-in application compatibility.
- End-to-end encryption with [[KMS]]-managed keys and tamper-evident enclosures.
- Clustering support for high-availability local operation.

### Common Use Cases

- Petabyte-scale offline data transfer to [[S3]].
- Edge computing in disconnected or low-bandwidth environments (factories, oil rigs, field stations).
- Pre-processing, filtering, or analytics on data before it is uploaded.
- Hybrid cloud workflows that need local storage with eventual sync to AWS.

### Pricing & Limits

- Per-job service charge plus storage per GB-month for the device rental duration.
- Data transfer out is billed; inbound transfer to [[S3]] is free.
- Device must be returned within a set service period to avoid additional fees.

### Related Services

- [[Snowball]]: Non-Edge version for pure data transfer without compute.
- [[S3]]: Primary destination for uploaded data.
- [[Lambda]]: Runs serverless code locally on Snowball Edge.
- AWS IoT Greengrass: Extends ML/IoT capabilities to Edge devices.
- [[DataSync]]: Complements for network-based transfers.
- [[KMS]]: Encrypts data at rest on the device.

### Related Concepts

- Edge Computing: Processes data locally to reduce latency and bandwidth needs.
- Offline Data Transfer: Physical shipping for large datasets in low-connectivity areas.
- Hybrid Cloud: Bridges on-premises/edge with AWS for consistent operations.
- Data Security: End-to-end encryption with AWS KMS during transfer.
- Storage Classes: Data lands in [[S3]] and can then be tiered with lifecycle policies.
