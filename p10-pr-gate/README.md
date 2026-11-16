# Lab 10 — The Pull Request Gate (multibranch pipeline)

The workflow every team runs every single day: nobody pushes straight to
master. Work happens on **feature branches** and merges through **pull
requests** that CI must validate first. Jenkins' answer is the
**Multibranch Pipeline** — one job definition that automatically discovers
every branch (and PR) in your repo and gives each one its own build.

## The day-to-day problem

With a single job pinned to master, you find out a branch is broken *after*
merging it. Teams need per-branch builds *before* merge: red branch = don't
merge. This is also the lab where you install a plugin — installing plugins
is itself a daily Jenkins admin task.

## What you practice

- Installing a plugin via Manage Jenkins → Plugins (if missing)
- Creating a **Multibranch Pipeline** job with a GitHub branch source
- **Branch indexing**: how Jenkins discovers branches and pull requests
- Feature-branch workflow using GitHub's web editor (no local git needed)
- Per-branch build history, and why a red branch is a *good* outcome

## Part A — create the job

1. Check plugins: Manage Jenkins → Plugins → Installed. You need
   **Pipeline: Multibranch** and **GitHub Branch Source** (the standard
   installation usually has both; if the "Multibranch Pipeline" item type
   is missing, install them from Available plugins).
2. New Item → **Multibranch Pipeline** → name `pr-gate`.
3. Branch Sources → Add source → **GitHub** → Repository HTTPS URL
   `https://github.com/squishydal/jenkins-labs`, credentials: your
   `github-pat` (or "none" if the repo is public).
4. Build Configuration → Script Path: `p10-pr-gate/Jenkinsfile`
   (your repo keeps every lab's pipeline in its own folder, remember).
5. Save — the first **branch index scan** runs and builds master.

## Part B — the daily workflow (all via GitHub's web editor)

1. On GitHub: open `squishydal/jenkins-labs` → branch selector (reads
   `main` / `master`) → type `feature/loud-initials` → **Create branch**.
2. Switch to that branch, open `p10-pr-gate/checker.py`, make a small
   change (e.g. uppercase the greeting), **Commit changes**.
3. Jenkins → `pr-gate` → **Scan Multibranch Pipeline Now** (a laptop setup
   has no webhooks, so you ask Jenkins to re-scan; real servers use
   webhooks and do this automatically). A new job for your branch appears
   and builds.
4. GitHub → Pull requests → New PR: `feature/loud-initials` → master.
5. Merge the PR → Scan Multibranch Pipeline Now again → master rebuilds
   with your merged code.
6. The gate exercise: make a change on a new branch that BREAKS a test
   (change one expected value), commit, scan → watch the branch job go
   red. Do NOT merge. That red branch is the gate doing its job. Fix it,
   scan, watch it go green, then merge.

## One job, many branches

You never create a job per branch again — Jenkins creates and deletes
branch jobs by itself. Delete a branch on GitHub, re-scan, the job
disappears. This is the difference between managing Jenkins by hand
(Labs 1-4) and letting Jenkins manage the workflow for you (this lab).


THIS IS THE CHANGE
