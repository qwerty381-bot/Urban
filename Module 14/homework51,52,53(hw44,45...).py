from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = '7903980320:AAE6Q0MsfwZc72yhAEMyC4o3YEYs9uFk-V8'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
keyboard1.add(button1)
keyboard1.add(button2)
keyboard1.add(button3)

keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

keyboard3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')],
    ]
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я - бот, помогающий твоему здоровью.', reply_markup=keyboard1)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        await message.answer(text=f'Название: Product<{i}>| Описание:<{i}>| Цена: <{i*100}>', reply_markup=keyboard3)
        with open(f'Module13/images/{i}.png', 'rb') as img:
            await message.answer_photo(img)
        await message.answer(text='Выберите продукт для покупки: ', reply_markup=keyboard3)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer(text='Выберите опцию:', reply_markup=keyboard2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула расчета калорий: calories = 10 * weight + 6.25 * growth - 5 * age + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста, введите числовое значение для возраста.')
        return
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост в сантиметрах:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста, введите числовое значение для роста.')
        return
    await state.update_data(growth=int(message.text))  # Сохраняем рост как число
    await message.answer('Введите свой вес в килограммах:')
    await UserState.weight.set()  # Переход к следующему состоянию

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста, введите числовое значение для веса.')
        return
    await state.update_data(weight=int(message.text))  # Сохраняем вес как число

    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {calories}')

    await state.finish()

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)