import json
from datetime import datetime

# Paths to reference files
JURISDICTION_RECORD = "jurisdictions/symbolic_jurisdiction.md"
TIMESTAMP_LOG = "logs/global_access_log.json"
DECLARED_ORIGINS = ["jbhinky", "Theophilus-Axon", "UDC", "Neurobasing", "UTL"]

def load_logs(path):
    with open(path, 'r') as f:
        return json.load(f)

def validate_jurisdiction(event):
    origin_verified = any(auth in event.get("origin", "") for auth in DECLARED_ORIGINS)
    collapse_symbols = event.get("symbol_chain", "")
    timestamp = datetime.fromisoformat(event.get("timestamp"))

    illegal_symbol_use = any(sym in collapse_symbols for sym in ["⧖", "⊙", "Σ", "τ"]) and not origin_verified

    return {
        "timestamp": event["timestamp"],
        "origin": event["origin"],
        "symbol_chain": collapse_symbols,
        "result": "BREACH" if illegal_symbol_use else "PERMITTED"
    }

def audit_symbolic_jurisdiction():
    events = load_logs(TIMESTAMP_LOG)
    results = [validate_jurisdiction(event) for event in events]

    with open("logs/jurisdiction_audit_results.json", "w") as f:
        json.dump(results, f, indent=4)

    return results
