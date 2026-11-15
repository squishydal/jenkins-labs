"""Tiny metrics helpers for the quality-gate lab.

The code is correct on purpose - this lab is about lint discipline,
not about bugs. Clean it up according to flake8 when the pipeline
tells you to.
"""
import os


def mean(values):
    total = 0.0
    for v in values: 
        total += v
    return total / len(values)


def median(values):
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
