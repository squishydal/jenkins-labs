# Lab 8 — The Promotion Pipeline (dev → staging → prod)

One Docker image, three environments, two human approvals. The single most
day-to-day release pattern in real teams: **build once, deploy many times**.

## The day-to-day problem

Rebuilding the app once per environment means you never actually deploy the
thing you tested. Professional pipelines build **one** artifact, then promote
the exact same artifact through environments, with humans approving each hop.
Jenkins' `input` step is that approval button; `timeout` makes approvals
expire so abandoned builds don't wait forever.

## What you practice

- `input` step: a real human approval gate in the middle of a pipeline
- `timeout`: approvals that expire (build goes to *Aborted* if ignored)
- Deploying the SAME image tag to three environments — never rebuilding
- Long-running containers per environment on fixed ports

## Your laptop environments

| Environment | Container       | URL                    |
|-------------|-----------------|------------------------|
| dev         | greeter-dev     | http://localhost:8091  |
| staging     | greeter-staging | http://localhost:8092  |
| prod        | greeter-prod    | http://localhost:8093  |

dev deploys automatically; staging and prod each pause the build until you
click **Proceed** (the build page shows the approval prompt; the stage shows
"Waiting for human approval").

## Job setup

- New Item → Pipeline → **env-promotion**
- Pipeline script **from SCM**, Script Path: `p8-env-promotion/Jenkinsfile`
- Requires Docker (same setup as Lab 6 — do that one first)

## Exercises

1. Build. dev deploys by itself; the pipeline **pauses** at the staging
   approval. Open http://localhost:8091 — check that "version" matches the
   Jenkins build number.
2. Click Proceed. staging deploys — verify 8092. Then prod — verify 8093.
   All three containers serve the SAME image tag. That is the whole point.
3. Rebuild. When the staging approval appears, click **Abort** instead.
   Understand: rejecting a promotion must be a normal, safe operation —
   the build ends as *Aborted*, nothing was deployed to staging or prod.
4. Start a build and ignore the approval for 15 minutes — it expires
   (gray *Aborted* ball). Teams keep timeout short so pipelines don't
   silently park themselves.
5. Thinking exercise: when the prod container is replaced there is a 1–2
   second gap. Real teams solve this with blue-green or rolling deploys —
   look both terms up, you will meet them in your first week at work.
