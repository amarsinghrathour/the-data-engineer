import sys
from pathlib import Path

from utils import count_levels, parse_logs


def write_report(stats: dict, error_pct: float, path: Path) -> None:
    lines = [
        "Log Analysis Report",
        "=" * 40,
        "",
        "Counts by level:",
    ]
    for level, count in stats.items():
        lines.append(f"  {level}: {count}")
    lines.append("")
    lines.append(f"Error rate: {error_pct:.2f}%")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile> [LEVEL]")
        print("  LEVEL optional: INFO, WARNING, ERROR — list only those messages")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2].upper() if len(sys.argv) >= 3 else None

    logs = parse_logs(file_path)
    stats = count_levels(logs)

    print("\n📊 Log Summary:")
    for level, count in stats.items():
        print(f"{level}: {count}")

    error_pct = (stats.get("ERROR", 0) / len(logs)) * 100 if logs else 0.0
    print(f"\nError Rate: {error_pct:.2f}%")

    report_path = Path(__file__).resolve().parent / "report.txt"
    write_report(stats, error_pct, report_path)
    print(f"\n📄 Report saved to {report_path.name}")

    if level_filter:
        filtered = [log for log in logs if log["level"] == level_filter]
        print(f"\n📋 Messages ({level_filter}):")
        for log in filtered:
            print(log["message"])
        if not filtered:
            print("(none)")
    else:
        errors = [log for log in logs if log["level"] == "ERROR"]
        print("\n❌ Errors:")
        for err in errors:
            print(err["message"])


if __name__ == "__main__":
    main()
