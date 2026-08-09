#AWS #Service #Storage
### S3 Intelligent-Tiering

S3 Intelligent-Tiering is a storage class that automatically moves objects between access tiers based on changing access patterns. It monitors usage per object and transitions frequently accessed objects to a high-frequency tier and infrequently accessed objects to lower-cost tiers, with no retrieval fees and no minimum object size.

### How It Works

- Objects start in the Frequent Access tier, which behaves like S3 Standard.
- S3 monitors access per object and moves it to Infrequent Access after 30 days without access.
- Continued inactivity moves objects to Archive Instant Access after 90 days, then to Archive Access (90 days) and Deep Archive Access (180 days) tiers.
- Objects that become frequently accessed again are automatically moved back to the Frequent Access tier.
- Access to an object resets the inactivity clock that drives tier transitions.

### Key Features

- No retrieval fees and no minimum object size (unlike Standard-IA).
- Automatic tiering without maintaining lifecycle rules.
- Optional Archive Access and Deep Archive Access tiers add further cost savings.
- Optional object-level monitoring and automation features.
- Same 11 nines durability and millisecond first-byte latency for active tiers.

### Common Use Cases

- Data with unpredictable or changing access patterns (e.g., customer uploads, mixed datasets).
- Storage where it is hard to predict which objects will remain hot.
- Long-lived objects that may become cold but must retain fast retrieval.
- A simple way to optimize cost without building custom lifecycle rules.

### Pricing & Limits

- Billed per GB-month of storage plus a small monthly monitoring and automation fee per object.
- Frequent and Infrequent Access tiers provide millisecond access; archive tiers have slower retrieval.
- Archive Access and Deep Archive Access add minimum storage durations (90 and 180 days respectively).
- No retrieval fee applies on any tier.

### Related Services

- [[S3]]: The service hosting the Intelligent-Tiering storage class.
- [[S3 Lifecycle]]: An alternative, rule-based way to automate tier transitions.
- [[S3 Standard]]: The high-frequency tier behaves like Standard.
- [[S3 Standard-Infrequent Access (IA)]]: The Infrequent Access tier has a similar cost profile.
- [[S3 Glacier]]: Archive tiers offer a similar cost profile to Glacier.

### Related Concepts

- Automatic Tiering: Usage-based movement between storage tiers.
- Monitoring & Automation Fee: Per-object monthly charge for the monitoring service.
- Access Monitoring: S3 tracks object access to trigger tier transitions.
- Cost Optimization: Automatically balances storage cost with access latency.
