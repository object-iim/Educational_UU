from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = 'LOL12345:OMGWTF98765:BRB4L0lP0ny'
bot = Bot(token=api)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

keyboard_1 = ReplyKeyboardMarkup(resize_keyboard = True)
button_1 = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
keyboard_1.add(button_1)
keyboard_1.add(button_2)

keyboard_2 = InlineKeyboardMarkup()
button_3 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
button_4 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
keyboard_2.add(button_3)
keyboard_2.add(button_4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dispatcher.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup = keyboard_1)

@dispatcher.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup = keyboard_2)

@dispatcher.callback_query_handler(text = ['formulas'])
async def get_formulas(call):
    await call.message.answer('Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()
    await UserState.age.set()

@dispatcher.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dispatcher.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(key_age = message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dispatcher.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(key_growth = message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dispatcher.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(key_weight = message.text)
    data = await state.get_data()
    try:
        result = 10 * float(data['key_weight']) + 6.25 * float(data['key_growth']) - 5 * float(data['key_age']) - 161
        await message.answer(f'Необходимое количество килокалорий в сутки {result}. При условии, если Вы женского пола')
    except (ValueError, KeyError) as e:
        await message.answer('Пожалуйста, введите корректные значения для роста, веса и возраста')
    finally:
        await state.finish()

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)