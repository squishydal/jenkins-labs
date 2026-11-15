#!/usr/bin/env python3
"""Sales report generator — Lab 2 (Jenkins Nightly Report).

Reads sales_data.csv (same folder) and writes a summary report into
./reports/ relative to the Jenkins workspace.

Deliberate failure behaviour (so you can practise reading red builds):
  exit 2 - bad parameters (limit is not a number / out of range, unknown region)
  exit 3 - no data rows for the requested region
  exit 0 - report generated successfully
"""
import argparse
import csv
import datetime
import os
import sys

VALID_REGIONS = {"north", "south", "east", "west"}
MAX_LIMIT = 20


def load_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Generate a regional sales report")
    ap.add_argument("--region", required=True,
                    help="north | south | east | west | all")
    ap.add_argument("--limit", required=True,
                    help="how many top transactions to list (1-%d)" % MAX_LIMIT)
    ap.add_argument("--data", default=os.path.join(here, "sales_data.csv"))
    args = ap.parse_args()

    region = args.region.strip().lower()

    # ---- validation: LIMIT must be a whole number in range (deliberate case) ----
    try:
        limit = int(args.limit)
    except ValueError:
        print("BUILD FAILED: TOP_LIMIT must be a whole number, got '%s'."
              % args.limit, file=sys.stderr)
        sys.exit(2)
    if not 1 <= limit <= MAX_LIMIT:
        print("BUILD FAILED: TOP_LIMIT must be between 1 and %d, got %d."
              % (MAX_LIMIT, limit), file=sys.stderr)
        sys.exit(2)

    if region != "all" and region not in VALID_REGIONS:
        print("BUILD FAILED: unknown region '%s'. Valid choices: all, %s."
              % (args.region, ", ".join(sorted(VALID_REGIONS))), file=sys.stderr)
        sys.exit(2)

    rows = load_rows(args.data)
    if region != "all":
        rows = [r for r in rows if r["region"] == region]

    if not rows:
        print("BUILD FAILED: no sales data for region '%s'." % region,
              file=sys.stderr)
        sys.exit(3)

    for r in rows:
        r["amount"] = float(r["amount"])

    total = sum(r["amount"] for r in rows)
    average = total / len(rows)
    top = sorted(rows, key=lambda r: r["amount"], reverse=True)[:limit]

    os.makedirs("reports", exist_ok=True)
    out_path = os.path.join("reports", "sales_report_%s.txt" % region)
    with open(out_path, "w") as f:
        w = f.write
        w("SALES REPORT - %s\n" % region.upper())
        w("Generated    : %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        w("Transactions : %d\n" % len(rows))
        w("Total revenue: $%s\n" % format(total, ",.2f"))
        w("Average order: $%s\n" % format(average, ",.2f"))
        w("\nTOP TRANSACTIONS\n")
        w("-" * 42 + "\n")
        for i, r in enumerate(top, 1):
            w("%2d. %s  %-18s $%10s\n"
              % (i, r["date"], r["product"], format(r["amount"], ",.2f")))

    print("OK: wrote %s" % out_path)
    print("  transactions: %d   total: $%s" % (len(rows), format(total, ",.2f")))


if __name__ == "__main__":
    main()
