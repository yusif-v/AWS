#AWS #Service #Migration
### Transfer Family

AWS Transfer Family is a managed service for moving data in and out of S3 and EFS using SFTP, FTPS, and FTP protocols. It provides managed servers, integrates with IAM for user access, and suits legacy file-transfer workloads migrating to AWS. No file-transfer servers to patch or run; AWS manages the endpoint while you authenticate users through your identity provider.

### How It Works

- Create a **managed server** configured for SFTP, FTPS, or FTP.
- Point the server at a storage location in [[S3]] or [[EFS]] as the home directory.
- Authenticate users via IAM identities or an external identity provider such as Active Directory.
- Route each user to a mapped directory in storage, preserving scoped access.
- AWS runs the protocol endpoints in an internal network, managed for high availability.

### Key Features

- Support for SFTP, FTPS, and FTP on fully managed servers.
- Identity provider integration with IAM and custom (SCIM or AD) providers.
- Access scoping per user to specific paths in [[S3]] or [[EFS]].
- AWS PrivateLink support for private VPC connectivity to the endpoints.
- Pay-as-you-go with no upfront infrastructure.
- Workflow automations to process files after transfer.

### Common Use Cases

- Replacing legacy on-premises SFTP servers with a managed AWS alternative.
- Trading-partner and B2B file exchange into [[S3]].
- Securing FTP workloads behind managed authentication and private connectivity.
- Ingesting files from external parties before downstream processing.

### Pricing & Limits

- Billed per hour per server plus data transfer costs.
- Pricing is independent of storage; you still pay for the [[S3]]/[[EFS]] used.
- Data transfer in is free; egress follows standard AWS data transfer pricing.

### Related Services

- [[S3]]: Primary storage for transfer servers.
- [[EFS]]: Alternative storage destination.
- [[DataSync]]: High-volume automated transfer.
- [[IAM]]: Authenticates and authorizes SFTP/FTPS/FTP users.
- [[VPC]]: Endpoints can be hosted privately via PrivateLink.

### Related Concepts

- SFTP/FTPS/FTP: File transfer protocols.
- Managed Server: No servers to operate.
- Identity Provider: IAM or AD integration.
- Serverless File Transfer: Protocol endpoints without managing the underlying infrastructure.
