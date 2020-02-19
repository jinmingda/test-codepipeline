"""User models."""
from typing import Optional


class User:
    """A user of the app."""

    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        """A user of the app.

        Parameters
        ----------
        username : Optional[str], optional
            The unique user identifier, by default None
        password : Optional[str], optional
            The hashed password, by default None
        """
        self.username = username
        self.password = password


class Role():
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
