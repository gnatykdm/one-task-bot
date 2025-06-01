from handlers.messages.languages_start_choice import languages_start_choice_handler
from handlers.messages.ask_save_time_buttons import ask_save_time_buttons_handler
from handlers.commands.menu import menu
from handlers.messages.hadle_time_input_handler import handle_time_input
from utils.messages import LANGUAGE_BUTTON_TO_ENUM, LANGUAGE_CONFIG
from handlers.commands.start import handle_start
from models.models import UserStep, LanguageEnum
from telebot.async_telebot import AsyncTeleBot
from service.user_service import UserService
from db.session import get_db_session
from utils.validator import Validator
from utils.logs import setup_logger
from telebot.types import Message
from dotenv import load_dotenv
from logging import Logger
import asyncio
import os

load_dotenv()

logger: Logger = setup_logger()
TOKEN: str = os.getenv("API_TOKEN")
if not TOKEN:
    logger.error("No token provided")
    exit(1)

bot: AsyncTeleBot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=["start"])
async def handle_start_command(message) -> None:
    await handle_start(message, bot)

@bot.message_handler(func=lambda message: message.text in LANGUAGE_BUTTON_TO_ENUM)
async def handle_language_choice(message) -> None:
    await languages_start_choice_handler.handle_start_choice_language(message, bot)

@bot.message_handler(func=lambda m: m.text in LANGUAGE_CONFIG[LanguageEnum.ENGLISH]["start_buttons_ask_time"])
async def ask_time_buttons_english(message: Message):
    await ask_save_time_buttons_handler.handle_ask_save_time_buttons(message, bot)

@bot.message_handler(func=lambda m: m.text in LANGUAGE_CONFIG[LanguageEnum.RUSSIAN]["start_buttons_ask_time"])
async def ask_time_buttons_russian(message: Message):
    await ask_save_time_buttons_handler.handle_ask_save_time_buttons(message, bot)

@bot.message_handler(commands=["menu"])
async def handle_menu(message) -> None:
    await menu(message, bot)

@bot.message_handler(func=lambda m: Validator.validate_time(m.text))
async def time_input_handler(message: Message):
    with get_db_session() as session:
        user = UserService().get_user(message.from_user.id, session)
        if user and user.step == UserStep.SETTING_UP:
            await handle_time_input(message, bot)

async def main() -> None:
    logger.info("Starting bot")
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())