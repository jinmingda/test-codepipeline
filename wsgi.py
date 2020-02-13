"""Exposes the WSGI callable as a module-level variable."""
from flaskapp.app import create_app

application = create_app()
