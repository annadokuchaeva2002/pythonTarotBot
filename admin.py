from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from create_bot import bot
from aiogram.dispatcher.filters import Text
from const import ADMIN
from keyboards import kb_product_category, kb_admin, kb_view_types, \
    kb_view_types_tours, kb_view_types_product, kb_view_types_course, kb_view_types_service

from data_base import db_loader
from data_base import db_loader_courses
from data_base import db_loader_tour
from data_base import db_loader_services, get_admin_access, db_loader_admin, db_loader_mentor, db_delete_mentor, \
    db_delete_admin, db_all_cuses, db_delete_course, db_all_product, db_delete_product, db_delete_service, \
    db_all_service, db_all_tour, db_delete_tour, db_view_types_tour, db_view_types_product, db_view_types_service,\
    db_view_types_course, db_add_new_type_tour, db_add_new_type_product, db_add_new_type_service, \
    db_add_new_type_course, db_delete_type_courses, db_delete_type_product, db_delete_type_service, db_delete_type_tour

products_dict = {}


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    mentor = State()
    type_product = State()
    description = State()
    prise = State()

# Добавить запись о товаре в таблицу

async def cm_start(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')


async def cancel_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        curses_state = await state.get_state()
        if curses_state is None:
            return
        await state.finish()
        await message.reply('OK')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Введите название')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите id ментора')

async def load_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor'] = int(message.text)
    await FSMAdmin.next()
    await message.reply('Введите тип')

async def load_type_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type_product'] = int(message.text)
    await FSMAdmin.next()
    await message.reply('Введите описание')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите цену')

