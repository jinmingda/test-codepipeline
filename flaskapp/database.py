"""Database module including functions for initialization using factory patterns."""
from flask import Flask
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Session, sessionmaker

metadata = MetaData()


def init_app(app: Flask) -> None:
    """Initialize SQLAlchemy context in an app factory."""
    engine = create_engine(
        app.config["DATABASE_URL"],
        echo=True,
        convert_unicode=True,
        isolation_level="SERIALIZABLE",
    )
    metadata.bind = engine
    return None


def create_session() -> Session:
    """Create a database session using factory pattern."""
    return sessionmaker(bind=metadata.bind)
