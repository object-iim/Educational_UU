from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import time

from crud_functions import *
get_all_products()

api = "LOL12345:OMGWTF98765:BRB4L0lP0ny"
bot = Bot(token=api)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

keyboard_1 = ReplyKeyboardMarkup(resize_keyboard = True)
button_1 = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
button_3 = KeyboardButton(text = 'Купить')
keyboard_1.insert(button_1)
keyboard_1.insert(button_2)
keyboard_1.add(button_3)

keyboard_2 = InlineKeyboardMarkup()
button_4 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
button_5 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
keyboard_2.add(button_4)
keyboard_2.add(button_5)

keyboard_3 = InlineKeyboardMarkup(text="Выберите продукт для покупки: ")
button_6 = InlineKeyboardButton(text = 'Product1', callback_data = 'product_buying')
button_7 = InlineKeyboardButton(text = 'Product2', callback_data = 'product_buying')
button_8 = InlineKeyboardButton(text = 'Product3', callback_data = 'product_buying')
button_9 = InlineKeyboardButton(text = 'Product4', callback_data = 'product_buying')
keyboard_3.insert(button_6)
keyboard_3.insert(button_7)
keyboard_3.insert(button_8)
keyboard_3.insert(button_9)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dispatcher.message_handler(commands = ['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью", reply_markup = keyboard_1)

@dispatcher.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=keyboard_2)

@dispatcher.message_handler(text = ['Купить'])
async def get_buying_list(message):
    get_all_products()
    for number in range(1, 5):
        with open(f'{number}.png', "rb") as img: # картинки в основной директории, поэтому без file/
            await message.answer_photo(img)
            await message.answer(f'Название: {all_prcts[number-1][1]} |\n'
                                 f'Описание: {all_prcts[number-1][2]}| \n'
                                 f'Цена: {all_prcts[number-1][3]}')
        time.sleep(2.6)
    await message.answer(text=f'Выберите продукт для покупки: ', reply_markup=keyboard_3)

@dispatcher.callback_query_handler(text = ['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dispatcher.callback_query_handler(text = ['formulas'])
async def get_formulas(call):
    await call.message.answer('Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

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

@dispatcher.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)