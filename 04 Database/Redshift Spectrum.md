#AWS #Service #Database
### Redshift Spectrum

Redshift Spectrum lets you run SQL queries directly against data in S3 without loading it into Redshift. It uses the Redshift cluster to coordinate queries while massively parallel nodes scan S3, enabling petabyte-scale analytics over a data lake.

### Related Services

- [[Redshift]]: The cluster that runs Spectrum queries.
- [[S3]]: The data lake being queried.
- [[Athena]]: Serverless alternative for S3 queries.

### Related Concepts

- Data Lake: Querying raw data in S3.
- External Tables: Tables backed by S3.
- ELT/ETL: Spectrum avoids loading data.
