"""The settings module for production environment."""
from .common import env
from .common import *  # noqa

# When the envvar for storing the Sentry DSN is set to SENTRY_DSN, 'flask shell' will
# send messages to Sentry whether or not the DSN is loaded into the app config. Not
# sure why, but not using SENTRY_DSN as envvar seems to help.
SENTRY_DSN = env.str("SENTRYDSN", None)
