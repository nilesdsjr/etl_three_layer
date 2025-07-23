# 📄 Modern (2025) ETL / ELT Pipeline Design Document

---

## 🔁 Integration Strategy (select all that apply)

| Phase | Mode | Common Tools / Patterns | Notes |
|-------|------|-------------------------|-------|
| **Ingest** | ☐ Batch <br>☐ Log-based CDC <br>☐ Snapshot Replication <br>☐ Event Stream (Kafka/Pub/Sub/Kinesis) <br>☐ File Drop (SFTP / S3) | Airbyte, Fivetran, Debezium, DMS, NiFi, Flume | — |
| **Transform** | ☐ ELT (dbt / SQL) <br>☐ Spark / PySpark <br>☐ Beam / Dataflow <br>☐ Flink <br>☐ KsqlDB <br>☐ Pandas / Polars <br>☐ Custom Lambda/FaaS | — | — |
| **Serve** | ☐ Warehouse (BQ, Snowflake, Redshift) <br>☐ Lakehouse (Delta, Iceberg, Hudi) <br>☐ Relational DB (Postgres, MySQL) <br>☐ NoSQL (Mongo, DynamoDB) <br>☐ Feature Store (Feast, Vertex FS) <br>☐ Search (OpenSearch, Solr) <br>☐ API / Reverse-ETL | — | — |

> _Document required latency, ordering guarantees, and idempotency._

---

## 1 · Project Context
- **Name / Repo**:  
- **Team & Owners**:  
- **Start / Last Update**:  
- **Stakeholders & SLAs**:  
- **Compliance Tier**: ☐ Public ☐ Internal ☐ PII ☐ PCI/PHI  

---

## 2 · Business Objective
- **Problem / Opportunity**:  
- **Success Metrics (KPIs)**:  
- **Down-stream Consumers**: dashboards, ML models, ops, …  

---

## 3 · Extract Phase  (choose details)

| Item | Options | Selected |
|------|---------|----------|
| **Source Types** | CRM, ERP, SaaS APIs, OLTP DBs, Data Lake files, Social feeds, IoT sensors, Logs, IoT | |
| **Extraction Method** | ☐ Full Dump <br>☐ Incremental (watermark) <br>☐ Source-push / Webhook <br>☐ Log-based CDC <br>☐ Change-Data Snapshots <br>☐ Stream (event queue) | |
| **Trigger** | ☐ Schedule (cron) <br>☐ Event <br>☐ Continuous | |
| **Landing Zone** | s3://bronze/…, gs://…, ADLS, Kafka topic, GCS bucket | |
| **File/Record Format** | CSV, JSON, Parquet, Avro, Protobuf, ORC | |
| **Auth** | IAM role, OAuth, Key/PWD, SSH key, VPN | |
| **Expected Volume / Velocity** | — | |
| **Edge Cases** | soft deletes, schema drift, throttling limits | |

---

## 4 · Transform Phase  (choose details)

| Category | Common Operations (mark all required) |
|----------|---------------------------------------|
| **Data Quality / Hygiene** | ☐ Drop / flag nulls <br