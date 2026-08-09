#AWS #Service #Database
### DynamoDB Streams

DynamoDB Streams captures item-level changes (create, update, delete) in a time-ordered stream. Applications can consume these events to trigger workflows, replicate data, or maintain analytics, and stream records are retained for 24 hours.

### Related Services

- [[DynamoDB]]: The source table for changes.
- [[Lambda]]: Processes stream records via event source mapping.
- [[Kinesis]]: Alternative streaming data pipeline.

### Related Concepts

- Change Data Capture: Recording modifications.
- Event-Driven Architecture: React to table changes.
- Streams TTL: 24-hour record retention.
