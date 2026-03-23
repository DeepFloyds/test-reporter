import csv
import html
from pathlib import Path
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
    
    
    
def export_to_csv(testcases, path: Path):
    fieldnames = ["Index", "Name", "Category", "Result", "Duration", "Note"]

    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for t in testcases:
            writer.writerow({
                "Index": t.index,
                "Name": t.name,
                "Category": t.category,
                "Result": t.result,
                "Duration": t.duration,
                "Note": t.note
            })    
  
  
 
 
def export_to_html(testcases, summary, path: Path):
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Test Report</title>
    <style>
        table {{border-collapse: collapse; width: 80%; margin: 20px;}}
        th, td {{border: 1px solid black; padding: 8px; text-align: center;}}
        th {{background-color: #f2f2f2;}}
        .PASS {{background-color: #d4edda;}}
        .FAIL {{background-color: #f8d7da;}}
    </style>
</head>
<body>

<h2>Test Summary</h2>
<p>Passed: {passed}</p>
<p>Failed: {failed}</p>
<p>Average Duration: {avg:.2f}</p>

<h2>Test Cases</h2>
<table>
<tr>
<th>#</th><th>Name</th><th>Category</th><th>Result</th><th>Duration</th><th>Note</th>
</tr>
""".format(
        passed=summary["passed"],
        failed=summary["failed"],
        avg=summary["avg_duration"]
    )

    for t in testcases:
        html_content += f"""
<tr>
<td>{t.index}</td>
<td>{html.escape(t.name)}</td>
<td>{html.escape(t.category)}</td>
<td class="{t.result}">{t.result}</td>
<td>{t.duration}</td>
<td>{html.escape(str(t.note))}</td>
</tr>
"""

    html_content += """
</table>
</body>
</html>
"""

    with path.open("w", encoding="utf-8") as f:
        f.write(html_content) 
 