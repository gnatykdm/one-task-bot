import os
import asyncio
from typing import Dict
from logging import Logger

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from models.models import LanguageEnum
from handlers.commands.menu import menu
from handlers.commands.note import NoteHandler
from handlers.messages.note_input import NoteInputHandler
from handlers.commands.start import handle_start
from handlers.messages.languages_start_choice import languages_start_choice_handler

from config.states import UserState
from utils.logs import setup_logger
from utils.messages import LANGUAGE_BUTTON_TO_ENUM, LANGUAGE_CONFIG

# Load environment variables
load_dotenv()
logger: Logger = setup_logger()

# User States Dictionary [user_id, user_state]
STATES: Dict[int, UserState] = {}

# Initialize bot
TOKEN: str = os.getenv("API_TOKEN")
if not TOKEN:
    logger.error("API_TOKEN not found in environment variables")
    raise SystemExit("Bot cannot start without API_TOKEN")

bot: AsyncTeleBot = AsyncTeleBot(TOKEN)

async def handle_language_specific_buttons(message: Message, language: LanguageEnum, handler_func) -> None:
    """Handle language-specific button actions."""
    try:
        await handler_func(message, bot)
        logger.info(f"Processed button for language {language} for user {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error processing button for language {language} for user {message.from_user.id}: {str(e)}")
        await bot.reply_to(message, "Failed to process selection. Please try again.")

async def handle_back_button(message: Message) -> None:
    """Handle back button action by returning to the menu."""
    user_id: int = message.from_user.id
    try:
        STATES[user_id] = UserState.WORKING  # Reset state
        await menu(message, bot)
        logger.info(f"Processed back button for user {user_id}")
    except Exception as e:
        logger.error(f"Error processing back button for user {user_id}: {str(e)}")
        await bot.reply_to(message, "Failed to process back button. Please try again.")

@bot.message_handler(commands=["start"])
async def start_command(message: Message) -> None:
    """Handle /start command."""
    user_id: int = message.from_user.id
    try:
        STATES[user_id] = UserState.WORKING  # Reset state
        await handle_start(message, bot)
        logger.info(f"Processed /start command for user {user_id}")
    except Exception as e:
        logger.error(f"Error processing /start command for user {user_id}: {str(e)}")
        await bot.reply_to(message, "An error occurred. Please try again later.")

@bot.message_handler(func=lambda m: m.text in LANGUAGE_BUTTON_TO_ENUM)
async def language_choice(message: Message) -> None:
    """Handle language selection."""
    user_id: int = message.from_user.id
    try:
        await languages_start_choice_handler.handle_start_choice_language(message, bot)
        logger.info(f"Processed language choice '{message.text}' for user {user_id}")
    except Exception as e:
        logger.error(f"Error processing language choice for user {user_id}: {str(e)}")
        await bot.reply_to(message, "Failed to process language selection. Please try again.")

@bot.message_handler(commands=["menu"])
async def menu_command(message: Message) -> None:
    """Handle /menu command."""
    user_id: int = message.from_user.id
    try:
        STATES[user_id] = UserState.WORKING  # Reset state
        await menu(message, bot)
        logger.info(f"Processed /menu command for user {user_id}")
    except Exception as e:
        logger.error(f"Error processing /menu command for user {user_id}: {str(e)}")
        await bot.reply_to(message, "Failed to display menu. Please try again.")

@bot.message_handler(commands=["note"])
@bot.message_handler(func=lambda m: any(m.text in LANGUAGE_CONFIG[lang]["menu_buttons"] for lang in [LanguageEnum.ENGLISH, LanguageEnum.RUSSIAN]))
async def note_command(message: Message) -> None:
    """Handle /note command or menu button for note creation."""
    user_id: int = message.from_user.id
    STATES[user_id] = UserState.MAKING_NOTE
    try:
        await NoteHandler().note(message, bot)
        logger.info(f"Processed /note command for user {user_id}")
    except Exception as e:
        logger.error(f"Error processing /note command for user {user_id}: {str(e)}")
        await bot.reply_to(message, "Failed to process note command. Please try again.")

@bot.message_handler(func=lambda m: (
    STATES.get(m.from_user.id) == UserState.MAKING_NOTE
    and m.text not in [LANGUAGE_CONFIG[lang]["back_button"] for lang in [LanguageEnum.ENGLISH, LanguageEnum.RUSSIAN]]
))
async def handle_note_input(message: Message) -> None:
    """Handle note input when user is in MAKING_NOTE state."""
    user_id: int = message.from_user.id
    try:
        await NoteInputHandler().note_input(message, bot)
        STATES[user_id] = UserState.WORKING
        logger.info(f"Processed note input for user {user_id}")
    except Exception as e:
        logger.error(f"Error processing note input for user {user_id}: {str(e)}")
        await bot.reply_to(message, "Failed to process note input. Please try again.")

@bot.message_handler(func=lambda m: any(m.text in LANGUAGE_CONFIG[lang]["back_button"] for lang in [LanguageEnum.ENGLISH, LanguageEnum.RUSSIAN]))
async def back_button_handler(message: Message) -> None:
    """Handle back button for all supported languages."""
    await menu(message, bot)
    logger.info(f"Processed back button for user {message.from_user.id}")

async def main() -> None:
    """Start the Telegram bot."""
    try:
        logger.info("Starting Telegram bot")
        await bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logger.error(f"Bot polling failed: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())