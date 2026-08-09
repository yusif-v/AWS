#AWS #Service #Storage
### S3 Versioning

S3 Versioning keeps multiple versions of an object in a bucket whenever it is written or deleted. It protects against accidental overwrites and deletions, supports recovery of prior versions, and is a prerequisite for replication and S3 Object Lock.

### How It Works

- When enabled on a bucket, every PUT creates a new version, and DELETE adds a delete marker instead of removing data.
- Each version has a unique version ID; you can retrieve, delete, or restore any specific version.
- Old versions are retained until explicitly deleted, so storage grows with object churn.
- Previous versions and current versions can be managed with independent lifecycle rules.
- Versioning can be suspended (stops creating new versions) but cannot be disabled once enabled.
- MFA Delete adds an extra layer, requiring MFA to change versioning state or permanently delete versions.

### Key Features

- Recovery from accidental deletes and overwrites.
- Prerequisite for S3 Replication and S3 Object Lock.
- Version-aware lifecycle rules (current vs. previous versions, expired delete markers).
- MFA Delete for extra protection against destructive operations.
- Works with bucket policies to restrict access by version.
- Retrieve previous versions via the console, CLI, or API.

### Common Use Cases

- Protecting critical data against accidental overwrite.
- Recovering from ransomware or malicious deletion (with MFA delete).
- Auditing changes to objects over time.
- Keeping historical versions for compliance.
- Enabling replication and object lock.

### Pricing & Limits

- You pay for storage of all retained versions, so heavy version churn increases cost.
- Lifecycle rules can expire previous versions to control cost.
- Once enabled, versioning cannot be disabled, only suspended.

### Related Services

- [[S3]]: Hosts versioned objects.
- [[S3 Replication]]: Requires versioning on source and destination.
- [[S3 Lifecycle]]: Manages previous versions and delete markers.
- [[S3 Encryption]]: Applies to each version independently.
- [[S3 Access Control]]: Permissions apply per object version.

### Related Concepts

- Object Version: A distinct copy of an object with a version ID.
- Delete Marker: Marker left by DELETE instead of removing data.
- MFA Delete: Multi-factor protection for destructive operations.
- Version Suspension: Stops new versions without disabling the feature.
- Recovery: Restoring a previous version after accidental loss.
