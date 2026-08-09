#AWS #Service #Migration
### Snowcone

Discontinued (effective November 12, 2024) ultra-portable, rugged edge device for data transfer and computing in remote environments. Offered 8 TB storage, local EC2/Lambda processing, and secure upload to S3. Battery-powered for IoT, analytics, or small migrations. Use alternatives like AWS DataSync or Snowball.

### How It Works

- Shipped to the user like other Snow family devices, with an 8 TB capacity.
- Connected locally and used with the S3-compatible interface or as a compute node.
- Supported lightweight EC2 instances and [[Lambda]] for on-device processing.
- Data uploaded to [[S3]] when the device returns to AWS.
- Note for study: the device is deprecated, so focus on the alternatives.

### Key Features

- Ultra-portable form factor (about the size of a hard drive) for travel and field use.
- Battery or AC powered, ideal for mobile or off-grid locations.
- 8 TB of encrypted storage with [[KMS]]-managed keys.
- Local compute via EC2 instances and [[Lambda]].
- Tamper-evident and ruggedized for harsh environments.

### Common Use Cases

- Small migrations of a few terabytes to [[S3]].
- Edge processing on a device that can be carried in a backpack.
- Data collection at remote sites with intermittent connectivity.

### Pricing & Limits

- Historical: per-job fee plus storage per GB-month for the rental period.
- Now discontinued; AWS recommends [[DataSync]] for network transfers and [[Snowball]]/[[Snowball Edge]] for larger offline needs.
- Capacity limited to 8 TB, so not suitable for very large datasets.

### Related Services

- [[S3]]: Destination for data uploads.
- [[Snowball]]: Larger alternative for data transfer.
- [[DataSync]]: Network-based transfer replacement.
- AWS IoT Greengrass: For edge computing needs.
- [[Snowball Edge]]: Current device with storage and compute capabilities.

### Related Concepts

- Edge Computing: Local data processing in disconnected areas.
- Offline Data Transfer: Physical shipping for low-connectivity.
- Data Security: Encryption during transit.
- Service Deprecation: Migrate to current AWS options.
- Snow Family: The family of physical transfer devices now led by [[Snowball Edge]].
