from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from generated_model import (
    UserSignUP,
)
from util.models.comment import Comment
from util.sessionmaker.crud import get_session, get_session2


class formService:

    def __init__(self, session=get_session()):
        self.session = session

    async def signUp(self, data):
        try:

            existing_user = self.session.query(
                UserSignUP).filter_by(email=data['email']).first()
            if existing_user:
                return "Error: Email already exists."

            contact = UserSignUP(**data)
            self.session.add(contact)
            self.session.commit()
            return "Data inserted successfully!"
        except IntegrityError as e:
            self.session.rollback()
            return f"Error: {str(e)}"
        except Exception as e:
            self.session.rollback()
            return f"Unexpected error: {str(e)}"

    async def login(self, data):
        try:
            existing_user = self.session.execute(
                select(UserSignUP).where(
                    UserSignUP.email == data['email'],
                    UserSignUP.password == data['password'])
            )
            user = existing_user.scalar_one_or_none()

            if user:
                return "Login successful"
            else:
                return "Error"
        except IntegrityError as e:
            self.session.rollback() 
            return f"Error: {str(e)}"


class commentService:

    def __init__(self, session=get_session2()):
        self.session = session

    async def comment(self, data):
        try:
            contact = Comment(**data)
            self.session.add(contact)
            self.session.commit()
            return "Comment inserted successfully"
        except IntegrityError as e:
            return f"Error: {str(e)}"