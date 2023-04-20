from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_Main_Menu
from keyboards import kb_products
from keyboards import kb_services
from keyboards import kb_retreat
from keyboards import kb_Courses
from keyboards import kb_tarot
from keyboards import kb_stones
from keyboards import kb_candles
from keyboards import kb_oils
from keyboards import kb_buy


async def command_start(message: types.Message):
    await message.answer('Привет! Я бот интернет магазина Tarot shop, что Вас интересует?', reply_markup=kb_Main_Menu)

async def command_courses(message: types.Message):
    await message.answer('Какие курсы Вас интересуют?', reply_markup=kb_Courses)
async def command_services(message: types.Message):
    await message.answer('Какие услуги Вас интересуют?', reply_markup=kb_services)

async def command_products(message: types.Message):
    await message.answer('Какие товары Вас интересуют?', reply_markup=kb_products)
async def command_tours(message: types.Message):
    await message.answer('Какие ретриты Вас интересуют?', reply_markup=kb_retreat)

async def command_Main_Menu(message: types.Message):
    await message.answer('Что Вас интересует?', reply_markup=kb_Main_Menu)


async def command_tarot(message: types.Message):
    await message.answer('Какая колода Вас интересует?', reply_markup=kb_tarot)

async def command_oils(message: types.Message):
    await message.answer('Какое масло Вас интересует?', reply_markup=kb_oils)
async def command_stones(message: types.Message):
    await message.answer('Какой камень Вас интересует?', reply_markup=kb_stones)

async def command_candles(message: types.Message):
    await message.answer('Какая свеча Вас интересует?', reply_markup=kb_candles)

async def command_buy(message: types.Message):
    await message.answer('Оформление покупки', reply_markup=kb_buy)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_courses, commands=['Курсы'])
    dp.register_message_handler(command_services, commands=['Услуги'])
    dp.register_message_handler(command_products, commands=['Товары'])
    dp.register_message_handler(command_tours, commands=['Ретриты'])
    dp.register_message_handler(command_Main_Menu, commands=['Меню'])

    dp.register_message_handler(command_tarot, commands=['Таро'])
    dp.register_message_handler(command_oils, commands=['Масла'])
    dp.register_message_handler(command_stones, commands=['Камни'])
    dp.register_message_handler(command_candles, commands=['Свечи'])

    dp.register_message_handler(command_buy, commands=['Курс_Таро', 'Курс_Астрология',
                                                           'Курс_Бацзы', 'Курс_Энергии',
                                                           'Гадание', 'Астрология',
                                                           'Бацзы', 'Ритуалы', 'Медитации',
                                                           'Гвоздестояние', 'Чакры', 'Йога',
                                                           'Очищение', 'Интуиция', 'Карьера', 'Любовь'
                                                           'Розовый_кварц', 'Горный_хрусталь', 'Красная_яшма', 'Аметист',
                                                           'Лаванда', 'Мелисса', 'Пачули', 'Иланг-иланг',
                                                           'Уэйта', 'Манара', 'Эры_Водолея', '78_дверей'])








