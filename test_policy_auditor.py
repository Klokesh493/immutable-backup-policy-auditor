import unittest

from policy_auditor import audit


class PolicyAuditorTest(unittest.TestCase):
    def test_detects_missing_immutability(self):
        row = {"policy": "dev", "immutable": "no", "encrypted": "yes", "offsite_copy": "yes", "retention_days": "30"}
        self.assertEqual(audit(row), ["immutable"])


if __name__ == "__main__":
    unittest.main()
