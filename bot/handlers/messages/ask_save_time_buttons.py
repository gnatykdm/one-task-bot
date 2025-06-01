from utils.messages import LANGUAGE_CONFIG
from telebot.async_telebot import AsyncTeleBot as Bot
from utils.buttons import get_menu_buttons
from service.user_service import UserService
from utils.logs import setup_logger
from models.models import UserStep
from db.session import get_db_session
from telebot.types import Message
from logging import Logger

class AskSaveTimeButtonsHandler:
    def __init__(self, logger: Logger =None):
        self.logger = logger or setup_logger()
        self.user_service = UserService()

    async def handle_ask_save_time_buttons(self, message: Message, bot: Bot) -> None:
        user_id = message.from_user.id
        text = message.text

        with get_db_session() as session:
            user = self.user_service.get_user(user_id, session)
            if not user:
                self.logger.error(f"User not found: {user_id}")
                await bot.send_message(message.chat.id, "User not found. Please try /start again.")
                return

            save_time = text == LANGUAGE_CONFIG[user.language]["start_buttons_ask_time"][0]
            if save_time:
                user.step = UserStep.SETTING_UP
                self.user_service.update_user(user_id, session, step=UserStep.SETTING_UP)
                await bot.send_message(message.chat.id, LANGUAGE_CONFIG[user.language]["wake_time"])
            else:
                user.step = UserStep.WORKING
                self.user_service.update_user(user_id, session, step=UserStep.WORKING)
                await bot.send_message(message.chat.id, LANGUAGE_CONFIG[user.language]["menu"],
                                       reply_markup=get_menu_buttons(user.language))

ask_save_time_buttons_handler = AskSaveTimeButtonsHandler()
async def handle_ask_save_time_buttons(message: Message, bot: Bot) -> None:
    await ask_save_time_buttons_handler.handle_ask_save_time_buttons(message, bot)