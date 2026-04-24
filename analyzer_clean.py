import json

def detect_errors(run):
    errors = []

    for step in run.get("steps", []):
        if step.get("status") == "error":
            errors.append(
                f"Tool Error in {step.get('action')}: {step.get('error')}"
            )
    return errors

def detect_loops(run):
    steps = run.get("steps", [])
    actions = [step.get("action") for step in steps]

    loops = []

    for action in set(actions):
        if actions.count(action) >= 3:
            loops.append(
                f" Possible Loop: '{action}' repeated {actions.count(action)} times"
            )
    return loops

def analyze_run(run):
    run_id = run.get("run_id")
    print(f"\nRun {run_id}:")

    steps = run.get("steps", [])

    # Check empty
    if not steps:
        print("No steps found in this run")
        return
    
    # Tool errors
    errors = detect_errors(run)
    loops = detect_loops(run)

    # print results
    for e in errors:
        print("❌", e)

    for l in loops:
        print("⚠️", l)

# Main Program

with open("sample_logs.json", "r") as f:
    logs = json.load(f)

for run in logs:
    analyze_run(run)