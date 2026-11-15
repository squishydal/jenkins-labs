# jenkins-labs — ten hands-on projects for learning Jenkins

Each folder is a separate mini-project with a **different real-world case**, so you
practice a different Jenkins skill every time. The full walkthrough for every lab
(the exact clicks, what to watch for, and deliberate problems to debug) is in the
**Jenkins Hands-On Starter Kit** PDF that ships with this folder.

## Prerequisites

- Ubuntu or Debian laptop
- Docker Engine installed (`docker --version` works)
- Git + a GitHub account (labs 2-6 read the code from GitHub)

## Quick start

```bash
./setup.sh          # builds the image and starts Jenkins
# open http://localhost:8080
# unlock code: docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Then publish this folder to GitHub:

```bash
cd jenkins-labs
git init
git add .
git commit -m "Jenkins learning labs"
git branch -M main
git remote add origin https://github.com/<your-username>/jenkins-labs.git
git push -u origin main
```

## The lab map

### Core course (p1-p6): language builds

| Folder | Case you practice | Job type | Language | Jenkins skills |
|---|---|---|---|---|
| `p1-hello-jenkins` | The plain starter job (the "template" one) | Freestyle | shell/python | jobs, builds, console, workspace |
| `p2-nightly-report` | Scheduled regional sales report | Freestyle | Python | parameters, cron triggers, artifacts, failing on bad input |
| `p3-webapp-ci` | Checkout totals CI **with a planted bug** | Pipeline | Node.js | Jenkinsfile, stages, reading a red build, fix-and-rebuild |
| `p4-java-maven` | Invoice library build + test reports | Pipeline | Java/Maven | compiled builds, JUnit trend graphs, archiving jars |
| `p5-go-release` | Cross-platform CLI release | Pipeline | Go | parallel stages, matrix builds, versioned release zips |
| `p6-docker-deploy` | Flask API built, tested, deployed as a container | Pipeline | Python+Docker | image builds, smoke tests, deploy, cleanup |

### Day-to-day ops crash course (p7-p10): how real teams run Jenkins

Do these after p5-p6 — p8 and p9 need the Docker practice from p6.

| Folder | Daily problem it mirrors | Jenkins skills |
|---|---|---|
| `p7-quality-gate` | "Is it broken or just sloppy?" — lint noise vs real failures | `catchError`, UNSTABLE (yellow) vs FAILURE (red), pip inside builds |
| `p8-env-promotion` | Build once, promote dev → staging → prod with approvals | `input`, `timeout`, one artifact through environments |
| `p9-janitor` | "No space left on device" — the classic Jenkins admin ticket | cron in Jenkinsfile, safe docker pruning, `deleteDir`, Discard old builds |
| `p10-pr-gate` | Every PR must pass CI before merge (the daily team loop) | Multibranch Pipeline, branch indexing, plugin install, feature branches |

Do them in order — each lab assumes only what the previous ones taught.

## Everyday commands

```bash
docker compose up -d          # start Jenkins
docker compose down           # stop (jobs and history are kept)
docker compose logs -f jenkins
docker compose down -v        # FULL reset — deletes everything, back to square one
```

## Layout

```
jenkins-labs/
├── Dockerfile            custom Jenkins image (Jenkins LTS + Python/Node/Go/Maven/Docker CLI)
├── docker-compose.yml    how the container runs
├── setup.sh              one-command setup
└── p1 ... p10            the ten lab projects (p3+ contain a Jenkinsfile each)
```
