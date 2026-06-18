"""Tests for example_pkg.core — replace alongside the real logic."""

from __future__ import annotations

import pytest

from example_pkg.core import greet


def test_greet_returns_greeting() -> None:
    assert greet("world") == "Hello, world!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError):
        greet("")
