"""The app module, containing the app factory function."""
import os
from typing import Optional

from flask import Flask


def create_app(config: Optional[str] = None) -> Flask:
    """Create a Flask application using the app factory pattern.

    Parameters
    ----------
    config : Optional[str], optional
        The configuration module to load, by default None

    Returns
    -------
    Flask
        The WSGI interface
    """
    app = Flask(__name__)

    # load default configuration
    app.config.from_object("flaskapp.settings.common")

    # load environment configuration
    if "FLASK_SETTINGS_MODULE" in os.environ:
        app.config.from_envvar("FLASK_SETTINGS_MODULE")

    # load app specified configuration
    if config:
        app.config.from_pyfile(config)

    print(app.config)
    return app
