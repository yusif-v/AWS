#AWS 
### AWS Snowball

Portable data transfer service for moving terabytes to petabytes of data to/from AWS in remote or bandwidth-limited environments. Ruggedized devices (up to 80 TB) shipped for offline loading, then returned for upload to S3. Supports encryption, tamper detection, and high-speed transfer. Previous generation discontinued Nov 2024; Snowball Edge (with compute) limited to existing customers from Nov 7, 2025—new users use DataSync.

### Related Services

- [[Amazon S3]]: Primary destination for Snowball data uploads.
- [[AWS Snowcone]]: Smaller (8 TB) device, discontinued Nov 2024.
- [[AWS DataSync]]: Recommended alternative for network-based transfers.
- [[AWS Key Management Service (KMS)]]: Manages encryption keys for secure data.
- AWS IoT Greengrass: Extends edge capabilities on Snowball Edge.

### Related Concepts

- Offline Data Transfer: Physical shipping to avoid slow networks.
- Data Migration: Efficient for large-scale cloud ingress/egress.
- Edge Computing: Snowball Edge enables local processing before transfer.
- End-to-End Security: Encryption and tracking during transit.