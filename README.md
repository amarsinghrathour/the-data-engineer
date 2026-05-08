# The Data Engineer

**From zero to production-ready data engineer**

A complete, hands-on, project-first course designed to take you from beginner to job-ready data engineer.

## 🟢 Getting Started

### Prerequisites

- Python 3.10+
- Git
- Docker (optional but recommended)

### Setup

```bash
git clone https://github.com/amarsinghrathour/the-data-engineer.git
cd the-data-engineer
pip install -r requirements.txt
```

Reusable local fixtures live in **`resources/datasets/`** (single source of truth for notebook/project sample data).

### PostgreSQL (Phase 2 — SQL)

Before `notebooks/02_sql/`, start PostgreSQL (Docker one-liner and connection check): see **[`notebooks/02_sql/README.md`](notebooks/02_sql/README.md)** and run `python scripts/test_postgres_connection.py` when the container is up.

### Apache Spark (Phase 4 — big data)

Install deps (`pyspark` is in `requirements.txt`). For local Spark you may need **JDK 11+** — see **[`notebooks/04_spark/README.md`](notebooks/04_spark/README.md)** and run the smoke test there before opening `01_spark_basics.ipynb`.

### Apache Airflow (Phase 5 — orchestration)

Run Airflow with Docker — see **[`airflow/README.md`](airflow/README.md)** (`docker compose up` in `airflow/`, UI at **http://localhost:8080**) before `notebooks/05_airflow/`.

### Apache Kafka (Phase 6 — streaming)

Run Kafka with Docker — see **[`kafka/README.md`](kafka/README.md)** (`docker compose up` in `kafka/`, broker at **localhost:9092**) before `notebooks/06_kafka/`.

### Cloud (Phase 7 — deployment mindset)

Start with **[`notebooks/07_cloud/README.md`](notebooks/07_cloud/README.md)** and choose one provider (AWS recommended in this course). Focus on storage (`S3`), compute (`EC2`/`Lambda`), and database (`RDS`) mapping to your existing pipelines.

### Data Quality (Phase 8 — production reliability)

Start with **[`notebooks/08_data_quality/README.md`](notebooks/08_data_quality/README.md)** to add validation, rejection handling, and quality metrics to your pipelines.

### Final Capstone v2 (Phase 9 — interview-ready system)

Start with **[`notebooks/09_final_capstone/README.md`](notebooks/09_final_capstone/README.md)** for the upgraded end-to-end platform blueprint.

### 🧠 How to Use This Course

Each module contains:

- Concept notebook  
- Practice notebook  
- Assignment  

Follow **in order**. **Do not skip projects.**

## Course overview

By the end of this course you will be able to:

- Build real-world data pipelines (**batch** and **streaming**)
- Work with industry tools (**SQL**, **Spark**, **Airflow**, **Kafka**, **cloud**)
- Reason about **system design** and **scaling**
- Enter interviews with **portfolio proof** and structured preparation

## Who this course is for

- Beginners with no data engineering experience
- Backend engineers switching to data
- Students preparing for data roles
- Anyone tired of theory-only courses

## Tech stack covered

| Area | Tools |
|------|--------|
| Languages | Python, SQL (PostgreSQL) |
| Libraries | Pandas |
| Big data | Apache Spark |
| Orchestration | Apache Airflow |
| Streaming | Apache Kafka |
| Containers | Docker |
| Cloud | AWS / Azure / GCP (basics) |

## Repository structure

```text
the-data-engineer/
├── README.md
├── roadmap.md
├── airflow/
├── kafka/
├── datasets/
├── notebooks/
│   ├── 00_foundations/
│   ├── 01_python/
│   ├── 02_sql/
│   ├── 03_etl/
│   ├── 04_spark/
│   ├── 05_airflow/
│   ├── 06_kafka/
│   ├── 07_cloud/
│   ├── 08_data_quality/
│   ├── 09_capstone/
│   └── 09_final_capstone/
├── projects/
├── interview_prep/
└── resources/
```

See [`roadmap.md`](roadmap.md) for the high-level phase list.

## Notebook standard

Every notebook in `notebooks/` follows the same pedagogical skeleton (details in [`notebooks/README.md`](notebooks/README.md)):

1. Concept explanation  
2. Real-world analogy  
3. Code examples  
4. Practice problems  
5. Assignment  
6. Interview questions  
7. **Your tasks** — end-of-lesson checklist so learners know exactly what to do before moving on (`notebooks/README.md`)

## Interview preparation

The `interview_prep/` folder supports:

- SQL deep dives  
- Python problem-solving  
- System design prompts  
- Debugging scenarios  

Example themes: design a large-scale data pipeline, handle late-arriving data, optimize a slow Spark job.

Start with **`interview_prep/quick_revision.md`** for a fast pre-interview refresh.

## Evaluation system

| Component | Weight |
|-----------|--------|
| Assignments | 30% |
| Projects | 50% |
| Interview quizzes | 20% |

## Included projects

- Batch ETL pipeline  
- Streaming pipeline (Kafka)  
- Cloud deployment  
- Final capstone system (**e-commerce data platform**: events → Kafka → Spark → data lake → warehouse → dashboard)

## Learning philosophy

- Think like an engineer  
- Design for failure and recovery  
- Design scalable systems  
- Write production-ready code  

## Final outcome

Completing this course gives you:

- A strong **GitHub portfolio**  
- **Real-world** data engineering projects  
- Interview confidence grounded in **artifacts**, not buzzwords  
- **Production-level** intuition for pipelines and platforms  

---

Start with [`roadmap.md`](roadmap.md) **Phase 0**, then open `notebooks/00_foundations/`.
