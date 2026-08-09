#AWS #Service #Storage
### S3 Transfer Acceleration

S3 Transfer Acceleration speeds up uploads to S3 by routing traffic through AWS edge locations. It uses optimized network paths instead of direct internet routes, reducing latency for long-distance or large-object transfers.

### How It Works

- Uploads are sent to a nearby AWS edge location (CloudFront's global network) using an accelerated endpoint.
- The edge location forwards data to the destination bucket over AWS's optimized backbone network.
- Best for large files, many files, or uploads from geographically distant clients.
- The source bucket must have Transfer Acceleration enabled; clients use the `s3-accelerate` endpoint.
- A speed comparison tool lets you test whether acceleration improves transfer time.

### Key Features

- Reduced latency and improved throughput for long-distance uploads.
- Uses the AWS global network backbone instead of the public internet.
- Simple per-bucket opt-in; no client-side changes beyond using the accelerated endpoint.
- Automatic, seamless failover between network paths.
- Supports all S3 storage classes and access mechanisms.

### Common Use Cases

- Uploading large media or data files from far-flung regions.
- Moving on-premises data to S3 faster from remote locations.
- Publishing content to a central bucket from distributed sources.
- Improving upload throughput for latency-sensitive applications.

### Pricing & Limits

- Billed per GB accelerated (data transferred through the edge network); no charge when the feature is unused.
- Speed benefits are greatest for cross-region and high-bandwidth transfers.
- Not beneficial for uploads within the same region or where the source is already close to the bucket.

### Related Services

- [[S3]]: The target bucket for accelerated uploads.
- [[CloudFront]]: Edge locations used for acceleration.

### Related Concepts

- Edge Locations: PoPs that optimize network paths.
- Upload Throughput: Faster for cross-region transfers.
- Accelerated Endpoint: Uses an `s3-accelerate` endpoint domain.
- Global Network: AWS backbone between the edge and the region.
