from logging import Logger

from telebot.async_telebot import AsyncTeleBot as Bot
from telebot.types import Message

from db.session import get_db_session
from service.note_service import NoteService
from service.user_service import UserService
from utils.buttons import get_back_button
from utils.logs import setup_logger
from models.models import User
from utils.messages import LANGUAGE_CONFIG


class NoteHandler:
    def __init__(self, logger: Logger = None):
        self.logger = logger or setup_logger()
        self.user_service = UserService()
        self.note_service = NoteService()

    async def note(self, message: Message, bot: Bot) -> None:
        user_id = message.from_user.id

        with get_db_session() as session:
            user: User = self.user_service.get_user(user_id, session)
            if not user:
                self.logger.error(f"User not found: {user_id}")
                await bot.send_message(message.chat.id, "User not found. Please try /start again.")

            await bot.send_message(
                message.chat.id,
                LANGUAGE_CONFIG[user.language]["make_note"],
                reply_markup=get_back_button(user.language)
            )

