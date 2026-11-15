# Lab 3 — The Broken Build (QuickCart CI)

Checkout-total code with a **planted rounding bug** and a Jest suite that catches it.
Your first Jenkins build here WILL fail — that is the assignment. Full debugging
walkthrough: **Handbook, Chapter 8**.

## What you practice

- Your first **Pipeline job** reading a `Jenkinsfile` from SCM (Script Path: `p3-webapp-ci/Jenkinsfile`)
- Declarative pipeline structure: `pipeline` → `agent` → `stages` → `steps` → `post`
- Reading a **red build**: Console Output → Jest's Expected/Received diff → locate → fix → push → green

## The bug (no peeking until you have read the console output!)

`src/cart.js` rounds money to ONE decimal; the spec at the top of the file says TWO.
The fix is one line. The tests tell you exactly which values are wrong.

## Exercises

1. Add a 5% discount test case (55.97 * 0.95 = 53.1715 -> 53.17).
2. Break one expectation on purpose, push, watch the red build name the test, revert.
3. Add a 'Smoke' stage that runs `node src/index.js` between Install and Test.
