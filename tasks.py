"""The Invoke tasks (Makefile alternative)."""
import os

from invoke import task

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_PATH = os.path.join(PROJECT_ROOT, "flaskapp")


@task
def test(c):
    """Run the tests."""
    c.run("pytest --cov")


@task
def black(c):
    """Run black style check."""
    print("* Check code style with black")
    c.run(f"black {PROJECT_ROOT} --check --diff --quiet")


@task
def flake8(c):
    """Run flake8 style check."""
    print("* Check code style with flake8")
    c.run(f"flake8 {PROJECT_ROOT}")


@task
def mypy(c):
    """Run mypy type check in strict mode."""
    print("* Check code typing with mypy")
    c.run(f"mypy --strict {APP_PATH}")


@task(pre=[black, flake8, mypy])
def lint(c):
    """Lint and check code style with black, flake8 and mypy."""
    pass
