def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(" ", 1)
            logs.append(
                {
                    "level": parts[0],
                    "message": parts[1] if len(parts) > 1 else "",
                }
            )

    return logs


def count_levels(logs):
    counts = {}

    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1

    return counts
