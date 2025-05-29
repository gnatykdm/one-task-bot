from dotenv import load_dotenv
from database.crud.service import UserCRUD
from database.database import get_session
from telebot.async_telebot import AsyncTeleBot
import asyncio
import os

load_dotenv()
TOKEN: str = os.getenv("API_TOKEN")

bot: AsyncTeleBot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'

    user_id: int = message.from_user.id  
    user_name: str = message.from_user.username or message.from_user.first_name or "Unknown"

    session = next(get_session())
    try:
        user = UserCRUD.create(session, t_id=user_id, t_name=user_name)
        print(user)
    finally:
        session.close()

    await bot.reply_to(message, f"User created: {user.t_name} (ID: {user.t_id})")
    await bot.reply_to(message, text)


asyncio.run(bot.polling())