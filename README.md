# 📄 Modern (2025) ETL / ELT Pipeline Design Doc

---

## 🔁 Integration Strategy  
| Phase | Mode | Tools / Patterns |
|-------|------|------------------|
| **Ingest** | `☐ Batch  ☐ Log-based CDC  ☐ Stream (Kafka/PubSub)` | Fivetran / Airbyte / DMS / Debezium |
| **Transform** | `☐ ELT (dbt)  ☐ Spark  ☐ Beam  ☐ Flink  ☐ Pandas` |
| **Serve** | `☐ Warehouse  ☐ Lakehouse  ☐ Feature Store  ☐ API` |

> _Document latency target, exactly-once guarantees, and idempotency logic._

---

## 1 · Project Context  
- **Name**:   
- **Repository**: `git@…`  
- **Team / Owners**:   
- **Start / Last Update**:   
- **Stakeholders & SLAs**: e.g. <5 min freshness, 99.9 % uptime  
- **Domains / Data Products**:   
- **Compliance Tier**: `☐ Public ☐ Internal ☐ PII ☐ PCI/PHI`  

---

## 2 · Business Objective  
- **Problem / Opportunity**:   
- **Success Metrics (KPIs)**:   
- **Downstream Consumers**: dashboards, ML models, reverse ETL, etc.  

---

## 3 · Source-to-Landing (Bronze)  
| Source | Type | Change-detection | Connector | Landing Path | Notes |
|--------|------|-----------------|-----------|--------------|-------|
| … | DB | Log-based CDC | DMS | `s3://bronze/db/table/` | handle deletes with soft-flags |

- **Auth**: IAM role / secret manager  
- **Expected Volume & Growth**: e.g. 50 GB/day  
- **Schema Contract**: Avro / Protobuf versioned in Schema Registry  

---

## 4 · Transformation (Silver)  
- **Incremental Logic**: `dbt incremental` / merge-on-read  
- **Enrichment / Joins**: …  
- **Staging Format**: Parquet + Iceberg table (snapshot isolation)  
- **Unit Tests**: spark-tests, dbt unit, pytest-sql  

---

## 5 · Curated (Gold) & Semantic Layer  
- **Model Type**: `☐ Star  ☐ Data Vault  ☐ Wide Table`  
- **Metrics Defined** (semantic layer / dbt metrics): revenue, LTV, …  
- **Slowly Changing Dimension Strategy**: SCD Type 2 via MERGE  

---

## 6 · Data-Quality Management  🔍
| Check | Layer | Owner | Severity | Threshold | Action / Auto-remediation |
|-------|-------|-------|----------|-----------|---------------------------|
| Not-null `customer_id` | Silver | Data Eng | **Error** | 0 null rows | Fail task; roll back write |
| Freshness < 15 min | Gold | Platform | **Warn** | `MAX(ingest_time)` | Alert Slack `#data-alerts` |
| Duplicate PK rows | Silver | Data Eng | **Error** | 0 duplicates | Run de-dupe script + notify |
| PII leakage | Bronze | Security | **Block** | 0 matches | Route to quarantine bucket |
| Volume variance ±20 % | Bronze | Data Eng | **Warn** | window 7 d | Auto-open JIRA ticket |

- **Tooling**: Great Expectations / Soda-Core / dbt tests  
- **Quality SLAs**: 99 % tests pass; fix critical issues < 4 h  
- **Anomaly Detection**: Monte Carlo / Databand freshness & volume monitors  
- **Escalation Policy**: On-call engineer → Platform SRE after 30 min  

---

## 7 · Load / Serve  
| Target | Write-Mode | Partition / Cluster | Retention |
|--------|-----------|---------------------|-----------|
| BigQuery | MERGE | `date` partition, cluster by `customer_id` | 730 days |
| FeatureStore | Upsert | key=`cust_id` | latest only |

- **Post-Load Validation**: row-count match ±0.1 %, checksum diff = 0  

---

## 8 · Orchestration & CI/CD  
- **Scheduler**: Airflow 2.9 / Dagster / Prefect  
- **Trigger**: `☐ Cron  ☐ Event (PubSub)  ☐ On-Commit`  
- **Retries / SLA Miss Callback**: 3× exponential backoff, notify Slack  
- **Deployment**: GitHub Actions → Terraform → DAG dry-run → Prod  
- **Environments**: dev → staging → prod using data “sandboxes”  

---

## 9 · Observability, Lineage & Metrics  
- **Lineage & Catalog**: OpenLineage + DataHub (auto-populated)  
- **Dashboards**: Grafana → _etl_latency_seconds_, _rows_dropped_total_  
- **Log Aggregation**: Cloud Logging / Loki → centralized SIEM  
- **Alert Routing**: PagerDuty for SEV-1, Slack for SEV-2/3  

---

## 10 · Security & Compliance  
- **IAM Roles**: least privilege, service accounts per DAG  
- **Encryption**: At rest (KMS) & in transit (TLS 1.3)  
- **Row/Column Level Security**: BQ RLS / Snowflake Secure Views  
- **Data Masking / Tokenization**: yes for PII columns  
- **Audit Logs**: routed to SOC for 90 days  

---

## 11 · Disaster Recovery & Backfill  
| Asset | RTO | RPO | Strategy |
|-------|-----|-----|----------|
| Warehouse | 1 h | 15 min | point-in-time restore, snapshots |
| Streaming | 5 min | 0 min | Kafka topic replication (3×) |

- **Backfill Plan**: replay CDC logs from offset X  

---

## 12 · Cost & FinOps  
- **Budget Owner**:   
- **Cost Monitors**: BQ slots, Snowflake credits, S3 storage  
- **Optimization Levers**: partition pruning, materialized views, workload-manager rules  
- **Monthly Spend Target**: USD ____  

---

## 13 · Runbook & Incident Mgmt  
- **Pager Rotation**: @data-oncall  
- **Common Failures & Fixes**: connection timeout, schema drift  
- **Escalation Ladder**: L1 Data Eng → L2 Platform ☏ → L3 DevOps  
- **Handover Docs**: DAG diagram, KB article, Post-mortem template  

---

## 14 · Change Log  
| Date | Author | Change | Version |
|------|--------|--------|---------|
| 2025-07-23 | Niles D. | Initial draft | v1.0 |
| 2025-07-23 | Niles D. | Added Data-Quality section | v1.1 |