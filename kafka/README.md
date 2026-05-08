# Local Kafka (Docker)

Run Kafka + Zookeeper locally for Phase 6 notebooks.

## Start

From this directory (`kafka/`):

```bash
docker compose up
```

Kafka broker endpoint:

- `localhost:9092`

## Install Python client

Use your environment (venv recommended):

```bash
pip install kafka-python
```

## Stop

`Ctrl+C` in the terminal, or:

```bash
docker compose down
```
