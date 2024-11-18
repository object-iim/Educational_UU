# python.exe -m pip install --upgrade pip
# pip install -r requirements.txt
import aiogram
# import aiohttp
# import aiosignal
# import async_timeout
# import attrs
# import babel
# import certifi
# import charset_normalizer
# import frozenlist
# import idna
# import magic_filter
# import multidict
# import pytz
# import yarl

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'LOL12345:OMGWTF98765:BRB4L0lP0ny'
bot = Bot(token=api)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

@dispatcher.message_handler(commands=['start'])
async def start(message):
    try:
        print('Привет! Я бот помогающий твоему здоровью')
    except Exception as Hello:
        print(f"Ошибка в set_growth: {Hello}")

@dispatcher.message_handler()
async def all_messages(message):
    try:
        print('Введите команду /start, чтобы начать общение')
    except Exception as Please:
        print(f"Ошибка в set_growth: {Please}")

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)