import csv
import sys


REQUIRED = ["immutable", "encrypted", "offsite_copy"]


def audit(row):
    gaps = [field for field in REQUIRED if row[field].lower() != "yes"]
    if int(row["retention_days"]) < 30:
        gaps.append("retention_days")
    return gaps


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            gaps = audit(row)
            print(f"{row['policy']}: {'pass' if not gaps else ','.join(gaps)}")


if __name__ == "__main__":
    main(sys.argv[1])
