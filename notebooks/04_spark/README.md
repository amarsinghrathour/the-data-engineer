# Phase 4 — Big data (Apache Spark)

**Weeks 12–14**

Learn how data is processed **at scale**: distributed execution, Spark DataFrames, SQL on big data, tuning — and why Spark shows up in almost every large analytics stack.

**Project:** large-scale dataset processing (`05_spark_project.ipynb`).

---

## Setup (do this first)

### Install PySpark

From the repo root:

```bash
pip install -r requirements.txt
```

(`pyspark` is listed in `requirements.txt`.)

### Java (local mode)

Spark needs a **JVM**. If `SparkSession` fails with a Java-related error, install **JDK 11 or 17** (not only JRE) and ensure `JAVA_HOME` points at it.

### Smoke test

```bash
python -c "from pyspark.sql import SparkSession; SparkSession.builder.appName('test').getOrCreate().stop(); print('OK')"
```

Or run the first cells of `01_spark_basics.ipynb`.

---

## Notebooks (in order)

| File | Topic |
|------|--------|
| `01_spark_basics.ipynb` | Sessions, DataFrames, lazy vs eager |
| `02_dataframes_and_transformations.ipynb` | Load JSON, transforms, write datasets |
| `03_spark_sql.ipynb` | Temp views, SQL, joins, windows |
| `04_spark_optimization.ipynb` | Cache, shuffle, broadcast, explain |
| `05_spark_project.ipynb` | Synthetic scale + Parquet + SQL capstone |

Follow [`../README.md`](../README.md) — each notebook ends with **Your tasks**.
