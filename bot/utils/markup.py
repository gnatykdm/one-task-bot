from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from typing import List

def get_markup(buttons: List[str]) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(*[KeyboardButton(button) for button in buttons])
    return markup
