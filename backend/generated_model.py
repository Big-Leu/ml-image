from sqlalchemy import Column, Integer, String
from util.base.crud import Base


class UserSignUP(Base):
    __tablename__ = 'signup'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(Integer)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(String)
    author = Column(String)
