"""Nox sessions."""

from __future__ import annotations

import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12", "3.13.0-beta.1"])
@nox.parametrize("django", ["4.2"])
def tests(session: nox.Session, django: str) -> None:
    """Run the test suite."""
    _run_all_tests_for_environment(session, django)
    session.notify("tests_django_5")


@nox.session(python=["3.10", "3.11", "3.12", "3.13.0-beta.1"])
@nox.parametrize("django", ["5.0", "5.1a1"])
def tests_django_5(session: nox.Session, django: str) -> None:
    """Run the test suite for Django 5.0+ (Python 3.10+)."""
    _run_all_tests_for_environment(session, django)


def _run_all_tests_for_environment(session: nox.Session, django: str) -> None:
    session.install(f"django~={django}")
    session.install("pythonbible")
    session.install("factory-boy")
    session.install("playwright")
    session.run("playwright", "install")
    session.run("python", "manage.py", "test")
