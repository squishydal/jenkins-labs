# Lab 5 — Go multi-platform release

A word-count CLI released for Linux, macOS (darwin) and Windows, with versioned
zip names. Full walkthrough: **Handbook, Chapter 10**.

## What you practice

- **Parameters** (`VERSION`) baked into artifact file names
- **Parallel stages**: `go vet` and `go test` run at the same time
- **Matrix builds**: one stage definition × 3 values of `GOOS`
- **Release artifacts**: `dist/wordutil-0.1.0-<os>-amd64.zip` per platform

## Job setup

- Pipeline from SCM, Script Path: `p5-go-release/Jenkinsfile`

## Exercises

1. Build with VERSION `0.2.0` — the zip names change, old build keeps its own.
2. Add `arm64` as a second axis (`GOARCH`) — 6 zips per build.
3. Break a test locally, commit, and watch the **parallel** Verify stage fail fast.
