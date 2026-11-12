PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) policy_auditor.py sample_policies.csv
