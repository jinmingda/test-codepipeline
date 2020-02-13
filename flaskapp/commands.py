"""Click commands."""
import os
from subprocess import call
from typing import Sequence, Union

import click

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, "tests")
APP_PATH = os.path.join(PROJECT_ROOT, "flaskapp")


def execute_tool(
    command_line: Union[Union[bytes, str], Sequence[Union[bytes, str]]]
) -> None:
    """Execute a checking tool with its arguments."""
    rv = call(command_line)
    if rv != 0:
        exit(rv)
    return None


@click.command()
def test() -> None:
    """Run the tests."""
    execute_tool(["pytest", TEST_PATH, "--verbose"])
    return None


@click.command()
def lint() -> None:
    """Lint and check code style with black, flake8 and mypy."""
    click.echo("* Start running tests...")

    click.echo("* Check code style with black")
    execute_tool(["black", "--check", "--diff", "--quiet", PROJECT_ROOT])

    click.echo("* Check code style with flake8")
    execute_tool(["flake8", PROJECT_ROOT])

    click.echo("* Check code typing with mypy")
    execute_tool(["mypy", "--strict", APP_PATH])
    return None
