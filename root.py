import logging
import sys
from aiogram import Bot, Dispatcher, types

from core.keyboards.buttons import commands
from core.handlers.basic import generate_report
import asyncio
import redis
from core.keyboards.buttons import btn_подтверждение, btn3
from core.settings import settings
from ostatki_google import google_sheets_ostatki
from postcsv import ostatki_db, prodaja_db
from prodaja_google import google_sheets_prodaja
from db import select_url_ostatki, select_url_prodaja

dp = Dispatcher()


@dp.callback_query(
    lambda query: query.data in ['vse', "beauty4you", 'luckykids', 'topprice', 'tobe', 'smokecases'])
async def analiz(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer("загружаю...")
    name = query.data
    url = select_url_ostatki(name)[0]
    url1 = select_url_prodaja(name)[0]
    google_sheets = google_sheets_ostatki(url)
    google_sheets = google_sheets_prodaja(url1)
    await query.message.answer(f"{google_sheets}")
    await query.message.delete()


async def start_bot(bot: Bot):
    await bot.set_my_commands(commands)


async def stop_bot(bot: Bot):
    await bot.set_my_commands(commands)


async def main() -> None:
    bot = Bot(token=settings.bots.bot_token)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(generate_report)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
