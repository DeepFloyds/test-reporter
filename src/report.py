from statistics import mean


def build_summary(testcases):
    return {
        "passed": sum(1 for t in testcases if t.result == "PASS"),
        "failed": sum(1 for t in testcases if t.result == "FAIL"),
        "avg_duration": mean(t.duration for t in testcases)
    }


def group_by_category(testcases):
    grouped = {}

    for t in testcases:
        if t.category not in grouped:
            grouped[t.category] = []

        grouped[t.category].append(t)

    return grouped