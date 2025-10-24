#AWS 
### AWS Snowball Edge

Ruggedized device for edge computing, storage, and data transfer in remote or disconnected environments. Offers up to 210 TB storage, onboard compute (EC2 instances, Lambda), and clustering for local processing. Ships to customer for data loading, then returns to AWS for upload to S3; supports S3-compatible API for hybrid workflows.

### Related Services

- [[AWS Snowball]]: Non-Edge version for pure data transfer without compute.
- [[Amazon S3]]: Primary destination for uploaded data.
- [[AWS Lambda]]: Runs serverless code locally on Snowball Edge.
- AWS IoT Greengrass: Extends ML/IoT capabilities to Edge devices.
- [[AWS DataSync]]: Complements for network-based transfers.

### Related Concepts
- Edge Computing: Processes data locally to reduce latency and bandwidth needs.
- Offline Data Transfer: Physical shipping for large datasets in low-connectivity areas.
- Hybrid Cloud: Bridges on-premises/edge with AWS for consistent operations.
- Data Security: End-to-end encryption with AWS KMS during transfer.