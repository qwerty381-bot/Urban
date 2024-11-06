from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):

    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я - бот, помогающий твоему здоровью.')
    await message.answer('Привет! Я - бот, помогающий твоему здоровью.')

@dp.message_handler(text=['Colories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data_age = await state.get_data('age')
    data_growth = await state.get_data('growth')
    data_weight = await state.get_data('weight')
    calories = 10 * data_weight.weight + 6.25 * data_growth.growth - 5 * data_age.age + 5
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)