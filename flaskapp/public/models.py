"""The domain models for the public package.

Unlike data model, domain model is another term for business logic layer. In general,
it links the presentation layer and  the database layer, and should be free of
infrastructure concerns, that is, it has no dependencies on low-level implementation
(Dependecy Inversion Principle in SOLID). Given that, the use of Flask-SQLAlchemy or
SQLAlchemy declarative syntax is not encouraged because it will tightly couple domain
models with particular databases technologies.
"""
from typing import Optional


class User:
    """A user of the app."""

    def __init__(self, username: Optional[str] = None):
        """A user of the app.

        Parameters
        ----------
        username : Optional[str], optional
            A unique user identifier
        """
        self.username = username
