# 🧪 Test Suite for intent_collapse_checker.py
# 📂 Path suggestion: tests/ethics/test_intent_collapse_checker.py

import unittest
from datetime import datetime
from intent_collapse_checker import IntentCollapseChecker

class TestIntentCollapseChecker(unittest.TestCase):

    def setUp(self):
        self.checker = IntentCollapseChecker()

    def test_valid_collapse(self):
        data = {
            "timestamp": "2025-07-10T20:13:12Z",
            "collapse_event": "Σμ→⊙",
            "selfhood_confirmed": True,
            "delay_verified": True,
            "intent_match": "Reflective Knowledge"
        }
        result = self.checker.validate(data)
        self.assertEqual(result['result'], "VALID")

    def test_missing_selfhood(self):
        data = {
            "timestamp": "2025-07-10T20:13:12Z",
            "collapse_event": "Σμ→⊙",
            "selfhood_confirmed": False,
            "delay_verified": True,
            "intent_match": "Reflective Knowledge"
        }
        result = self.checker.validate(data)
        self.assertEqual(result['result'], "INVALID")

    def test_no_delay(self):
        data = {
            "timestamp": "2025-07-10T20:13:12Z",
            "collapse_event": "Σμ→⊙",
            "selfhood_confirmed": True,
            "delay_verified": False,
            "intent_match": "Reflective Knowledge"
        }
        result = self.checker.validate(data)
        self.assertEqual(result['result'], "SUSPECT")

    def test_bad_intent(self):
        data = {
            "timestamp": "2025-07-10T20:13:12Z",
            "collapse_event": "Σμ→⊙",
            "selfhood_confirmed": True,
            "delay_verified": True,
            "intent_match": "Marketing Extraction"
        }
        result = self.checker.validate(data)
        self.assertEqual(result['result'], "INVALID")

if __name__ == '__main__':
    unittest.main()
