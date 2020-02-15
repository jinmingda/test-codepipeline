"""The app module, containing the app factory function."""
import os
from typing import Any, Dict, Optional

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from flaskapp import commands, public


def register_extensions(app: Flask) -> None:
    """Register Flask plugins."""
    # Initialize Sentry
    if app.config.get("SENTRY_DSN"):
        sentry_sdk.hub.init(
            dsn=app.config.get("SENTRY_DSN"), integrations=[FlaskIntegration()],
        )
    else:
        sentry_sdk.hub.init()
    return None


def register_blueprints(app: Flask) -> None:
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    return None


def register_shellcontext(app: Flask) -> None:
    """Register shell context objects."""

    def shell_context() -> Dict[str, Any]:
        """Shell context objects."""
        return {}

    app.shell_context_processor(shell_context)


def register_commands(app: Flask) -> None:
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    return None


def create_app(config: Optional[str] = None) -> Flask:
    """Create a Flask application using the app factory pattern.

    Parameters
    ----------
    config : Optional[str], optional
        The configuration object to load, by default None

    Returns
    -------
    Flask
        The WSGI interface
    """
    app = Flask(__name__)

    # Load configuration
    if config:
        app.config.from_object(config)
    elif "FLASK_SETTINGS_MODULE" in os.environ:
        app.config.from_object(os.environ["FLASK_SETTINGS_MODULE"])
    else:
        app.config.from_object("flaskapp.settings.common")

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)

    return app
