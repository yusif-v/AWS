#Amazon 
### Amazon FSx File Gateway

Fully managed hybrid storage service within AWS Storage Gateway, providing low-latency on-premises access to Amazon FSx for Windows File Server via SMB protocol. Caches frequently accessed data locally on gateway appliances, syncs changes to FSx in the cloud for seamless file sharing and backups.

### Related Services

- AWS Storage Gateway: Core service hosting FSx File Gateway mode.
- Amazon FSx for Windows File Server: Cloud file storage accessed via the gateway.
- [[Amazon EC2]]: Runs virtual gateways for FSx access.
- [[Amazon CloudWatch]]: Monitors gateway performance and metrics.
- AWS Backup: Backs up data stored in FSx via the gateway.

### Related Concepts

- Hybrid Cloud Storage: Extends on-premises access to cloud file systems.
- File Caching: Local storage of hot data for reduced latency.
- SMB Protocol: Enables Windows-compatible file sharing.
- Data Synchronization: Ensures consistency between on-premises and cloud.