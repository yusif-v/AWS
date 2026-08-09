#AWS #Service #Networking
### VPC Endpoints

VPC Endpoints enable private connectivity between a VPC and AWS services (e.g., S3, DynamoDB, Lambda) without traversing the public internet. Gateway endpoints (S3, DynamoDB) and interface endpoints (ENI-based, most services) both keep traffic inside the AWS network.

### How It Works
- A gateway endpoint adds an entry to a VPC route table pointing to a prefix list for the target service (S3 or DynamoDB); traffic follows the internal AWS network.
- An interface endpoint creates an elastic network interface (ENI) with a private IP in a subnet, backed by AWS PrivateLink, for most other AWS services.
- Endpoint policies (JSON) control which actions and resources are allowed through the endpoint.
- Both types keep traffic off the public internet and remove the need for a NAT Gateway or internet gateway for those services.
- Gateway endpoints are free and highly available by design; interface endpoints use an ENI per subnet.

### Key Features
- Gateway endpoints: no hourly charge, no ENI, automatic high availability across AZs, limited to S3 and DynamoDB.
- Interface endpoints: work with hundreds of AWS services, integrate with security groups, and support private DNS.
- Endpoint policies and integration with IAM for fine-grained access control.
- Private DNS option for interface endpoints simplifies service access.
- Traffic never leaves the AWS network, improving security and reducing exposure.

### Common Use Cases
- Private S3 access from a VPC without a NAT Gateway (gateway endpoint).
- Private DynamoDB access for applications that need low-latency, secure calls.
- Connecting VPCs to services like Lambda, API Gateway, Secrets Manager, and more via interface endpoints.
- Cross-account access to services through PrivateLink.
- PCI/HIPAA environments that must avoid internet transit.

### Pricing & Limits
- Gateway endpoints are free; only normal service data transfer charges apply.
- Interface endpoints are billed per hour per endpoint plus per GB of data processed.
- Each VPC can have multiple endpoints per service/region.
- Interface endpoints create one ENI per subnet where they are deployed.

### Related Services
- [[VPC]]: The network hosting endpoints.
- [[S3]]: Uses gateway endpoints.
- [[DynamoDB]]: Uses gateway endpoints.
- [[NAT Gateway]]: Alternative outbound path that endpoints can replace.
- [[Lambda]]: Commonly accessed via interface endpoints.
- [[Security Groups vs NACLs]]: Security groups attach to interface endpoint ENIs.

### Related Concepts
- Private Connectivity: Traffic stays in AWS network.
- Endpoint Policy: Controls access through the endpoint.
- Interface Endpoint: ENI-based, supports most services.
- Gateway Endpoint: Route-table-based, only S3 and DynamoDB.
- PrivateLink: The technology behind interface endpoints.
