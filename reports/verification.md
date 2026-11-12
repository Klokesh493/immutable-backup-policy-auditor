# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 policy_auditor.py sample_policies.csv
prod-db: pass
dev-share: immutable,offsite_copy,retention_days
test_detects_missing_immutability (test_policy_auditor.PolicyAuditorTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
