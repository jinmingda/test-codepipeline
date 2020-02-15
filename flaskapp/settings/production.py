"""The settings module for production environment."""
from .common import env
from .common import *  # noqa

SENTRY_DSN = env.str("SENTRY_DSN", None)