async def load_prise(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = (message.text)
    await FSMAdmin.next()
    await message.reply('Выберите категорию товара', reply_markup=kb_product_category)

async def command_products_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await db_loader(data)
    await state.finish()
    await message.reply('Запись добавлена в таблицу')

async def command_courses_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await db_loader_courses(data)
    await state.finish()
    await message.reply('Запись добавлена в таблицу')

async def command_tours_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await db_loader_tour(data)
    await state.finish()
    await message.reply('Запись добавлена в таблицу')

async def command_services_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await db_loader_services(data)
    await state.finish()
    await message.reply('Запись добавлена в таблицу')


# Проверка администратора

async def cm_get_admin_access(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await message.reply('Доступ открыт', reply_markup=kb_admin)
    else:
        await message.reply('Вы не являетесь аминистратором')

# Добавление администратора

class add_admin(StatesGroup):
    name = State()
    second_name = State()
    contact_account = State()
    tg_id_admin = State()

async def add_new_admin(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await add_admin.name.set()
        await message.reply('Введите имя')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def load_admin_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await add_admin.next()
    await message.reply('Введите фамилию')
async def load_admin_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['second_name'] = message.text
    await add_admin.next()
    await message.reply('Введите контактный аккаунт')
async def load_contact_account(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_account'] = message.text
    await add_admin.next()
    await message.reply('Введите tg id')
async def load_tg_id_admin(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id_admin'] = message.text
    async with state.proxy() as data:
        await db_loader_admin(data)
    await state.finish()
    await message.reply('Новый администратор добавлен')

# Добавление ментора

class add_mentor(StatesGroup):
    name = State()
    second_name = State()
    contact_account = State()
    tg_id_admin = State()

async def add_new_mentor(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await add_mentor.name.set()
        await message.reply('Введите имя')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def load_mentor_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await add_mentor.next()
    await message.reply('Введите фамилию')
async def load_mentor_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['second_name'] = message.text
    await add_mentor.next()
    await message.reply('Введите контактный аккаунт')
async def load_contact_account_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_account'] = message.text
    await add_mentor.next()
    await message.reply('Введите tg id')
async def load_tg_id_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id_mentor'] = message.text
    async with state.proxy() as data:
        await db_loader_mentor(data)
    await state.finish()
    await message.reply('Новый ментор добавлен')
# Удаление ментора
class Form_delete_mentor(StatesGroup):
    id_mentor = State()

async def delete_mentor(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_mentor.id_mentor.set()
        await message.reply('Введиете id ментора')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def delete_id_mentor(message: types.Message, state: FSMContext):
    userID = message.from_user.id
    id_mentor = int(message.text)
    await db_delete_mentor(id_mentor, userID)
    await state.finish()

# Удаление админа
class Form_delete_admin(StatesGroup):
    id_admin = State()

async def delete_admin(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_admin.id_admin.set()
        await message.reply('Введиете id администратора')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def delete_id_admin(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    id_admin = int(message.text)
    await db_delete_admin(id_admin, user_id)
    await state.finish()


# Удалить курс
class Form_delete_course(StatesGroup):
    id_course = State()

async def delete_course(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_course.id_course.set()
        await message.reply('Введиете id курса')
        await db_all_cuses(user_id)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def delete_id_course(message: types.Message, state: FSMContext):
    id_course = int(message.text)
    user_id = message.from_user.id
    await db_delete_course(id_course, user_id)
    await state.finish()

# Удалить товар
class Form_delete_product(StatesGroup):
    id_product = State()

async def delete_product(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_product.id_product.set()
        await message.reply('Введиете id товара')
        await db_all_product(user_id)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def delete_id_product(message: types.Message, state: FSMContext):
    id_product = int(message.text)
    user_id = message.from_user.id
    await db_delete_product(id_product, user_id)
    await state.finish()
# Удалить услугу
class Form_delete_service(StatesGroup):
    id_service = State()

async def delete_service(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_service.id_service.set()
        await message.reply('Введиете id услуги')
        await db_all_service(user_id)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def delete_id_service(message: types.Message, state: FSMContext):
    id_service = int(message.text)
    user_id = message.from_user.id
    await db_delete_service(id_service, user_id)
    await state.finish()

# Удалить тур
class Form_delete_tour(StatesGroup):
    id_tour = State()

async def delete_tour(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_tour.id_tour.set()
        await message.reply('Введиете id ретрита')
        await db_all_tour(user_id)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def delete_id_tour(message: types.Message, state: FSMContext):
    id_tour = int(message.text)
    user_id = message.from_user.id
    await db_delete_tour(id_tour, user_id)
    await state.finish()

# ДОБАВИТЬ ТИПЫ ТУРОВ ВВОД/ВЫВОД/УДАЛЕНИЕ

async def view_types(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await message.reply("Выберите категорию", reply_markup=kb_view_types)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# Показать тип туров
async def view_types_tour(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await db_view_types_tour(user_id)
        await message.reply("Выберите действие", reply_markup=kb_view_types_tours)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# Показать тип товаров
async def view_types_product(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await db_view_types_product(user_id)
        await message.reply("Выберите действие", reply_markup=kb_view_types_product)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# Показать тип услуг
async def view_types_service(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await db_view_types_service(user_id)
        await message.reply("Выберите действие", reply_markup=kb_view_types_service)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# Показать тип курсов
async def view_types_course(message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await db_view_types_course(user_id)
        await message.reply("Выберите действие", reply_markup=kb_view_types_course)
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

# вернуться в админское меню
async def back_admin (message: types.Message):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await message.reply("Что желаете посмотреть?", reply_markup=kb_admin)
    else:
        await message.reply('Вы не являетесь администратором')


# ДОБАВИТЬ ТИПЫ ТУРОВ

class new_type_tour(StatesGroup):
    tour_name = State()

async def add_new_type_tour (message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await new_type_tour.tour_name.set()
        await message.reply('Введите название типа ретрита')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def add_new_type_tour_(message: types.Message, state: FSMContext):
    Tour_name = (message.text)
    await db_add_new_type_tour(Tour_name)
    await state.finish()
    await message.reply('Тип тура добавлен')

# ДОБАВИТЬ ТИПЫ ТОВАРОВ

class new_type_product(StatesGroup):
    product_name = State()

async def add_new_type_product (message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await new_type_product.product_name.set()
        await message.reply('Введите название типа товара')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def add_new_type_product_(message: types.Message, state: FSMContext):
    product_name = (message.text)
    await db_add_new_type_product(product_name)
    await state.finish()
    await message.reply('Тип товара добавлен')
#
# # ДОБАВИТЬ ТИПЫ УСЛУГ
#
class new_type_service(StatesGroup):
    service_name = State()

async def add_new_type_service (message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await new_type_service.service_name.set()
        await message.reply('Введите название типа услуги')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def add_new_type_service_(message: types.Message, state: FSMContext):
    service_name = (message.text)
    await db_add_new_type_service(service_name)
    await state.finish()
    await message.reply('Тип услуги добавлен')

# # ДОБАВИТЬ ТИПЫ КУРСОВ
#
class new_type_course(StatesGroup):
    course_name = State()

async def add_new_type_course(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await new_type_course.course_name.set()
        await message.reply('Введите название типа курса')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')

async def add_new_type_course_(message: types.Message, state: FSMContext):
    course_name = (message.text)
    await db_add_new_type_course(course_name)
    await state.finish()
    await message.reply('Тип курса добавлен')

# #Удалить тип курсы
class Form_delete_type_courses(StatesGroup):
    id_type_courses = State()

async def courses_type_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_type_courses.id_type_courses.set()
        await message.reply('Введите id типа, который хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')


async def courses_type_record_delete_(message: types.Message, state: FSMContext):
    id_courses_type = int(message.text)
    await db_delete_type_courses(id_courses_type)
    await state.finish()
    await message.reply('Тип удалён')

# #Удалить тип товары
class Form_delete_type_product(StatesGroup):
    id_type_product = State()

async def product_type_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_type_product.id_type_product.set()
        await message.reply('Введите id типа, который хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')


async def product_type_record_delete_(message: types.Message, state: FSMContext):
    id_product_type = int(message.text)
    await db_delete_type_product(id_product_type)
    await state.finish()
    await message.reply('Тип удалён')

# #Удалить тип услуги
class Form_delete_type_service(StatesGroup):
    id_type_service = State()

async def service_type_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_type_service.id_type_service.set()
        await message.reply('Введите id типа, который хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')


async def service_type_record_delete_(message: types.Message, state: FSMContext):
    id_service_type = int(message.text)
    await db_delete_type_service(id_service_type)
    await state.finish()
    await message.reply('Тип удалён')

# #Удалить тип курсы
class Form_delete_type_tour(StatesGroup):
    id_type_tour = State()

async def tour_type_record_delete(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await get_admin_access(user_id):
        await Form_delete_type_tour.id_type_tour.set()
        await message.reply('Введите id типа, который хотите удалить')
    else:
        await message.reply('У вас нет прав для выполнения этой команды')


async def tour_type_record_delete_(message: types.Message, state: FSMContext):
    id_tour_type = int(message.text)
    await db_delete_type_tour(id_tour_type)
    await state.finish()
    await message.reply('Тип удалён')







def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)

    dp.register_message_handler(load_mentor, state=FSMAdmin.mentor)
    dp.register_message_handler(load_type_product, state=FSMAdmin.type_product)
    dp.register_message_handler(load_prise, state=FSMAdmin.prise)

    dp.register_message_handler(command_courses_category, commands=['Курсы_таблица'])
    dp.register_message_handler(command_services_category, commands=['Услуги_таблица'])
    dp.register_message_handler(command_products_category, commands=['Товары_таблица'])
    dp.register_message_handler(command_tours_category, commands=['Ретриты_таблица'])
    dp.register_message_handler(cm_get_admin_access, commands=['Админ'], state=None)

    dp.register_message_handler(add_new_admin, commands=['Добавить_админа'], state=None)
    dp.register_message_handler(load_admin_name, state=add_admin.name)
    dp.register_message_handler(load_admin_surname, state=add_admin.second_name)
    dp.register_message_handler(load_contact_account, state=add_admin.contact_account)
    dp.register_message_handler(load_tg_id_admin, state=add_admin.tg_id_admin)

    dp.register_message_handler(add_new_mentor, commands=['Добавить_ментора'], state=None)
    dp.register_message_handler(load_mentor_name, state=add_mentor.name)
    dp.register_message_handler(load_mentor_surname, state=add_mentor.second_name)
    dp.register_message_handler(load_contact_account_mentor, state=add_mentor.contact_account)
    dp.register_message_handler(load_tg_id_mentor, state=add_mentor.tg_id_admin)

    dp.register_message_handler(delete_mentor, commands=['Удалить_ментора'], state=None)
    dp.register_message_handler(delete_id_mentor, state=Form_delete_mentor.id_mentor)

    dp.register_message_handler(delete_admin, commands=['Удалить_админа'], state=None)
    dp.register_message_handler(delete_id_admin, state=Form_delete_admin.id_admin)

    dp.register_message_handler(delete_course, commands=['Удалить_курс'], state=None)
    dp.register_message_handler(delete_id_course, state=Form_delete_course.id_course)

    dp.register_message_handler(delete_product, commands=['Удалить_товар'], state=None)
    dp.register_message_handler(delete_id_product, state=Form_delete_product.id_product)

    dp.register_message_handler(delete_service, commands=['Удалить_услугу'], state=None)
    dp.register_message_handler(delete_id_service, state=Form_delete_service.id_service)

    dp.register_message_handler(delete_tour, commands=['Удалить_ретрит'], state=None)
    dp.register_message_handler(delete_id_tour, state=Form_delete_tour.id_tour)

    dp.register_message_handler(view_types, commands=['Типы'], state=None)
    dp.register_message_handler(back_admin, commands=['Админ_меню'], state=None)

    dp.register_message_handler(view_types_course, commands=['Показать_типы_курсов'], state=None)
    dp.register_message_handler(view_types_product, commands=['Показать_типы_товаров'], state=None)
    dp.register_message_handler(view_types_service, commands=['Показать_типы_услуг'], state=None)
    dp.register_message_handler(view_types_tour, commands=['Показать_типы_ретритов'], state=None)

    dp.register_message_handler(add_new_type_tour, commands=['Добавить_тип_ретрита'], state=None)
    dp.register_message_handler(add_new_type_tour_, state=new_type_tour.tour_name)

    dp.register_message_handler(add_new_type_product, commands=['Добавить_тип_товара'], state=None)
    dp.register_message_handler(add_new_type_product_, state=new_type_product.product_name)

    dp.register_message_handler(add_new_type_service, commands=['Добавить_тип_услуг'], state=None)
    dp.register_message_handler(add_new_type_service_, state=new_type_service.service_name)

    dp.register_message_handler(add_new_type_course, commands=['Добавить_тип_курса'], state=None)
    dp.register_message_handler(add_new_type_course_, state=new_type_course.course_name)



    dp.register_message_handler(courses_type_record_delete, commands=['Удалить_тип_курса'], state=None)
    dp.register_message_handler(courses_type_record_delete_, state=Form_delete_type_courses.id_type_courses)

    dp.register_message_handler(product_type_record_delete, commands=['Удалить_тип_товара'], state=None)
    dp.register_message_handler(product_type_record_delete_, state=Form_delete_type_product.id_type_product)

    dp.register_message_handler(service_type_record_delete, commands=['Удалить_тип_услуг'], state=None)
    dp.register_message_handler(service_type_record_delete_, state=Form_delete_type_service.id_type_service)

    dp.register_message_handler(tour_type_record_delete, commands=['Удалить_тип_ретрита'], state=None)
    dp.register_message_handler(tour_type_record_delete_, state=Form_delete_type_tour.id_type_tour)


