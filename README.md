# 📄 **Modern (2025) ETL / ELT Pipeline Design Document**

Use this doc to capture every design decision—from source-system quirks to SLAs and on-call playbooks.  
Delete any row or checkbox that doesn’t apply after you finish design reviews.

---

## 🔁 **Integration Strategy**

| Phase | Mode (☑ choose) | Common Tools / Patterns | Latency Target (ms / min / hr) | Notes |
|-------|-----------------|-------------------------|--------------------------------|-------|
| **Ingest** | ☐ **Batch** (dump) <br>☐ **Incremental** (watermark) <br>☐ **Log-based CDC** <br>☐ **Snapshot replication** <br>☐ **Event stream** (Kafka / PubSub / Kinesis) <br>☐ **File drop** (SFTP / S3) | Airbyte · Fivetran · Debezium · Database DMS · NiFi | | |
| **Transform** | ☐ **ELT** (dbt / SQL) <br>☐ **Spark / PySpark** <br>☐ **Beam / Dataflow** <br>☐ **Flink** <br>☐ **KsqlDB** <br>☐ **Pandas / Polars** <br>☐ **Custom FaaS / Lambda** | - | | |
| **Serve** | ☐ **Warehouse** (BigQuery · Snowflake · Redshift) <br>☐ **Lakehouse** (Delta · Iceberg · Hudi) <br>☐ **Data Lake** (S3 + Glue, GCS + Dataplex) <br>☐ **Relational DB** (PostgreSQL · MySQL) <br>☐ **NoSQL** (Mongo · DynamoDB · Cassandra) <br>☐ **Feature Store** (Feast · Vertex FS) <br>☐ **Search / Vector DB** (OpenSearch · Pinecone) <br>☐ **API / Reverse-ETL** | - | | |

> **Guarantees**: idempotent writes ? · exactly-once / at-least-once · ordering constraints · back-pressure plan.

---

## 1 · **Project Context**

| Field | Value |
|-------|-------|
| **Project / Repo** |  |
| **Team / Owners** |  |
| **Start Date** |  |
| **Last Updated** |  |
| **Stakeholders & SLAs** | e.g. < 5 min freshness · 99.9 % uptime |
| **Compliance Tier** | ☐ Public ☐ Internal ☐ PII ☐ PCI / PHI |

---

## 2 · **Business Objective**

*Goal, success metrics, and who uses the output.*

|                                |                                         |
|--------------------------------|-----------------------------------------|
| **Problem / Opportunity**      |                                         |
| **KPIs / Metrics Produced**    | revenue, churn-rate, MAU, …             |
| **Down-stream Consumers**      | dashboards, ML models, finance exports  |

---

## 3 · **Extract Phase**

| Item | Options / Examples | Your Selection & Notes |
|------|--------------------|------------------------|
| **Source Systems** | CRM · ERP · SaaS APIs · OLTP DBs · Data-lake files · Social feeds · IoT sensors · Logs | |
| **Extraction Method** | ☐ Full dump <br>☐ Incremental (watermark) <br>☐ Source-push / Webhook <br>☐ Log-based CDC <br>☐ Stream events | |
| **Trigger** | ☐ Schedule (cron) <br>☐ Event based <br>☐ Continuous stream | |
| **Landing Zone** | `s3://bronze/...` · `gs://bronze/...` · ADLS Gen2 · Kafka topic | |
| **Record / File Format** | CSV · JSON · Parquet · Avro · Protobuf · ORC | |
| **Authentication** | IAM role · OAuth2 · Service Account key · SSH key · VPN | |
| **Expected Volume & Velocity** | ___ GB / day ; peak ___ msg / s | |
| **Edge-case Handling** | soft deletes · high watermark reset · API rate-limit | |

---

## 4 · **Transform Phase** *(“Silver”)*

| Category | Check all that apply / describe |
|----------|---------------------------------|
| **Hygiene / Quality** | ☐ Drop / flag nulls ☐ Type-cast ☐ Trim whitespace ☐ Time-zone standardise ☐ Deduplicate ☐ Outlier capping |
| **Enrichment** | ☐ Dim-table joins ☐ Geo-enrich ☐ Currency FX ☐ ML inference (sentiment, embeddings) |
| **Filtering** | ☐ Row filter ☐ Column filter ☐ Time-window ☐ PII strip / hash |
| **Aggregation & Windowing** | ☐ Sum ☐ Avg ☐ Min/Max ☐ Median ☐ Percentiles ☐ Sessionisation |
| **Restructuring** | ☐ Pivot / Unpivot ☐ Flatten JSON ☐ Explode arrays |
| **Incremental Pattern** | ☐ Append-only ☐ Merge-on-read (Delta/Iceberg) ☐ Partition overwrite ☐ SCD Type 1 ☐ SCD Type 2 ☐ Periodic snapshot |
| **Governance Actions** | ☐ Schema contract validation ☐ PII masking / tokenisation |
| **Data-quality Tests** | dbt tests · Great Expectations · Soda-SQL · pytest-sql |
| **Processing Engine** | Spark · dbt · Beam · Flink · Pandas · Polars | |

