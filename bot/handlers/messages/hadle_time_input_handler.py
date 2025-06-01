from utils.messages import LANGUAGE_CONFIG
from telebot.async_telebot import AsyncTeleBot as Bot
from utils.buttons import get_menu_buttons
from service.user_service import UserService
from db.session import get_db_session
from telebot.types import Message
from models.models import UserStep
from utils.validator import Validator

async def handle_time_input(message: Message, bot: Bot) -> None:
    user_id: int = message.from_user.id

    with get_db_session() as session:
        user = UserService().get_user(user_id, session)
        if not user:
            await bot.send_message(message.chat.id, "Please send /start again.")
            return

        if user.step == UserStep.SETTING_UP:
            if not user.wake_up_time:
                if not Validator.validate_time(message.text):
                    await bot.send_message(message.chat.id, LANGUAGE_CONFIG[user.language]["time_error"])
                    return

                UserService().update_user(user_id, session, wake_up_time=message.text)
                await bot.send_message(message.chat.id, LANGUAGE_CONFIG[user.language]["sleep_time"])
            else:
                if not Validator.validate_time(message.text):
                    await bot.send_message(message.chat.id, LANGUAGE_CONFIG[user.language]["time_error"])
                    return

                UserService().update_user(
                    user_id,
                    session,
                    sleep_time=message.text,
                    step=UserStep.WORKING
                )
                await bot.send_message(
                    message.chat.id,
                    LANGUAGE_CONFIG[user.language]["saved"],
                    reply_markup=get_menu_buttons(user.language)
                )
