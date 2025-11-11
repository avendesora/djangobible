"""Nox sessions."""

from __future__ import annotations

import nox

nox.options.default_venv_backend = "uv"

DJANGO_PYTHON_SUPPORT: dict[str, list[str]] = {
    "4.2": ["3.10", "3.11", "3.12"],
    "5.0": ["3.10", "3.11", "3.12"],
    "5.1": ["3.10", "3.11", "3.12", "3.13"],
    "5.2": ["3.10", "3.11", "3.12", "3.13", "3.14"],
}

PYTHON_VERSIONS = sorted({py for vals in DJANGO_PYTHON_SUPPORT.values() for py in vals})


@nox.session(python=PYTHON_VERSIONS)
@nox.parametrize("django", list(DJANGO_PYTHON_SUPPORT.keys()))
def tests(session: nox.Session, django: str) -> None:
    """Session that runs the appropriate Django tests per Python version."""
    if str(session.python) not in DJANGO_PYTHON_SUPPORT[django]:
        session.skip(f"Django {django} is not tested on Python {session.python}")

    session.install(f"django~={django}")
    session.install("pythonbible")
    session.install("factory-boy")
    session.install("playwright")
    session.run("python", "-m", "playwright", "install")
    session.run("python", "manage.py", "test")