---

## 5 · **Load / Serve Phase** *(“Gold” & downstream)*

| Field | Options | Selection |
|-------|---------|-----------|
| **Destination** | Warehouse · Lakehouse · Relational DB · Feature Store · Search index · API | |
| **Load Strategy** | ☐ Append ☐ Upsert / MERGE ☐ Overwrite ☐ Micro-batch ☐ Streaming (exactly-once) | |
| **Table Format** | ☐ Native (Snowflake) ☐ Delta ☐ Iceberg ☐ Hudi | |
| **Partition / Cluster Keys** | e.g. `event_date`, `customer_id` | |
| **Retention / TTL** | e.g. 730 days · GDPR delete policy | |
| **Post-load Validation** | row-count ±0.1 % · checksum diff · metric parity | |
| **Semantic Layer / Metrics** | dbt metrics · LookML · Cube.js · MetricFlow | |

---

## 6 · **Data-Quality Management 🔍**

| Check | Layer | Owner | Severity | Threshold | Auto-remediation / Action |
|-------|-------|-------|----------|-----------|---------------------------|
| Not-null `customer_id` | Silver | Data Eng | **Error** | 0 nulls | Fail job, rollback |
| Freshness < 15 min     | Gold   | Platform | Warn      | 15 min  | Alert Slack #data-alerts |
| Volume variance ±20 %  | Bronze | Data Eng | Warn      | ±20 %   | Auto-open JIRA ticket |
| Duplicate PK rows      | Silver | Data Eng | **Error** | 0 rows | Run de-dupe script |
| PII leakage            | Bronze | SecOps  | Block     | 0 hits | Quarantine bucket |

*Tooling:* Great Expectations · Soda-Core · dbt tests · Monte Carlo · Databand  
*Quality SLA:* ≥ 99 % tests pass; fix *critical* issues < 4 h.

---

## 7 · **Orchestration & CI/CD**

| Item | Details |
|------|---------|
| **Scheduler** | Airflow 2.x · Prefect 2 · Dagster · Cloud Composer |
| **Trigger Types** | ☐ Cron ☐ Event (Pub/Sub) ☐ On-commit CI |
| **Retries & SLA Miss** | 3× exponential back-off · on-fail callback →
Slack · SLA 15 min |
| **Envs & Promotion** | dev → staging → prod (data sandboxes) |
| **CI Pipeline** | GitHub Actions → Terraform plan/apply → DAG lint →
unit + integration tests |

---

## 8 · **Observability, Lineage & Metrics**

| Aspect | Tooling / Endpoint |
|--------|-------------------|
| **Lineage** | OpenLineage · DataHub · Marquez |
| **Data Catalog** | DataHub · Amundsen · Dataplex |
| **Dashboards** | Grafana / Cloud Monitoring: `etl_latency_seconds`,
`rows_dropped_total` |
| **Alert Routing** | PagerDuty (SEV-1) · Slack (SEV-2/3) |
| **Log Aggregation** | Cloud Logging · Loki → central SIEM |

---

## 9 · **Security & Compliance**

| Domain | Controls |
|--------|----------|
| **IAM / RBAC** | Least-privilege service accounts per DAG |
| **Encryption** | At-rest (KMS/CMEK) · In-transit (TLS 1.3) |
| **Row / Column Level Security** | BQ RLS · Snowflake Secure Views |
| **Data Masking / Tokenisation** | Hash PII, vault tokens |
| **Audit Logs** | Route to SOC; retain ≥ 90 days |
| **Regulations** | GDPR · LGPD · HIPAA (if applicable) |

---

## 10 · **Disaster Recovery & Backfill**

| Asset | RTO | RPO | Strategy |
|-------|-----|-----|----------|
| Warehouse | 1 h | 15 min | point-in-time restore, snapshots |
| Streaming  | 5 min | 0 min | Kafka 3× replication, mirror-topics |

*Backfill Plan:* replay CDC logs from offset X; historical S3 manifests.

---

## 11 · **Cost & FinOps**

| Item | Details |
|------|---------|
| **Budget Owner** | |
| **Monthly Spend Target** | USD ___ |
| **Cost Monitors** | BQ slots · Snowflake credits · S3 storage |
| **Optimisation Levers** | partition pruning · materialised views · workload-manager rules |
| **Chargeback Tags** | `env`, `owner`, `product` |

---

## 12 · **Runbook & Incident Management**

| Topic | Info |
|-------|------|
| **Pager Rotation** | @data-oncall (Opsgenie schedule #123) |
| **Common Failures** | connection timeout, schema drift, API rate-limit |
| **Escalation Ladder** | L1 Data Eng → L2 Platform SRE → L3 DevOps |
| **Handover Docs** | DAG diagram · KB article · Post-mortem template |

---

## 13 · **Change Log**

| Date | Author | Change | Version |
|------|--------|--------|---------|
| YYYY-MM-DD | Name | Initial template | v1.0 |
| YYYY-MM-DD | Name | — | — |