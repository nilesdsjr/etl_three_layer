# 📄 ETL Pipeline Design Documentation Template

---

## 🔁 Phases in ETL

### 1. Extract
Retrieves and verifies data from each source, including CRM, APIs, databases, logs, and platforms.

- **Full extraction**: all records from the source
- **Source-driven extraction**: triggered by source system changes
- **Incremental extraction**: only new or changed records since last run

### 2. Transform
Cleans, merges, filters, and aggregates data for analytical use.

- **Cleaning**: normalize types, remove nulls
- **Merging**: join tables from multiple sources
- **Filtering**: keep relevant records only
- **Aggregation**: group by metrics such as sums, averages, min, max

### 3. Load
Loads processed data into target destinations.

- Can be flat files, SQL databases, cloud warehouses (e.g., BigQuery)

---

## 1. Project Context

- **Project Name**:  
- **Author / Team**:  
- **Start Date**:  
- **Last Updated**:  
- **Stakeholders**:  
- **Frequency**: `☐ Real-time ☐ Daily ☐ Weekly`  
- **Pipeline Type**: `☐ ETL ☐ ELT ☐ Batch ☐ Stream`  

---

## 2. Business Objective

- **Goal**:  
- **KPIs / Metrics Produced**:  
- **Consumers**:  

---

## 3. Extract Phase

- **Source Systems**:  
- **Extraction Method**: `☐ Full ☐ Incremental ☐ Source-driven`  
- **Authentication / Access**:  
- **Landing Zone Path (Bronze)**:  
- **Extraction Notes / Challenges**:  

---

## 4. Transform Phase

- **Cleaning Steps**: `☐ Drop nulls ☐ Normalize ☐ Deduplication`  
- **Joins / Enrichment**:  
- **Filtering Logic**:  
- **Aggregations**:  
- **Transformation Tools**: `☐ Spark ☐ Beam ☐ dbt ☐ Pandas ☐ SQL`  
- **Staging Zone Path (Silver)**:  

---

## 5. Load Phase

- **Target Destination**: `☐ BigQuery ☐ Snowflake ☐ PostgreSQL ☐ Cloud Storage`  
- **Load Strategy**: `☐ Overwrite ☐ Append ☐ Merge / SCD`  
- **Data Model**: `☐ Star Schema ☐ Flat Table`  
- **Partitioning / Clustering Strategy**:  
- **Post-load Validation**:  

---

## 6. Scheduling & Orchestration

- **Tool Used**: `☐ Airflow / Composer ☐ Cloud Scheduler ☐ Prefect`  
- **Trigger Type**: `☐ Time-based ☐ Event-based`  
- **Retry Policy / SLA**:  
- **Monitoring Integration**:  

---

## 7. Cost, Monitoring & Maintenance

- **Cost Optimization**:  
  - `☐ Partitioned tables ☐ Materialized views ☐ Filter pushdown`  
- **Data Quality Checks**: `☐ Great Expectations ☐ SQL tests`  
- **Alerting Rules**: `☐ Slack ☐ Email ☐ PagerDuty`  

---

## 8. Security & Governance

- **IAM Role Definitions**:  
- **Encryption**: `☐ CMEK ☐ Default encryption`  
- **Lineage Tools**: `☐ Dataplex ☐ Data Catalog`  
- **PII Handling / Compliance**:  

---

## 9. Outputs / Dashboards

- **BI Tools Connected**: `☐ Looker ☐ Tableau ☐ Power BI ☐ Superset`  
- **KPIs Delivered**:  
- **Data Products Produced**: `☐ Datasets ☐ Dashboards ☐ API / file exports`  

---

## 10. Change Log & Future Work

- **Git Repo / Versioning**:  
- **Schema Changes**:  
- **Enhancement Backlog**:  
- **Handoff Materials**:  
  - `☐ Runbook ☐ DAG diagram ☐ Readme / onboarding guide`