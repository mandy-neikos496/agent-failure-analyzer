import json

# load file :D
with open("sample_logs.json", "r") as f:
    logs = json.load(f)

for run in logs:
    run_id = run.get("run_id")
    steps = run.get("steps", [])

    print(f"\nRun {run_id}:")

    # Check empty
    if not steps:
        print("No steps found in this run ૮(˶ㅠ︿ㅠ)ა")
        continue

    # Tool errors
    for step in steps:
        if step.get("status") == "error":
            print(f"Tool Error in {step.get('action')}: {step.get('error')}")
    
    # Loop detection
    actions = [step.get("action") for step in steps]

    for action in set(actions):
        if actions.count(action) >= 3:
            print(f" ∞ Possible Loop: '{action}' repeated {actions.count(action)} times")