from db.repository.user import UserRepository
from models.models import User
from utils.logs import setup_logger
from typing import Optional
from sqlalchemy.orm import Session
from logging import Logger

logger: Logger = setup_logger()

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.logger = logger

    def register_user(self, telegram_id: int, username: str, session: Session) -> User:
        try:
            user = self.user_repo.get(session, telegram_id)
            if not user:
                user = self.user_repo.create(session, telegram_id, username)
                self.logger.info(f"Created new user: {telegram_id} ({username})")
            else:
                self.logger.info(f"User already exists: {telegram_id} ({username})")
            return user
        except Exception as e:
            self.logger.error(f"Error registering user {telegram_id}: {str(e)}")
            raise

    def get_user(self, telegram_id: int, session: Session) -> Optional[User]:
        try:
            user = self.user_repo.get(session, telegram_id)
            if user:
                self.logger.info(f"Retrieved user: {telegram_id}")
            else:
                self.logger.warning(f"User not found: {telegram_id}")
            return user
        except Exception as e:
            self.logger.error(f"Error retrieving user {telegram_id}: {str(e)}")
            raise

    def update_user(self, telegram_id: int, session: Session, **kwargs) -> Optional[User]:
        try:
            user = self.user_repo.get(session, telegram_id)
            if not user:
                return None
            for key, value in kwargs.items():
                setattr(user, key, value)
            session.commit()
            return user
        except Exception as e:
            session.rollback()
            logger.error(f"Failed to update user {telegram_id}: {e}")
            return None

    def check_if_user_exists(self, telegram_id: int, session: Session) -> bool:
        try:
            user = self.user_repo.get(session, telegram_id)
            return user is not None
        except Exception as e:
            self.logger.error(f"Error checking if user {telegram_id} exists: {str(e)}")
            raise