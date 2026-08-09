#AWS #Service #Migration
### Snowball

Portable data transfer service for moving terabytes to petabytes of data to/from AWS in remote or bandwidth-limited environments. Ruggedized devices (up to 80 TB) shipped for offline loading, then returned for upload to S3. Supports encryption, tamper detection, and high-speed transfer. Previous generation discontinued Nov 2024; Snowball Edge (with compute) limited to existing customers from Nov 7, 2025—new users use DataSync.

### How It Works

- Request a Snowball device via the console; AWS ships it to your site.
- Connect over the network and load data using the Snowball client or S3 API.
- Optionally export data out of AWS by shipping a device to a destination and reading it back.
- Track the device with the embedded E-ink label and ship it back to AWS.
- AWS copies the data into [[S3]] and erases the device to AWS standards.

### Key Features

- Ruggedized, tamper-evident enclosures with TPM-based integrity tracking.
- Up to 80 TB per device (previous generation; current offering is [[Snowball Edge]]).
- End-to-end encryption with keys managed in [[KMS]].
- Tracking of the device location during shipping.
- Fast transfer once connected to the network, far quicker than WAN upload for large datasets.

### Common Use Cases

- One-time bulk migrations of large data sets to [[S3]].
- Moving data out of AWS for backup or to another provider.
- Data center-to-data center transfer when the network is slow or unavailable.
- Seed data loads followed by ongoing sync with [[DataSync]].

### Pricing & Limits

- Service charge per job plus storage per GB-month during device rental.
- Data transfer into AWS is free; outbound is billed.
- Note the deprecation: Snowball (classic) is discontinued; use [[Snowball Edge]] or [[DataSync]] going forward.

### Related Services

- [[S3]]: Primary destination for Snowball data uploads.
- [[Snowcone]]: Smaller (8 TB) device, discontinued Nov 2024.
- [[DataSync]]: Recommended alternative for network-based transfers.
- [[KMS]]: Manages encryption keys for secure data.
- AWS IoT Greengrass: Extends edge capabilities on Snowball Edge.
- [[Snowball Edge]]: Current device generation offering storage and compute.

### Related Concepts

- Offline Data Transfer: Physical shipping to avoid slow networks.
- Data Migration: Efficient for large-scale cloud ingress/egress.
- Edge Computing: Snowball Edge enables local processing before transfer.
- End-to-End Security: Encryption and tracking during transit.
- AWS Global Infrastructure: Devices ship between your site and a chosen AWS region.
