# CLI Log Analyzer

A small Python CLI that reads line-based logs, counts levels, surfaces errors, and writes a short report—similar to first-pass production debugging.

## Features

- Count log lines by level (`INFO`, `WARNING`, `ERROR`, …)
- List every `ERROR` message (default mode)
- **Error rate** — errors as a percentage of all lines
- **Report file** — writes `report.txt` next to `analyzer.py`
- **Optional filter** — show only messages for one level

## Setup

From this directory:

```bash
pip install -r ../../../requirements.txt
```

(Only the standard library is required for this project.)

## Run

```bash
cd projects/batch_pipeline/log_analyzer
python analyzer.py logs.txt
```

Optional — filter to one level (example: errors only at message level):

```bash
python analyzer.py logs.txt ERROR
python analyzer.py logs.txt INFO
```

## Output

- Printed summary, error rate, error messages (or filtered messages)
- `report.txt` with counts and error rate

## Project layout

```text
log_analyzer/
├── logs.txt       # sample input
├── analyzer.py    # CLI entrypoint
├── utils.py       # parse + aggregate
├── README.md
└── report.txt     # generated when you run the tool
```
