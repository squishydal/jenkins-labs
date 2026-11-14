#!/usr/bin/env bash
# One-command setup for the Jenkins learning lab (Ubuntu / Debian).
#
# What it does:
#   1. Writes .env with your laptop's docker group ID (needed for Lab 6)
#   2. Builds the custom Jenkins image (first run: roughly 3-5 minutes)
#   3. Starts the container in the background
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -f .env ]; then
  if [ ! -S /var/run/docker.sock ]; then
    echo "ERROR: Docker does not seem to be running (/var/run/docker.sock is missing)."
    echo "Install Docker first (Handbook, Chapter 3), then re-run this script."
    exit 1
  fi
  DOCKER_GID=$(stat -c '%g' /var/run/docker.sock)
  echo "DOCKER_GID=${DOCKER_GID}" > .env
  echo "[setup] wrote .env with DOCKER_GID=${DOCKER_GID}"
fi

echo "[setup] building and starting Jenkins (first build takes a few minutes)..."
docker compose up -d --build

echo
echo "[setup] done. Jenkins is booting, it needs ~1 minute before the web page is up."
echo
echo "  Open the UI :  http://localhost:8080"
echo "  Unlock code :  docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword"
echo "  Follow logs :  docker compose logs -f jenkins"
echo "  Stop / start:  docker compose down | docker compose up -d"
echo "  FULL reset  :  docker compose down -v   (deletes all jobs and history!)"
