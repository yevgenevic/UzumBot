from aiogram import types
import redis
from aiogram import Bot

from core.keyboards.buttons import btn3, commands

redis_db = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


async def generate_report(message: types.Message, bot: Bot):
    key = types.InlineKeyboardMarkup(inline_keyboard=btn3)
    if message.text == "/report":
        await message.answer(f"Здраствуйте {message.from_user.first_name}", reply_markup=key)
    else:
        await message.answer(f"Здраствуйте {message.from_user.first_name}")
        await bot.set_my_commands(commands)
