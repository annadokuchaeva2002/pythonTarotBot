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
from keyboards import kb_buy_course
from keyboards import kb_sign_up
from keyboards import kb_retreats
from keyboards import btn_Main_Menu
from data_base import db_unloader
from aiogram.dispatcher import FSMContext



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

async def command_tarot_course(message: types.Message):
    await db_unloader(19)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_astrology_course(message: types.Message):
    await db_unloader(20)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_bazi_course(message: types.Message):
    await db_unloader(21)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_energy_course(message: types.Message):
    await db_unloader(22)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_divination(message: types.Message):
    await db_unloader(23)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)

async def command_astrology(message: types.Message):
    await db_unloader(24)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)

async def command_bazi(message: types.Message):
    await db_unloader(25)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)

async def command_rituals(message: types.Message):
    await db_unloader(26)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)

async def command_meditations(message: types.Message):
    await db_unloader(27)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)

async def command_solstice(message: types.Message):
    await db_unloader(28)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)

async def command_chakras(message: types.Message):
    await db_unloader(29)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)

async def command_yoga(message: types.Message):
    await db_unloader(30)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)
# желаете приобрести курс

async def command_buy_course(message: types.Message):



# БЫЛО
# async def command_buy(message: types.Message):
#     await message.answer('Оформление покупки', reply_markup=kb_buy)

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

    # товары
    dp.register_message_handler(command_tarot_course, commands=['Курс_Таро'])
    dp.register_message_handler(command_astrology_course, commands=['Курс_Астрология'])
    dp.register_message_handler(command_bazi_course, commands=['Курс_Бацзы'])
    dp.register_message_handler(command_energy_course, commands=['Курс_Энергии'])
    # услуги
    dp.register_message_handler(command_divination, commands=['Гадание'])
    dp.register_message_handler(command_astrology, commands=['Астрология'])
    dp.register_message_handler(command_bazi, commands=['Бацзы'])
    dp.register_message_handler(command_rituals, commands=['Ритуалы'])
    # ретриты
    dp.register_message_handler(command_meditations, commands=['Медитации'])
    dp.register_message_handler(command_solstice, commands=['Гвоздестояние'])
    dp.register_message_handler(command_chakras, commands=['Чакры'])
    dp.register_message_handler(command_yoga, commands=['Йога'])
    # покупка
    dp.register_message_handler(command_buy_course, commands=['/Приобрести_курс'])

# БЫЛО
#     dp.register_message_handler(command_buy, commands=['Очищение', 'Интуиция', 'Карьера', 'Любовь'
#                                                            'Розовый_кварц', 'Горный_хрусталь', 'Красная_яшма', 'Аметист',
#                                                            'Лаванда', 'Мелисса', 'Пачули', 'Иланг-иланг',
#                                                            'Уэйта', 'Манара', 'Эры_Водолея', '78_дверей'])

    # async def command_(message: types.Message):
    #     await message.answer('Оформление покупки', reply_markup=kb_buy)








