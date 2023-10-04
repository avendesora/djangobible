"""Nox sessions."""

from __future__ import annotations

import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
@nox.parametrize("django", ["3.2", "4.1", "4.2"])
def tests(session: nox.Session, django: str) -> None:
    """Run the test suite."""
    session.install(f"django~={django}")
    session.install("pythonbible")
    session.install("factory-boy")
    session.install("playwright")
    session.run("python", "manage.py", "test")
    session.notify("tests_python_3_12")


@nox.session(python=["3.12"])
@nox.parametrize("django", ["3.2", "4.1", "4.2"])
def tests_python_3_12(session: nox.Session, django: str) -> None:
    """Run the test suite for Python 3.12."""
    # Playwright doesn't support Python 3.12 yet, so only run unit tests.
    session.install(f"django~={django}")
    session.install("pythonbible")
    session.install("factory-boy")
    session.run("python", "manage.py", "test", "test_django_app/tests/unit_tests")
