from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import get_settings


class Base(DeclarativeBase):
    pass


def get_engine():
    settings = get_settings()
    if not settings.database_url:
        return None
    return create_engine(settings.database_url, pool_pre_ping=True)


def get_session() -> Generator[Session, None, None]:
    engine = get_engine()
    if engine is None:
        raise RuntimeError("DATABASE_URL is not configured")

    session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    with session_factory() as session:
        yield session


def check_database() -> bool:
    engine = get_engine()
    if engine is None:
        return False

    with engine.connect() as connection:
        connection.execute(text("select 1"))
    return True
