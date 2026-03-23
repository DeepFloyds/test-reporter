# Test Reporter

Python tool for generating test reports similar to Polarion.

## Features
- Load test results from JSON
- Convert to structured test cases
- Generate summary (PASS / FAIL / average duration)
- Export reports:
  - CSV (Excel compatible)
  - HTML (styled report)

## Project Structure
src/
- model.py
- parser.py
- report.py
- main.py

example_data/
- tests.json

## Usage

python src/main.py

## Output

- CSV report
- HTML report

## Setup

python -m venv venv
venv\Scripts\activate
Note: Uses only Python standard library.

## Background

Inspired by real work in firmware testing and Polarion-based validation workflows.