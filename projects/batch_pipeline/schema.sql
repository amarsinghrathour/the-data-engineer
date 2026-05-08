-- Users table for projects/batch_pipeline/etl_pipeline.py
-- Run once against your Postgres (same DB as POSTGRES_* env vars).

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
