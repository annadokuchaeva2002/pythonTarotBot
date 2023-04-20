from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from create_bot import bot
from aiogram.dispatcher.filters import Text
from const import ADMIN

from data_base import db_loader

products_dict = {}


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    prise = State()


async def make_changer_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message('Здравствуй, госпожа')


async def cm_start(message: types.Message):
    if message.from_user.id == ADMIN:
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото')


async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN:
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
    await message.reply('Введите описание')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите цену')


async def load_prise(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    async with state.proxy() as data:
        await db_loader(data)
    await state.finish()


# await db_loader(query)

# async with state.proxy() as data:

# print('ВОТ ЭТО ОНО = ', str(data))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    # dp.register_message_handler(test, commands=['test'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_prise, state=FSMAdmin.prise)
    dp.register_message_handler(make_changer_command, commands=['Модератор'], is_chat_admin=True)