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
| **Data Quality / Hygiene** | ☐ Drop / flag nulls <br>☐ Type casting <br>☐ Trim whitespace <br>☐ Standardise timestamps / time-zones <br>☐ Deduplicate <br>☐ Outlier capping |
| **Enrichment** | ☐ Look-ups / dimension joins <br>☐ Geo-coding <br>☐ Currency conversion <br>☐ ML inference (embedding, sentiment) |
| **Filtering** | ☐ Row, ☐ Column, ☐ Time-window, ☐ PII strip |
| **Aggregations** | ☐ Sum, Avg, Min/Max, Median <br>☐ Window funcs <br>☐ Sessionisation |
| **Restructuring** | ☐ Pivot / Unpivot <br>☐ Flatten nested JSON <br>☐ Explode arrays |
| **Governance** | ☐ Hash / Mask PII <br>☐ Tokenise <br>☐ Apply data contract (schema registry) |
| **Incremental Pattern** | ☐ Append-only <br>☐ Merge-on-read (delta/iceberg) <br>☐ Partition overwrite <br>☐ SCD Type 1/2 <br>☐ Snapshotting |
| **Testing** | dbt tests, Great Expectations, Soda, unit (pytest-sql), integration dry-runs |

---

## 5 · Load / Serve Phase  (choose details)

| Item | Options | Selected |
|------|---------|----------|
| **Destination** | Warehouse, Data Lake, Lakehouse, Feature Store, Relational DB, BI extract, Search index, Message Bus, API | |
| **Load Strategy** | ☐ Append <br>☐ Upsert / MERGE <br>☐ Overwrite <br>☐ Micro-batch <br>☐ Streaming (exactly-once) | |
| **Table Format** | ☐ Native (Snowflake) <br>☐ Delta <br>☐ Iceberg <br>☐ Hudi | |
| **Partition / Cluster Keys** | — | |
| **Retention / TTL** | — | |
| **Post-load Validation** | Row-count check, checksum, statistical compare | |

---

## 6 · Data-Quality Management  🔍
*(keep or extend the matrix; choices already embedded)*

---

## 7 · Orchestration & CI/CD
*(unchanged – list scheduler, triggers, retries, GitOps flow, etc.)*

---

## 8 · Observability, Lineage & Metrics
*(unchanged – pick OpenLineage, DataHub, Monte Carlo, etc.)*

---

## 9 · Security & Compliance
*(unchanged – IAM, encryption, RLS/CLS, masking, audit logs, …)*

---

## 10 · Disaster Recovery & Backfill
*(select RTO/RPO strategy; include replay method for batch vs stream)*

---

## 11 · Cost & FinOps
*(specify slot/credit budgets, optimisation levers, chargeback tags)*

---

## 12 · Runbook & Incident Mgmt
*(pager rotation, escalation, common fixes, post-mortem template)*

---

## 13 · Change Log
| Date | Author | Change | Version |
|------|--------|--------|---------|
| 2025-07-23 | Niles D. | Initial full-choice template | v2.0 |