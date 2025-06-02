from utils.buttons import get_language_buttons, get_menu_buttons
from telebot.async_telebot import AsyncTeleBot as Bot
from service.user_service import UserService
from utils.messages import LANGUAGE_CONFIG
from utils.logs import setup_logger
from db.session import get_db_session
from telebot.types import Message
from models.models import User, LanguageEnum
from logging import Logger
from typing import Optional

class StartCommandHandler:
    def __init__(self, logger: Optional[Logger] = None):
        self.logger = logger or setup_logger()
        self.user_service = UserService()

    async def handle_start(self, message: Message, bot: Bot) -> None:
        try:
            user_id: int = message.from_user.id
            user_name: str = message.from_user.username

            if not user_id or not user_name:
                self.logger.error(f"Invalid user data for /start: {user_id} ({user_name})")
                await bot.send_message(
                    message.chat.id,
                    LANGUAGE_CONFIG[LanguageEnum.ENGLISH]["error"]
                )
                return

            with get_db_session() as session:
                user: User = self.user_service.get_user(user_id, session)

                if user:
                    await bot.send_message(
                        message.chat.id,
                        LANGUAGE_CONFIG[user.language]["welcome_back"].format(user_name=user_name),
                        reply_markup=get_menu_buttons(user.language)
                    )
                else:
                    self.logger.info(f"New user {user_id} ({user_name})")
                    user = self.user_service.register_user(user_id, user_name, session)
                    await bot.send_message(
                        message.chat.id,
                        LANGUAGE_CONFIG[user.language]["welcome"].format(user_name=user_name),
                        reply_markup=get_language_buttons()
                    )

        except Exception as e:
            self.logger.error(f"Exception occurred while handling /start command: {str(e)}")
            try:
                language = user.language if user else LanguageEnum.ENGLISH
                await bot.send_message(
                    message.chat.id,
                    LANGUAGE_CONFIG[language]["error"]
                )
            except Exception as inner_e:
                self.logger.error(f"Failed to send error message: {str(inner_e)}")
                await bot.send_message(
                    message.chat.id,
                    "An unexpected error occurred. Please try again later."
                )

start_handler = StartCommandHandler()
async def handle_start(message: Message, bot: Bot) -> None:
    await start_handler.handle_start(message, bot)