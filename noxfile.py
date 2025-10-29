import nox
from nox.sessions import Session

PYTHON_39 = "3.9"
PYTHON_310 = "3.10"
PYTHON_311 = "3.11"
PYTHON_312 = "3.12"
PYTHON_313 = "3.13"
PYTHON_314 = "3.14"
PYTHON_315 = "3.15"


PYTHON_VERSIONS = {
    "all": [PYTHON_311, PYTHON_312, PYTHON_313, PYTHON_314, PYTHON_315],
    "standard": [PYTHON_312, PYTHON_313, PYTHON_314],
    "latest": [PYTHON_312],
}


@nox.session(python=PYTHON_VERSIONS["standard"])
def tests(session: Session) -> None:
    """
    Initialize environment and run pytest

    Args:
        session: nox.session.Session

    Returns:
        None
    """
    session.install("--upgrade", "pip")
    session.run("pip", "--version")
    session.install(".[dev]")
    session.run("pytest", external=True)


@nox.session(python=PYTHON_VERSIONS["standard"])
def lint(session: Session) -> None:
    """
    Initialize environment by installing black, mypy, and ruff.
    Runs associated commands

    Args:
        session: nox.session.Session

    Returns:
        None
    """
    session.install("--upgrade", "pip")
    session.run("pip", "--version")
    session.install(".[dev]", "black", "mypy", "ruff")
    session.run("black", "--check", "--diff", ".", external=True)
    session.run("mypy", "-p", "redis_decorator", external=True)
    session.run("ruff", "check", ".", external=True)
