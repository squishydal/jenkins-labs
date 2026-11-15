# Lab 7 — The Quality Gate (lint + the yellow ball)

A tiny metrics library whose code *works* but is *sloppy* — exactly how real
pull requests arrive every day. Your pipeline must accept working code but
still complain about style. This lab teaches the middle ground between
"broken" and "perfect".

## The day-to-day problem

Teams fail builds for two very different reasons:

- the code is **broken** (tests fail) → red ball, must be fixed before merge
- the code is **sloppy** (lint warnings) → should not block anyone, but must
  not be silent either

That middle state is Jenkins' **UNSTABLE** result — the yellow ball: the build
finished, tests passed, but something needs attention. Recognizing and acting
on yellow is a daily CI skill in every team.

## What you practice

- Installing a tool *inside* a pipeline (`pip install` as a build step)
- `catchError(buildResult: 'UNSTABLE')` — a stage can "fail" without failing
  the whole build
- Reading flake8 output (`F401`, `W291`, `E501` and friends)
- UNSTABLE vs FAILURE vs SUCCESS — on the ball, in the history, in the log
- The quality-gate idea: warnings are visible, tests are authoritative

## Job setup

- New Item → Pipeline → **quality-gate**
- Pipeline script **from SCM**: your `jenkins-labs` repo
- Script Path: `p7-quality-gate/Jenkinsfile`

## The seeded lint issues (look at them first, fix them later)

1. `metrics.py` — unused `import os` (`F401`)
2. `metrics.py` — trailing whitespace on the `for` line (`W291`)
3. `test_metrics.py` — one line over the 100-char limit (`E501`)

## Exercises

1. Build. Expect a **yellow ball**: 3 flake8 issues in the log, tests all
   passing. Make sure you can explain why it is not red.
2. Fix the three issues via GitHub's web editor, push, rebuild → green.
3. Now break a *test expectation* on purpose, push → **red**. Compare the
   yellow build and the red build in build history, then fix it back.
4. Advanced: make the gate threshold-based (teams often allow N warnings
   before going yellow). Hint: `flake8 --exit-zero --count`, capture the
   count, and only mark UNSTABLE above your threshold.
