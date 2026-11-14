# Lab 2 — The Nightly Report

A regional sales report generator that Jenkins runs on a schedule, with
parameters and archived artifacts. Full walkthrough: **Handbook, Chapter 7**.

## What you practice

- Freestyle job reading code **from Git** (your `jenkins-labs` repo)
- **Build parameters**: `REGION` (choice) and `TOP_LIMIT` (string)
- **Build periodically** trigger (`H 23 * * *`, or `H/5 * * * *` while practising)
- **Archiving artifacts** (`reports/*.txt`)
- Deliberate failure case: a bad `TOP_LIMIT` value → red build → read the log

## Build step to paste

```bash
python3 p2-nightly-report/report.py --region "$REGION" --limit "$TOP_LIMIT"
```

## Post-build action

Archive the artifacts, path pattern: `reports/*.txt`

## Try these builds

| Build | REGION | TOP_LIMIT | Expected |
|---|---|---|---|
| 1 | west | 5 | green, artifact appears |
| 2 | all | 10 | green, artifact appears |
| 3 | east | banana | RED — read the error in console |
| 4 | east | 999 | RED — range check |
