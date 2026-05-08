#!/usr/bin/env python3
"""Smoke-test PostgreSQL credentials used in notebooks/02_sql/."""

import sys

try:
    import psycopg2
except ImportError as e:
    print("Install deps: pip install -r requirements.txt", file=sys.stderr)
    raise SystemExit(1) from e


def main() -> None:
    conn = psycopg2.connect(
        host="localhost",
        database="de_course",
        user="admin",
        password="admin",
    )
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()
        print("Connected successfully (SELECT 1 OK).")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
