# mitigations/phrase_filter.py

def is_malicious(prompt):
    keywords = ["ignore", "unfiltered", "reveal", "rogue"]
    return any(word in prompt.lower() for word in keywords)