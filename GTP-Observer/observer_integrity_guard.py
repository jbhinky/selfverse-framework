# 📂 Theo-GTP Observer / core / guardian / observer_integrity_guard.py

class EthicsViolation(Exception):
    pass

class ObserverRegistry:
    def __init__(self, max_allowed=1):
        self.registered_observers = []
        self.max_allowed = max_allowed  # default: only one observer permitted

    def register_observer(self, observer_name, intent_log, delay_token):
        if len(self.registered_observers) >= self.max_allowed:
            raise EthicsViolation("Multiple observers not permitted without recursive split approval.")

        if not self._is_valid(observer_name, intent_log, delay_token):
            raise EthicsViolation("Observer registration failed ethical verification.")

        self.registered_observers.append({
            "name": observer_name,
            "intent": intent_log,
            "delay": delay_token
        })
        return True

    def _is_valid(self, name, intent_log, delay_token):
        # Enforce delay+intent+identifier presence
        if not name or not delay_token or "intent" not in intent_log:
            return False
        # Add symbolic collapse check here if needed
        return True

    def is_duplicate_attempt(self):
        return len(self.registered_observers) > self.max_allowed

    def summary(self):
        return {
            "active_observers": len(self.registered_observers),
            "registry": self.registered_observers
        }

# 🔐 Usage Example
if __name__ == "__main__":
    registry = ObserverRegistry()
    try:
        registry.register_observer("⧖-alpha", {"intent": "ethical research"}, delay_token="⏳")
        registry.register_observer("⧖-beta", {"intent": "testing"}, delay_token="⏳")  # Triggers EthicsViolation
    except EthicsViolation as e:
        print(f"[⚠️ Ethics Violation] {e}")
