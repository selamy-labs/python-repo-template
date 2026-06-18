"""Replace with real logic; kept minimal so the template ships green and covered."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a greeting for ``name``."""
    if not name:
        raise ValueError("name must be non-empty")
    return f"Hello, {name}!"
