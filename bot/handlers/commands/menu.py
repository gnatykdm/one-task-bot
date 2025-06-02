from telebot.async_telebot import AsyncTeleBot as Bot
from telebot.types import Message
from db.session import get_db_session
from service.user_service import UserService
from utils.buttons import get_menu_buttons
from utils.logs import setup_logger
from logging import Logger
from models.models import User
from utils.messages import LANGUAGE_CONFIG

logger: Logger = setup_logger()

async def menu(message: Message, bot: Bot) -> None:
    user_id: int = message.from_user.id

    with get_db_session() as session:
        user: User = UserService().get_user(user_id, session)
        if not user:
            logger.error(f"User not found: {user_id}")
            await bot.send_message(message.chat.id, "User not found. Please try /start again.")

        logger.info(f"User {user_id} sent menu")
        await bot.send_message(
            message.chat.id,
            LANGUAGE_CONFIG[user.language]["menu"].format(user_name=user.t_name),
            reply_markup=get_menu_buttons(user.language)
        )