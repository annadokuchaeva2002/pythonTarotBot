from aiogram import types, Dispatcher
from keyboards import kb_retreats, kb_buy_product, kb_sign_up, kb_buy_course, kb_oils, kb_candles, \
    kb_stones, kb_tarot, kb_Courses, kb_retreat, kb_services, kb_products, kb_Main_Menu
from data_base import db_unloader, db_unloader_service, db_unloader_tour, db_unloader_product, \
    db_loader_course_student, db_loader_buyer_of_goods, db_loader_service_buyer, db_loader_tour_visitor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

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
    ID = message.from_user.id
    await db_unloader("Курс таро", ID)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_astrology_course(message: types.Message):
    ID = message.from_user.id
    await db_unloader("Курс астрология", ID)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_bazi_course(message: types.Message):
    ID = message.from_user.id
    await db_unloader("Курс ба-цзы", ID)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_energy_course(message: types.Message):
    ID = message.from_user.id
    await db_unloader("Курс энергии", ID)
    await message.answer('Желаете приобрести курс?', reply_markup=kb_buy_course)

async def command_divination(message: types.Message):
    ID = message.from_user.id
    await db_unloader_service("Гадание", ID)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)

async def command_astrology(message: types.Message):
    ID = message.from_user.id
    await db_unloader_service("Астрология", ID)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)

async def command_bazi(message: types.Message):
    ID = message.from_user.id
    await db_unloader_service("Ба-цзы", ID)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)

async def command_rituals(message: types.Message):
    ID = message.from_user.id
    await db_unloader_service("Ритуалы", ID)
    await message.answer('Желаете записаться?', reply_markup=kb_sign_up)
#
async def command_meditations(message: types.Message):
    ID = message.from_user.id
    await db_unloader_tour("Медитации", ID)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)

async def command_solstice(message: types.Message):
    ID = message.from_user.id
    await db_unloader_tour("Гвоздестояние", ID)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)

async def command_chakras(message: types.Message):
    ID = message.from_user.id
    await db_unloader_tour("Чакры", ID)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)

async def command_yoga(message: types.Message):
    ID = message.from_user.id
    await db_unloader_tour("Йога", ID)
    await message.answer('Желаете записаться на ретрит?', reply_markup=kb_retreats)

