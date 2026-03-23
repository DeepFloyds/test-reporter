from pathlib import Path
from parser import load_tests, build_testcases
from report import build_summary, group_by_category, export_to_csv, export_to_html


def main():
    data = load_tests(Path("example_data/tests.json"))
    testcases = build_testcases(data)

    print("\nAll Tests:")
    for t in testcases:
        print(f"{t.index}. {t.name} - {t.result}")

    summary = build_summary(testcases)

    print("\nSummary:")
    print(summary)

    grouped = group_by_category(testcases)

    print("\nGrouped by category:")
    for category, tests in grouped.items():
        print(f"\n{category}:")
        for t in tests:
            print(f" - {t.name}")
            
            
    summary = build_summary(testcases)

    export_to_csv(testcases, Path("example_data/report.csv"))
    print("CSV report generated.")

    export_to_html(testcases, summary, Path("example_data/report.html"))
    print("HTML report generated.")        


if __name__ == "__main__":
    main()
    
    