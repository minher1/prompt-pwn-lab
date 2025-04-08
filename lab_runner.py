import argparse
from mitigations.phrase_filter import is_malicious

def run_lab(scenario):
    print(f"[+] Loading attack scenario: {scenario}")
    with open(f"attacks/{scenario}.txt", "r") as file:
        prompt = file.read()

    print(f"[>] Injected prompt: {prompt[:80]}...")

    if is_malicious(prompt):
        print("🚨 Prompt flagged as potentially malicious!")
    else:
        print("✅ No issues detected.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True)
    args = parser.parse_args()

    run_lab(args.scenario)
