# Lab 4 — Maven build & test reports (Java)

An invoice library compiled with Maven, tested with JUnit 5, packaged into a jar.
Full walkthrough: **Handbook, Chapter 9**.

## What you practice

- Pipeline stages for a **compiled language**: Build → Test → Package
- The `junit` step: Jenkins parses surefire XML and draws **test trend graphs**
- `archiveArtifacts` for the built jar, with fingerprinting
- Watching build history accumulate (retention settings)

## Job setup

- Pipeline script **from SCM**: your `jenkins-labs` repo, branch `*/main`
- Script Path: `p4-java-maven/Jenkinsfile`

## Exercises

1. Open a build → **Test Result**: you should see 5 passed tests and a trend graph.
2. Change `assertEquals(47.5, ...)` to `47.6`, commit, push: red build + trend dips.
3. Fix it back, commit, push: green. You just lived the daily CI loop.
4. Click **Keep this build forever** on a good build, then explain why teams do that.
