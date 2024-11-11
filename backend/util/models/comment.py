from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

meta = MetaData()


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(String)
    author = Column(String)
