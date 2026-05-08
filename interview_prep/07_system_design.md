# Data Engineering System Design

Q: Design a data pipeline

Answer:

- Source -> API / Kafka
- Ingestion -> ETL / streaming
- Storage -> S3 + DB
- Processing -> Spark
- Orchestration -> Airflow

---

Q: Batch vs Streaming?

Batch:
- scheduled
- large data

Streaming:
- real-time
- continuous

---

Q: How do you scale?

- partitioning
- distributed systems
- parallel processing
