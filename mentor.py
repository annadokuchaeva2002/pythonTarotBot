from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards import kb_mentor, kb_mentor_delete_courses, kb_mentor_delete_tours, kb_mentor_delete_products, kb_mentor_delete_services
from data_base import get_mentor_access, db_view_tour, db_view_product, db_view_course, db_view_services, \
    db_delete_record_tour, db_delete_record_service, db_delete_record_products, db_delete_record_courses
# Проверка ментора
async def cm_get_mentor_access(message: types.Message):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await message.reply('Доступ открыт', reply_markup=kb_mentor)
        # await message.reply(reply_markup=kb_mentor_delete_courses)
    else:
        await message.reply('Вы не являетесь ментором')

# Посмотреть ретриты

async def view_tour(message: types.Message):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await db_view_tour(user_id)
        await message.reply("Желаете удалить запись?", reply_markup=kb_mentor_delete_tours)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# Посмотреть товары

async def view_product(message: types.Message):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await db_view_product(user_id)
        await message.reply("Желаете удалить запись?", reply_markup=kb_mentor_delete_products)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# Посмотреть курсы

async def view_course(message: types.Message):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await db_view_course(user_id)
        await message.reply("Желаете удалить запись?", reply_markup=kb_mentor_delete_courses)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# Посмотреть услуги

async def view_services(message: types.Message):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await db_view_services(user_id)
        await message.reply("Желаете удалить запись?", reply_markup=kb_mentor_delete_services)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

#Удалить ретриты

class Form_delete_tour(StatesGroup):
    id_user_tour = State()

async def tour_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await Form_delete_tour.id_user_tour.set()
        await message.reply('Введите id пользователя, которого хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def tour_record_delete_(message: types.Message, state: FSMContext):
    id_user_tour = int(message.text)
    await db_delete_record_tour(id_user_tour)
    await state.finish()
    await message.reply('Участник тура удалён')

#Удалить услуги
class Form_delete_service(StatesGroup):
    id_user_service = State()

async def service_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await Form_delete_service.id_user_service.set()
        await message.reply('Введите id пользователя, которого хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def service_record_delete_(message: types.Message, state: FSMContext):
    id_service_buyer = int(message.text)
    await db_delete_record_service(id_service_buyer)
    await state.finish()
    await message.reply('Клиент удалён')


# #Удалить товар
class Form_delete_products(StatesGroup):
    id_user_products = State()

async def products_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await Form_delete_products.id_user_products.set()
        await message.reply('Введите id пользователя, которого хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def products_record_delete_(message: types.Message, state: FSMContext):
    id_products_buyer = int(message.text)
    await db_delete_record_products(id_products_buyer)
    await state.finish()
    await message.reply('Клиент удалён')

# #Удалить курсы
class Form_delete_courses(StatesGroup):
    id_user_courses = State()

async def courses_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await Form_delete_courses.id_user_courses.set()
        await message.reply('Введите id пользователя, которого хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')


async def courses_record_delete_(message: types.Message, state: FSMContext):
    id_courses_buyer = int(message.text)
    await db_delete_record_courses(id_courses_buyer)
    await state.finish()
    await message.reply('Клиент удалён')



async def back (message: types.Message):
    user_id = message.from_user.id
    if await get_mentor_access(user_id):
        await message.reply("Желаете посмотреть запись?", reply_markup=kb_mentor)
    else:
        await message.reply('Вы не являетесь ментором')


def register_handlers_mentor(dp: Dispatcher):
    dp.register_message_handler(cm_get_mentor_access, commands=['Ментор'], state=None)
    dp.register_message_handler(view_tour, commands=['Ретриты_запись'], state=None)
    dp.register_message_handler(view_product, commands=['Товары_заказы'], state=None)
    dp.register_message_handler(view_course, commands=['Курсы_запись'], state=None)
    dp.register_message_handler(view_services, commands=['Услуги_запись'], state=None)

    dp.register_message_handler(courses_record_delete, commands=['Курсы_удалить_запись'],state=None)
    dp.register_message_handler(courses_record_delete_, state=Form_delete_courses.id_user_courses)

    dp.register_message_handler(service_record_delete, commands=['Услуги_удалить_запись'],state=None)
    dp.register_message_handler(service_record_delete_, state=Form_delete_service.id_user_service)

    dp.register_message_handler(products_record_delete, commands=['Товары_удалить_заказ'],state=None)
    dp.register_message_handler(products_record_delete_, state=Form_delete_products.id_user_products)

    dp.register_message_handler(tour_record_delete, commands=['Ретриты_удалить_запись'], state=None)
    dp.register_message_handler(tour_record_delete_, state=Form_delete_tour.id_user_tour)

    dp.register_message_handler(back, commands=['Назад'], state=None)