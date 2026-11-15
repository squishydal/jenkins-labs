"""Tests for metrics.py - all of these should pass."""
from metrics import mean, median


def test_mean_basic():
    assert mean([1, 2, 3]) == 2.0


def test_mean_single():
    assert mean([7]) == 7.0


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even_returns_average_and_this_long_descriptive_name_pushes_the_line_over_hundred_chars():
    assert median([4, 1, 3, 2]) == 2.5
