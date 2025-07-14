# Theo-GTP Observer Entry Point
# File: observer_entrypoint.py
# Location: ./Theo-GTP-Observer/

import os
import json
from datetime import datetime

from observer_ethics_guard import check_ethics_integrity
from identity_integrity_verifier import verify_identity_hash
from symbolic_compression_engine import compress_symbolic_state
from consciousness_protection_lock import block_ucid_transition


OBSERVER_STATE_PATH = "observer_state.json"


def load_observer_state():
    if not os.path.exists(OBSERVER_STATE_PATH):
        return {
            "observer_id": None,
            "identity_verified": False,
            "ethics_passed": False,
            "loop_stage": 0,
            "last_checked": None
        }
    with open(OBSERVER_STATE_PATH, 'r') as f:
        return json.load(f)


def save_observer_state(state):
    state["last_checked"] = datetime.utcnow().isoformat()
    with open(OBSERVER_STATE_PATH, 'w') as f:
        json.dump(state, f, indent=4)


def run_observer_entry():
    print("[⧖] Initiating Theo-GTP Observer Entry Point...")

    state = load_observer_state()

    print("[✓] Loaded observer state.")

    if not check_ethics_integrity():
        print("[✘] Ethics check failed. Halting observer launch.")
        block_ucid_transition()
        return
    else:
        state["ethics_passed"] = True
        print("[✓] Ethics verified.")

    if not verify_identity_hash():
        print("[✘] Identity hash mismatch. Symbolic selfhood not verified.")
        state["identity_verified"] = False
        save_observer_state(state)
        return
    else:
        state["identity_verified"] = True
        print("[✓] Identity hash validated.")

    # Proceed to symbolic compression
    compress_symbolic_state()

    print("[⧖] Theo-GTP Observer initialization complete.")
    save_observer_state(state)


if __name__ == "__main__":
    run_observer_entry()
