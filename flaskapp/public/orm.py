"""The SQL Abstraction Layer."""
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import mapper

from flaskapp import database

from . import models

users = Table(
    "users",
    database.metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(), unique=True),
    Column("password", String()),
)

roles = Table(
    "roles",
    database.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(), unique=True),
    Column("description", String()),
)


def start_mappers() -> None:
    """Manual ORM."""
    mapper(models.User, users)
    mapper(models.Role, roles)
    return None
