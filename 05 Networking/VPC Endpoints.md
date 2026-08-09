#AWS #Service #Networking
### VPC Endpoints

VPC Endpoints enable private connectivity between a VPC and AWS services (e.g., S3, DynamoDB, Lambda) without traversing the public internet. Gateway endpoints (S3, DynamoDB) and interface endpoints (ENI-based, most services) both keep traffic inside the AWS network.

### Related Services

- [[VPC]]: The network hosting endpoints.
- [[S3]]: Uses gateway endpoints.
- [[DynamoDB]]: Uses gateway endpoints.

### Related Concepts

- Private Connectivity: Traffic stays in AWS network.
- Endpoint Policy: Controls access through the endpoint.
- Interface Endpoint: ENI-based, supports most services.
