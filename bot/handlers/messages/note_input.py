from logging import Logger

from telebot.async_telebot import AsyncTeleBot as Bot
from telebot.types import Message

from db.session import get_db_session
from models.models import User
from service.note_service import NoteService
from service.user_service import UserService
from utils.buttons import get_menu_buttons
from utils.logs import setup_logger
from utils.messages import LANGUAGE_CONFIG
from utils.validator import Validator

class NoteInputHandler:
    def __init__(self, logger: Logger = None):
        self.logger = logger or setup_logger()
        self.user_service = UserService()
        self.note_service = NoteService()

    async def note_input(self, message: Message, bot: Bot) -> None:
        user_id: int = message.from_user.id

        with get_db_session() as session:
            user: User = self.user_service.get_user(user_id, session)
            if not user:
                self.logger.error(f"User not found: {user_id}")
                await bot.send_message(message.chat.id, "User not found. Please try /start again.")

            note_context = message.text
            if Validator.validate_note(note_context):
                self.note_service.create_note(user_id, note_context, session)
                self.logger.info(f"User {user_id} saved note: {note_context}")
                await bot.send_message(
                    message.chat.id,
                    LANGUAGE_CONFIG[user.language]["saved"],
                    reply_markup=get_menu_buttons(user.language))
            else:
                await bot.send_message(
                    message.chat.id,
                    LANGUAGE_CONFIG[user.language]["error"])
