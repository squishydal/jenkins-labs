"""Tiny string helpers for the pull-request gate lab."""


def slugify(text):
    """'Hello Jenkins World' -> 'hello-jenkins-world'."""
    words = text.strip().lower().split()
    return "-".join(words) if words else ""


def initials(name):
    """'Ada Byron' -> 'A.B.'"""
    parts = name.split()
    if not parts:
        return ""
    return ".".join(p[0].upper() for p in parts) + "."