# /ПРОДУКТ
#
async def command_cleansing(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Очищение", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)
async def command_intuition(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Интуиция", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)
async def command_career(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Карьера – Свеча «Спираль Богатства»", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)
async def command_love(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Любовь - Свеча «Влюблённые»", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)

async def command_rose_quartz(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Розовый кварц", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)
async def command_rhinestone(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Горный хрусталь", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)
async def command_red_yashma(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Красная яшма", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)
async def command_amethyst(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Аметист", ID)
    await message.answer('Желаете приобрести свечу?', reply_markup=kb_buy_product)

async def command_lavender(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Лаванда", ID)
    await message.answer('Желаете приобрести масло?', reply_markup=kb_buy_product)
async def command_melissa(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Мелисса", ID)
    await message.answer('Желаете приобрести масло?', reply_markup=kb_buy_product)
async def command_patchouli(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Пачули", ID)
    await message.answer('Желаете приобрести масло?', reply_markup=kb_buy_product)
async def command_ylang_ylang(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Иланг-иланг", ID)
    await message.answer('Желаете приобрести масло?', reply_markup=kb_buy_product)


async def command_waite_tarot(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Таро Уэйта", ID)
    await message.answer('Желаете приобрести карты?', reply_markup=kb_buy_product)
async def command_manara(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Манара", ID)
    await message.answer('Желаете приобрести карты?', reply_markup=kb_buy_product)
async def command_age_aquarius(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("Эра Водолея", ID)
    await message.answer('Желаете приобрести карты?', reply_markup=kb_buy_product)
async def command_78_doors(message: types.Message):
    ID = message.from_user.id
    await db_unloader_product("78 дверей", ID)
    await message.answer('Желаете приобрести карты?', reply_markup=kb_buy_product)


# приобрести курс

class Form(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    contact_account = State()
    course = State()

async def command_buy_course(message: types.Message):
    await Form.name.set()
    await message.answer('Введите ваше имя')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await Form.next()
        await message.reply('Введите вашу фамилию')

async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
        await Form.next()
        await message.reply('Введите ваше отчество')

async def load_patronymic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
        await Form.next()
        await message.reply('Введите ваше имя пользователя (@ИмяПользователяТГ)')

async def load_contact_account(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_account'] = message.text
        await Form.next()
        await message.reply('Введите id курса')


async def load_course(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['course'] = int(message.text)
    async with state.proxy() as data:
        await db_loader_course_student(data)
        await message.reply('Заявка на прохождение курса сформирована, скоро с Вами свяжется наш куратор. \n Спасибо, что выбрали tarot shop💕')
    await state.finish()


# Услуга
class Form_services(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    contact_account = State()
    service = State()

async def command_buy_services(message: types.Message):
    await Form_services.name.set()
    await message.answer('Введите ваше имя')

async def load_name_services(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await Form_services.next()
        await message.reply('Введите вашу фамилию')

async def load_surname_services(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
        await Form_services.next()
        await message.reply('Введите ваше отчество')

async def load_patronymic_services(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
        await Form_services.next()
        await message.reply('Введите ваше имя пользователя (@ИмяПользователяТГ)')

async def load_contact_account_services(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_account'] = message.text
        await Form_services.next()
        await message.reply('Введите id услуги')

async def load_services(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service'] = int(message.text)
    async with state.proxy() as data:
        await db_loader_service_buyer(data)
        await message.reply('Скоро с Вами свяжется наш практик. \n Спасибо, что выбрали tarot shop💕')
    await state.finish()
 # приобрести товар


class Form_products(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    address = State()
    contact_account = State()
    product = State()


async def command_buy_product(message: types.Message):
    await Form_products.name.set()
    await message.answer('Введите ваше имя')

async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await Form_products.next()
        await message.reply('Введите вашу фамилию')

async def load_product_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
        await Form_products.next()
        await message.reply('Введите ваше отчество')

async def load_product_patronymic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
        await Form_products.next()
        await message.reply('Адрес доставки')

async def load_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
        await Form_products.next()
        await message.reply('Введите ваше имя пользователя (@ИмяПользователяТГ)')

async def load_contact_account_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_account'] = message.text
        await Form_products.next()
        await message.reply('Введите id товара')

async def load_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product'] = int(message.text)
        data['contact_account'] =message.from_user.id
    async with state.proxy() as data:
        await db_loader_buyer_of_goods(data)
    await state.finish()
    await message.reply('Скоро с Вами свяжется наш сотрудник \n Спасибо, что выбрали tarot shop💕')

# ретрит

class Form_tour(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()
    contact_account = State()
    tour = State()


async def command_buy_tour(message: types.Message):
    await Form_tour.name.set()
    await message.answer('Введите ваше имя')

async def load_name_tour(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await Form_tour.next()
        await message.reply('Введите вашу фамилию')

async def load_surname_tour(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
        await Form_tour.next()
        await message.reply('Введите ваше отчество')

async def load_patronymic_tour(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
        await Form_tour.next()
        await message.reply('Введите ваше имя пользователя (@ИмяПользователяТГ)')

async def load_contact_account_tour(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_account'] = message.text
        await Form_tour.next()
        await message.reply('Введите id ретрита')


async def load_tour(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tour'] = int(message.text)
    async with state.proxy() as data:
        await db_loader_tour_visitor(data)
        await message.reply('Заявка на участие в ретрите отпрвлена, скоро с Вами свяжется наш куратор. \n Спасибо, что выбрали tarot shop💕')
    await state.finish()


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

    # курсы
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
    # товары
    dp.register_message_handler(command_love, commands=['Любовь'])
    dp.register_message_handler(command_career, commands=['Карьера'])
    dp.register_message_handler(command_intuition, commands=['Интуиция'])
    dp.register_message_handler(command_cleansing, commands=['Очищение'])

    dp.register_message_handler(command_rose_quartz, commands=['Розовый_кварц'])
    dp.register_message_handler(command_rhinestone, commands=['Горный_хрусталь'])
    dp.register_message_handler(command_red_yashma, commands=['Красная_яшма'])
    dp.register_message_handler(command_amethyst, commands=['Аметист'])

    dp.register_message_handler(command_lavender, commands=['Лаванда'])
    dp.register_message_handler(command_melissa, commands=['Мелисса'])
    dp.register_message_handler(command_patchouli, commands=['Пачули'])
    dp.register_message_handler(command_ylang_ylang, commands=['Иланг-иланг'])

    dp.register_message_handler(command_waite_tarot, commands=['Уэйта'])
    dp.register_message_handler(command_manara, commands=['Манара'])
    dp.register_message_handler(command_age_aquarius, commands=['Эры_Водолея'])
    dp.register_message_handler(command_78_doors, commands=['78_дверей'])
    # покупка
    dp.register_message_handler(command_buy_course, commands=['Приобрести_курс'], state=None)
    dp.register_message_handler(load_name, state=Form.name)
    dp.register_message_handler(load_surname, state=Form.surname)
    dp.register_message_handler(load_patronymic, state=Form.patronymic)
    dp.register_message_handler(load_contact_account, state=Form.contact_account)
    dp.register_message_handler(load_course, state=Form.course)

    dp.register_message_handler(command_buy_tour, commands=['Принять_участие'], state=None)
    dp.register_message_handler(load_name_tour, state=Form_tour.name)
    dp.register_message_handler(load_surname_tour, state=Form_tour.surname)
    dp.register_message_handler(load_patronymic_tour, state=Form_tour.patronymic)
    dp.register_message_handler(load_contact_account_tour, state=Form_tour.contact_account)
    dp.register_message_handler(load_tour, state=Form_tour.tour)

    dp.register_message_handler(command_buy_product, commands=['Приобрести_товар'], state=None)
    dp.register_message_handler(load_product_name, state=Form_products.name)
    dp.register_message_handler(load_product_surname, state=Form_products.surname)
    dp.register_message_handler(load_product_patronymic, state=Form_products.patronymic)
    dp.register_message_handler(load_address, state=Form_products.address)
    dp.register_message_handler(load_contact_account_product, state=Form_products.contact_account)
    dp.register_message_handler(load_product, state=Form_products.product)

    dp.register_message_handler(command_buy_services, commands=['Записаться'], state=None)
    dp.register_message_handler(load_name_services, state=Form_services.name)
    dp.register_message_handler(load_surname_services, state=Form_services.surname)
    dp.register_message_handler(load_patronymic_services, state=Form_services.patronymic)
    dp.register_message_handler(load_contact_account_services, state=Form_services.contact_account)
    dp.register_message_handler(load_services, state=Form_services.service)












