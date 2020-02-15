"""The settings module for production environment."""
from .common import env
from .common import *  # noqa

# Don't store the DSN envvar as SENTRY_DSN because it'll be sliently loaded by the SDK.
# https://github.com/getsentry/sentry-python/blob/master/sentry_sdk/client.py#L56
SENTRY_DSN = env.str("SENTRYDSN", None)
