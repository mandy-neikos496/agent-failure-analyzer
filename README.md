# Agent Failure Analyzer

A simple Python tool that analyzes AI agent logs and detects common failure patterns.

## What it does
This tool reads structured AI agent logs and helps identify:
- Tool execution errors
    - e.g. API timeouts
- Repeated action loops
    - redundant execution
- Missing or empty runs

It helps debug behavior in agent systems like those used in frameworks such as LangChain.

## Features
- Detects tool execution errors
- Detects repeated action loops
- Handles empty runs safely
- Outputs readable diagnostic reports

## Project Structure
- analyzer_clean.py
- analyzer_bad.py
- sample_logs.json
- README.md

## How to Run
```bash
python analyzer_clean.py
```
## Example Output
```
Run 1:
❌ Tool Error in summarize: API timeout

Run 2:
⚠️  Possible Loop: 'search' repeated 3 times
```

## Purpose
This project simulates the debugging of AI agent failures by analyzing step-by-step execution logs and identifying patterns that  indicate errors or inefficient behavior.

