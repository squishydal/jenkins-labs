# Lab 6 — Docker CI/CD Capstone (Notes API)

A real Flask API taken from commit to a running service on your laptop:
tested with pytest, packaged as a Docker image, smoke-tested, deployed.
Full walkthrough: **Handbook, Chapter 11**.

## What you practice

- The full CI/CD shape: Test -> Build image -> Smoke test -> Deploy
- Tagging images with the build number (`notes-api:$BUILD_NUMBER`) for instant rollback
- Smoke tests: throwaway container + `/health` polling + guaranteed cleanup
- Deploying: replace the running container, verify health, open http://localhost:8090

## Job setup

- Pipeline from SCM, Script Path: `p6-docker-deploy/Jenkinsfile`

## After a green build

```bash
curl -s -X POST http://localhost:8090/api/notes \
  -H 'Content-Type: application/json' \
  -d '{"text": "deployed by Jenkins"}'
curl -s http://localhost:8090/api/notes
docker ps          # see notes-api running next to jenkins-lab
docker images      # see notes-api:<build number>
```

## Exercises

1. Change the health message in app.py, push, rebuild — watch the live replacement.
2. Rollback drill: run an older image tag on port 8090 on purpose.
3. Delete a test, push, confirm the pipeline refuses to deploy broken code.
