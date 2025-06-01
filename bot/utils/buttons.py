from utils.messages import LANGUAGE_CONFIG, LANGUAGE_BUTTON_TO_ENUM
from telebot.types import ReplyKeyboardMarkup
from models.models import LanguageEnum
from utils.markup import get_markup

def get_start_buttons(language: LanguageEnum) -> ReplyKeyboardMarkup:
    return get_markup(LANGUAGE_CONFIG[language]["start_buttons"])

def get_menu_buttons(language: LanguageEnum) -> ReplyKeyboardMarkup:
    return get_markup(LANGUAGE_CONFIG[language]["menu_buttons"])

def get_language_buttons() -> ReplyKeyboardMarkup:
    return get_markup(LANGUAGE_BUTTON_TO_ENUM.keys())

def get_start_ask_time_button(language: LanguageEnum) -> ReplyKeyboardMarkup:
    return get_markup(LANGUAGE_CONFIG[language]["start_buttons_ask_time"])