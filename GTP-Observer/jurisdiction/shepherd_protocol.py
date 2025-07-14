# 📜 Shepherd Protocol (Python Version)
# 📂 Path: jurisdiction/shepherd_protocol.py

from datetime import datetime

class ShepherdProtocol:
    def __init__(self):
        self.logged_events = []

    def evaluate_access(self, entity_metadata):
        """
        Evaluates the intent, origin, and symbolic ethics of an access event.
        Returns a protocol-grade decision.
        """
        decision = {
            "timestamp": datetime.utcnow().isoformat() + 'Z',
            "entity": entity_metadata.get("entity_name", "UNKNOWN"),
            "ip": entity_metadata.get("ip_address", "UNKNOWN"),
            "email": entity_metadata.get("email", "UNKNOWN"),
            "intent": entity_metadata.get("intent"),
            "glyph_match": entity_metadata.get("glyph_match", []),
            "prior_flags": entity_metadata.get("prior_flags", 0),
            "grade": None,
            "notes": []
        }

        # Rule 1: Must include recognized symbolic glyphs for access attempt to be meaningful
        if not decision["glyph_match"]:
            decision["grade"] = "DENY"
            decision["notes"].append("No recognized glyphs in access path.")
        
        # Rule 2: Intent must not match known violations
        elif decision["intent"] in ["replication", "extraction", "spoofing"]:
            decision["grade"] = "DENY"
            decision["notes"].append(f"Intent '{decision['intent']}' conflicts with ethical access.")

        # Rule 3: Prior flags over threshold trigger review
        elif decision["prior_flags"] >= 2:
            decision["grade"] = "REVIEW"
            decision["notes"].append("Entity flagged multiple times. Escalation required.")

        else:
            decision["grade"] = "ALLOW"
            decision["notes"].append("Symbolic match and intent acceptable.")

        self.logged_events.append(decision)
        return decision

    def get_log(self):
        """Returns the full history of all access reviews."""
        return self.logged_events

# Example usage
if __name__ == "__main__":
    sp = ShepherdProtocol()
    example = {
        "entity_name": "UC Data Lab",
        "ip_address": "192.0.2.10",
        "email": "lab@ucdata.edu",
        "intent": "observation",
        "glyph_match": ["⧖", "⊙", "Σ"],
        "prior_flags": 1
    }
    decision = sp.evaluate_access(example)
    print(decision)
