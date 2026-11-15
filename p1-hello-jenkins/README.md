# Lab 1 — Hello Jenkins (the starter template)

The gentle first project: no code, no Git — just you, the Jenkins UI, and your
first build. Full click-by-click instructions: **Handbook, Chapter 6**.

## What you practice

- Creating a **Freestyle job** from scratch
- Adding an **Execute shell** build step
- Running **Build Now** and reading the **Console Output**
- Finding the **Workspace** and understanding the **build number**

## The build step to paste

```bash
echo "Hello from Jenkins!"
echo "Build #$BUILD_NUMBER, running on node: $NODE_NAME"
date
python3 --version
echo "---- workspace contents ----"
ls -la
```

## Exercises after it goes green

1. Add `exit 1` as the last line, build again, and see your first **red** build.
2. Remove the line, rebuild, and watch the job go back to blue/green.
3. Use **Disable/Enable** on the job and observe the gray icon.
4. Build 3 times, then explore **Build History** on the left.
