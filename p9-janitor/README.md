# Lab 9 — The Janitor (Jenkins disk management)

The most common Jenkins admin ticket in the world: **"No space left on
device"** — usually at 4am. Every job copies its repo into a workspace on
every build, archived artifacts pile up, Docker keeps old image layers.
Disk fills. This lab builds the scheduled job that fights back.

## What actually fills the disk (day-to-day)

1. **Workspaces** — one folder per job, often never cleaned between builds
2. **Archived artifacts** — every build keeps its jars/zips/reports forever
   unless someone enables *Discard old builds*
3. **Docker** — dangling images and layers from repeated builds

## What you practice

- A scheduled housekeeping pipeline (`triggers { cron(...) }` inside the
  Jenkinsfile — the pipeline way of doing what you did in the Lab 2 UI)
- Reading `df -h`, `du -sh`, `docker system df` like an operator
- **Safe** cleanup: `docker container prune` removes *stopped* containers
  only, `docker image prune` removes *dangling* images only — and why those
  qualifiers matter (running apps and tagged images survive)
- `deleteDir()` in post — this job cleans up after itself
- The human fix you must also learn: **Discard old builds** per job

## Job setup

- New Item → Pipeline → **janitor**
- Pipeline script **from SCM**, Script Path: `p9-janitor/Jenkinsfile`
- The nightly trigger (`H 4 * * *`) registers itself after the first run;
  you can also run it manually any time with Build Now

## Exercises

1. Run it manually. Open the archived `disk_report.txt`: which workspace is
   the biggest? Which is your own?
2. Build Lab 4 (Maven) two or three times, then run the janitor again —
   watch docker's dangling-image count and image size shrink.
3. The real fix, part 1: open the `maven-build` job → Configure → check
   **Discard old builds** → "Keep builds no more than" 5. Save, rebuild
   twice, watch old builds disappear from history. Janitor = symptoms;
   retention = cause. A real admin does both.
4. Advanced: add a stage that marks the build UNSTABLE when `df` reports
   less than 2 GB free on `/var/jenkins_home` — paging yourself before the
   disk pages you. (Hint: Lab 7's `catchError` pattern.)
