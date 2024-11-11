from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.models.comment import Base


def get_session(db_url="sqlite:///new.db"):

    try:
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print(f"An error occurred while connecting to the database: {str(e)}")
        return None


def get_session2(db_url="sqlite:///comment.db"):

    try:
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print(f"An error occurred while connecting to the database: {str(e)}")
        return None
