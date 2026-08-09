#AWS #Service #Storage
### S3 Lifecycle

S3 Lifecycle is a bucket configuration that automatically manages objects over time: transitioning them between storage classes as they age, and expiring or deleting them after a defined period. It reduces storage cost and automates retention without manual intervention.

### How It Works

- Define lifecycle rules on a bucket, scoped by prefix or object tags.
- Transition actions move objects between classes, e.g., Standard → Standard-IA after 30 days → Glacier after 90 days.
- Expiration actions delete objects (or versions) after a set number of days.
- For versioned buckets, rules can act on current versions, previous versions, and expired delete markers.
- Transition actions require a minimum storage duration in the source class (e.g., 30 days in Standard-IA, 90 days in Glacier).
- Rules are evaluated asynchronously and applied to new objects, current versions, and old versions.

### Key Features

- Automates storage cost optimization (tier transitions) and retention/compliance (expiration).
- Supports prefix- and tag-based filtering for granular control.
- Version-aware actions: expire incomplete multipart uploads, previous versions, and delete markers.
- Works across all S3 storage classes, including Intelligent-Tiering and Glacier/Deep Archive.
- Combines with S3 Replication and S3 Object Lock.

### Common Use Cases

- Moving logs to cheaper storage after a retention period.
- Automatically deleting temporary or transient files.
- Archiving old versions of versioned objects to Glacier.
- Enforcing data retention policies for compliance.
- Cleaning up incomplete multipart uploads and expired delete markers.

### Pricing & Limits

- Lifecycle rules themselves are free; you pay normal storage and transition (per 1,000 objects) fees.
- Transition requests are billed per 1,000 objects transitioned.
- Minimum durations: 30 days in Standard-IA/One Zone-IA, 90 days in Glacier/Deep Archive (unless using Intelligent-Tiering).
- A bucket supports up to 1,000 lifecycle rules.

### Related Services

- [[S3]]: The bucket service where lifecycle rules run.
- [[S3 Intelligent-Tiering]]: An automatic per-object tiering alternative.
- [[S3 Glacier]]: Common transition destination for archival.
- [[S3 Deep Archive]]: Final archival tier for lifecycle transitions.
- [[S3 Versioning]]: Lifecycle interacts with object versions.
- [[S3 One Zone-IA]]: Transition target for lower-cost single-AZ storage.

### Related Concepts

- Transition: Moving objects between storage classes.
- Expiration: Automatically deleting objects or versions.
- Filtering: Rules match on prefix and tags.
- Retention: Controlling how long data is kept for compliance.
