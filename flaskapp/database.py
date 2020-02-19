from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

metadata = MetaData()


def init_app(app) -> None:
    engine = create_engine(app.config["DATABASE_URL"],
                           echo=True,
                           convert_unicode=True,
                           isolation_level="SERIALIZABLE")
    metadata.bind = engine
    return None


def session_factory() -> scoped_session:
    return scoped_session(sessionmaker(bind=metadata.bind))
