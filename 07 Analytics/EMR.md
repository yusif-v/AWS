#AWS #Service #Analytics
### EMR

Amazon EMR (Elastic MapReduce) is a managed big-data platform for running open-source frameworks like Apache Spark, Hadoop, Hive, and Flink. It processes large data sets stored in S3, scales clusters on EC2, and is used for ETL, machine learning, and log analysis.

### How It Works

- EMR provisions clusters of EC2 instances pre-configured with big-data frameworks such as Spark, Hadoop, Hive, Flink, Presto, and HBase.
- Cluster types include transient clusters (run the job, then terminate) and long-running clusters for persistent workloads.
- Master and core/task nodes distribute computation; task nodes can be scaled independently, often with Spot capacity.
- Data is read from and written to S3 or HDFS, keeping transient clusters aligned to job duration and cost.
- Clusters can be launched via console, CLI, API, CloudFormation, or the EMR Serverless runtime without provisioning nodes.

### Key Features

- Open-source compatibility: Runs the same engines, tools, and APIs teams already use.
- Managed scaling: Auto-scaling adjusts cluster resources to workload demand.
- Spot instance integration: Task nodes run on lower-cost EC2 Spot capacity.
- EMR Serverless: Optionally runs Spark and Hive jobs without managing clusters.
- Integration with S3, the Glue Data Catalog, and many storage and compute services.
- Built-in monitoring through CloudWatch metrics and cluster logs.

### Common Use Cases

- Large-scale ETL and data transformation pipelines.
- Machine learning data preparation with Spark (Spark MLlib).
- Log and clickstream analysis across very large datasets.
- Running Hive/Pig/SQL workloads over big data.
- Petabyte-scale analytics when pure SQL services are insufficient.

### Pricing & Limits

- Billed as per-hour EC2 instance pricing plus an EMR software surcharge per instance.
- Transient clusters and Spot task nodes reduce total cost.
- EMR Serverless bills per amount of vCPU and memory consumed by jobs.
- Cluster size and instance limits follow EC2 quotas.

### Related Services

- [[S3]]: Source and destination for processed data.
- [[EC2]]: Backs EMR cluster nodes.
- [[Glue]]: Serverless ETL alternative.
- [[Athena]]: SQL alternative for querying data in S3.
- [[Redshift]]: Data warehousing destination for processed data.
- [[Lake Formation]]: Governs the data lake EMR processes.

### Related Concepts

- Cluster: Managed set of EC2 nodes.
- Spark/Hadoop: Open-source processing engines.
- Spot Instances: Lower-cost cluster nodes.
- Big Data: High-volume, high-velocity data processing at scale.
- ETL: Extract, transform, load pipelines at scale.
