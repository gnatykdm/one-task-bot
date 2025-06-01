from utils.messages import LANGUAGE_CONFIG, LANGUAGE_BUTTON_TO_ENUM
from telebot.async_telebot import AsyncTeleBot as Bot
from utils.buttons import get_start_ask_time_button
from service.user_service import UserService
from utils.logs import setup_logger
from db.session import get_db_session
from telebot.types import Message

class LanguagesStartChoiceHandler:
    def __init__(self, logger=None):
        self.logger = logger or setup_logger()
        self.user_service = UserService()

    async def handle_start_choice_language(self, message: Message, bot: Bot) -> None:
        user_id = message.from_user.id
        text = message.text

        if text not in LANGUAGE_BUTTON_TO_ENUM:
            await bot.send_message(message.chat.id, "Please choose a valid language.")
            return

        language = LANGUAGE_BUTTON_TO_ENUM[text]

        with get_db_session() as session:
            user = self.user_service.get_user(user_id, session)
            if not user:
                self.logger.error(f"User not found: {user_id}")
                await bot.send_message(message.chat.id, "User not found. Please try /start again.")
                return

            self.user_service.update_user(user_id, session, language=language)
            self.logger.info(f"User {user_id} set language to {language}")

        await bot.send_message(
            message.chat.id,
            LANGUAGE_CONFIG[language]["ask_time"],
            reply_markup=get_start_ask_time_button(language)
        )

languages_start_choice_handler = LanguagesStartChoiceHandler()
async def handle_start_choice_language(message: Message, bot: Bot) -> None:
    await languages_start_choice_handler.handle_start_choice_language(message, bot)
