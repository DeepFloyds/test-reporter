import json
from pathlib import Path
from model import TestCase


def load_tests(path: Path):
    with path.open("r") as f:
        return json.load(f)


def build_testcases(data: list[dict]) -> list[TestCase]:
    testcases = []

    for i, t in enumerate(data, start=1):
        testcases.append(
            TestCase(
                index=i,
                name=t.get("test_name", "UNKNOWN"),
                category=t.get("category"),
                result="PASS" if t.get("result") else "FAIL",
                duration=t.get("time_sec"),
                note=t.get("error") if not t.get("result") else ""
            )
        )

    return testcases