from db.repository.user import UserRepository
from models.models import User, LanguageEnum
from utils.logs import setup_logger
from typing import Optional
from sqlalchemy.orm import Session
from logging import Logger
import datetime

logger: Logger = setup_logger()

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.logger = logger

    def register_user(
        self,
        telegram_id: int,
        username: str,
        session: Session,
        language: LanguageEnum = LanguageEnum.ENGLISH,
        wake_up_time: Optional[datetime.datetime] = None,
        sleep_time: Optional[datetime.datetime] = None
    ) -> User:
        """
        Register a new user or return an existing one.

        Args:
            telegram_id: Unique Telegram ID of the user.
            username: Username of the user.
            session: SQLAlchemy session for database operations.
            language: User's preferred language (default: ENGLISH).
            wake_up_time: Optional wake-up time for the user.
            sleep_time: Optional sleep time for the user.

        Returns:
            User: The created or existing user object.

        Raises:
            Exception: If an error occurs during user registration.
        """
        try:
            user = self.user_repo.get(session, telegram_id)
            if not user:
                user = self.user_repo.create(
                    session=session,
                    t_id=telegram_id,
                    t_name=username,
                    language=language,
                    wake_up_time=wake_up_time,
                    sleep_time=sleep_time
                )
                self.logger.info(f"Created new user: {telegram_id} ({username})")
            else:
                self.logger.info(f"User already exists: {telegram_id} ({username})")
            return user
        except Exception as e:
            self.logger.error(f"Error registering user {telegram_id}: {str(e)}")
            raise

    def get_user(self, telegram_id: int, session: Session) -> Optional[User]:
        """
        Retrieve a user by their Telegram ID.

        Args:
            telegram_id: Unique Telegram ID of the user.
            session: SQLAlchemy session for database operations.

        Returns:
            Optional[User]: The user object if found, else None.

        Raises:
            Exception: If an error occurs during retrieval.
        """
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
        """
        Update user attributes.

        Args:
            telegram_id: Unique Telegram ID of the user.
            session: SQLAlchemy session for database operations.
            **kwargs: Key-value pairs of attributes to update.

        Returns:
            Optional[User]: The updated user object if found, else None.

        Raises:
            Exception: If an error occurs during update.
        """
        try:
            user = self.user_repo.update(session, telegram_id, **kwargs)
            if user:
                self.logger.info(f"Updated user: {telegram_id}")
            else:
                self.logger.warning(f"User not found for update: {telegram_id}")
            return user
        except Exception as e:
            session.rollback()
            self.logger.error(f"Failed to update user {telegram_id}: {str(e)}")
            raise

    def delete_user(self, telegram_id: int, session: Session) -> bool:
        """
        Delete a user by their Telegram ID.

        Args:
            telegram_id: Unique Telegram ID of the user.
            session: SQLAlchemy session for database operations.

        Returns:
            bool: True if the user was deleted, False if not found.

        Raises:
            Exception: If an error occurs during deletion.
        """
        try:
            success = self.user_repo.delete(session, telegram_id)
            if success:
                self.logger.info(f"Deleted user: {telegram_id}")
            else:
                self.logger.warning(f"User not found for deletion: {telegram_id}")
            return success
        except Exception as e:
            session.rollback()
            self.logger.error(f"Error deleting user {telegram_id}: {str(e)}")
            raise

    def list_all_users(self, session: Session) -> list[User]:
        """
        Retrieve all users.

        Args:
            session: SQLAlchemy session for database operations.

        Returns:
            list[User]: List of all user objects.

        Raises:
            Exception: If an error occurs during retrieval.
        """
        try:
            users = self.user_repo.list_all(session)
            self.logger.info(f"Retrieved {len(users)} users")
            return users
        except Exception as e:
            self.logger.error(f"Error retrieving all users: {str(e)}")
            raise

    def check_if_user_exists(self, telegram_id: int, session: Session) -> bool:
        """
        Check if a user exists by their Telegram ID.

        Args:
            telegram_id: Unique Telegram ID of the user.
            session: SQLAlchemy session for database operations.

        Returns:
            bool: True if the user exists, False otherwise.

        Raises:
            Exception: If an error occurs during the check.
        """
        try:
            exists = self.user_repo.get(session, telegram_id) is not None
            self.logger.info(f"Checked user existence: {telegram_id}, exists={exists}")
            return exists
        except Exception as e:
            self.logger.error(f"Error checking if user {telegram_id} exists: {str(e)}")
            raise