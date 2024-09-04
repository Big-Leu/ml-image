from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

meta = MetaData()


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
