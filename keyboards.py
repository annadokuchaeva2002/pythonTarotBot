from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btn_courses = KeyboardButton('/Курсы')
btn_services = KeyboardButton('/Услуги')
btn_products = KeyboardButton('/Товары')
btn_tours = KeyboardButton('/Ретриты')

kb_Main_Menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_Main_Menu.add(btn_courses).add(btn_services).add(btn_products).add(btn_tours)
# add - в столбец insert - по свободному месту row - в строку


# ////////////////////ТОВАРЫ////////////////////
btn_tarot = KeyboardButton('/Таро')
btn_oils = KeyboardButton('/Масла')
btn_stones = KeyboardButton('/Камни')
btn_candles = KeyboardButton('/Свечи')
btn_Main_Menu = KeyboardButton('/Меню')

kb_products = ReplyKeyboardMarkup(resize_keyboard=True)
kb_products.add(btn_tarot).insert(btn_oils).add(btn_stones).insert(btn_candles).add(btn_Main_Menu)

btn_tarot_1 = KeyboardButton('/Уэйта')
btn_tarot_2 = KeyboardButton('/Манара')
btn_tarot_3 = KeyboardButton('/Эры_Водолея')
btn_tarot_4 = KeyboardButton('/78_дверей')
btn_Main_Menu = KeyboardButton('/Меню')

kb_tarot = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tarot.add(btn_tarot_1).insert(btn_tarot_2).add(btn_tarot_3).insert(btn_tarot_4).add(btn_Main_Menu)

btn_oils_1 = KeyboardButton('/Иланг-иланг')
btn_oils_2 = KeyboardButton('/Пачули')
btn_oils_3 = KeyboardButton('/Мелисса')
btn_oils_4 = KeyboardButton('/Лаванда')
btn_Main_Menu = KeyboardButton('/Меню')

kb_oils = ReplyKeyboardMarkup(resize_keyboard=True)
kb_oils.add(btn_oils_1).insert(btn_oils_2).add(btn_oils_3).insert(btn_oils_4).add(btn_Main_Menu)


btn_stones_1 = KeyboardButton('/Розовый_кварц')
btn_stones_2 = KeyboardButton('/Горный_хрусталь')
btn_stones_3 = KeyboardButton('/Красная_яшма')
btn_stones_4 = KeyboardButton('/Аметист')
btn_Main_Menu = KeyboardButton('/Меню')

kb_stones = ReplyKeyboardMarkup(resize_keyboard=True)
kb_stones.add(btn_stones_1).insert(btn_stones_2).add(btn_stones_3).insert(btn_stones_4).add(btn_Main_Menu)

btn_candles_1 = KeyboardButton('/Любовь')
btn_candles_2 = KeyboardButton('/Карьера')
btn_candles_3 = KeyboardButton('/Интуиция')
btn_candles_4 = KeyboardButton('/Очищение')
btn_Main_Menu = KeyboardButton('/Меню')

kb_candles = ReplyKeyboardMarkup(resize_keyboard=True)
kb_candles.add(btn_candles_1).insert(btn_candles_2).add(btn_candles_3).insert(btn_candles_4).add(btn_Main_Menu)



# ////////////////////УСЛУГИ////////////////////
btn_services_1 = KeyboardButton('/Гадание')
btn_services_2 = KeyboardButton('/Астрология')
btn_services_3 = KeyboardButton('/Бацзы')
btn_services_4 = KeyboardButton('/Ритуалы')
btn_Main_Menu = KeyboardButton('/Меню')

kb_services = ReplyKeyboardMarkup(resize_keyboard=True)
kb_services.add(btn_services_1).insert(btn_services_2).add(btn_services_3).insert(btn_services_4).add(btn_Main_Menu)
# ////////////////////КУРСЫ////////////////////
btn_Courses_1 = KeyboardButton('/Курс_Таро')
btn_Courses_2 = KeyboardButton('/Курс_Астрология')
btn_Courses_3 = KeyboardButton('/Курс_Бацзы')
btn_Courses_4 = KeyboardButton('/Курс_Энергии')
btn_Main_Menu = KeyboardButton('/Меню')

kb_Courses = ReplyKeyboardMarkup(resize_keyboard=True)
kb_Courses.add(btn_Courses_1).insert(btn_Courses_2).add(btn_Courses_3).insert(btn_Courses_4).add(btn_Main_Menu)
# ////////////////////ретриты////////////////////
btn_retreat_1 = KeyboardButton('/Медитации')
btn_retreat_2 = KeyboardButton('/Гвоздестояние')
btn_retreat_3 = KeyboardButton('/Чакры')
btn_retreat_4 = KeyboardButton('/Йога')
btn_Main_Menu = KeyboardButton('/Меню')

kb_retreat = ReplyKeyboardMarkup(resize_keyboard=True)
kb_retreat.add(btn_retreat_1).insert(btn_retreat_2).add(btn_retreat_3).insert(btn_retreat_4).add(btn_Main_Menu)

btn_buy = KeyboardButton('/Купить')
btn_Main_Menu = KeyboardButton('/Меню')
kb_buy = ReplyKeyboardMarkup(resize_keyboard=True)
kb_buy.add(btn_buy).add(btn_Main_Menu)

btn_buy_course = KeyboardButton('/Приобрести_курс')
btn_Main_Menu = KeyboardButton('/Меню')
kb_buy_course = ReplyKeyboardMarkup(resize_keyboard=True)
kb_buy_course.add(btn_buy_course).add(btn_Main_Menu)

btn_sign_up = KeyboardButton('/Записаться')
btn_Main_Menu = KeyboardButton('/Меню')
kb_sign_up = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sign_up.add(btn_sign_up).add(btn_Main_Menu)

btn_sign_up_retreats = KeyboardButton('/Принять_участие')
btn_Main_Menu = KeyboardButton('/Меню')
kb_retreats = ReplyKeyboardMarkup(resize_keyboard=True)
kb_retreats.add(btn_sign_up_retreats).add(btn_Main_Menu)

btn_buy_product = KeyboardButton('/Приобрести_товар')
btn_Main_Menu = KeyboardButton('/Меню')
kb_buy_product = ReplyKeyboardMarkup(resize_keyboard=True)
kb_buy_product.add(btn_buy_product).add(btn_Main_Menu)


btn_courses_category = KeyboardButton('/Курсы_таблица')
btn_services_category = KeyboardButton('/Услуги_таблица')
btn_products_category = KeyboardButton('/Товары_таблица')
btn_tours_category = KeyboardButton('/Ретриты_таблица')

kb_product_category = ReplyKeyboardMarkup(resize_keyboard=True)
kb_product_category.add(btn_courses_category).add(btn_services_category).add(btn_products_category).add(btn_tours_category)

btn_download = KeyboardButton('/Загрузить')
btn_add_admin = KeyboardButton('/Добавить_админа')
btn_add_mentor = KeyboardButton('/Добавить_ментора')
btn_delete_mentor = KeyboardButton('/Удалить_ментора')
btn_delete_admin = KeyboardButton('/Удалить_админа')
btn_delete_course = KeyboardButton('/Удалить_курс')
btn_delete_product = KeyboardButton('/Удалить_товар')
btn_delete_service = KeyboardButton('/Удалить_услугу')
btn_delete_tour = KeyboardButton('/Удалить_ретрит')
btn_types = KeyboardButton('/Типы')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(btn_delete_tour).insert(btn_delete_course).add(btn_delete_product).insert(btn_delete_service)\
    .add(btn_download).insert(btn_types).add(btn_add_admin).insert(btn_delete_admin).add(btn_add_mentor)\
    .insert(btn_delete_mentor).add(btn_Main_Menu)


btn_view_types_course = KeyboardButton('/Показать_типы_курсов')
btn_view_types_product = KeyboardButton('/Показать_типы_товаров')
btn_view_types_service = KeyboardButton('/Показать_типы_услуг')
btn_view_types_tour = KeyboardButton('/Показать_типы_ретритов')
btn_admin_menu = KeyboardButton('/Админ_меню')

kb_view_types = ReplyKeyboardMarkup(resize_keyboard=True)
kb_view_types.add(btn_view_types_course).add(btn_view_types_product).add(btn_view_types_service)\
    .add(btn_view_types_tour).add(btn_admin_menu)

btn_add_types_tour = KeyboardButton('/Добавить_тип_ретрита')
btn_delete_types_tour = KeyboardButton('/Удалить_тип_ретрита')

kb_view_types_tours = ReplyKeyboardMarkup(resize_keyboard=True)
kb_view_types_tours.add(btn_add_types_tour).add(btn_delete_types_tour).add(btn_types)

btn_add_types_product = KeyboardButton('/Добавить_тип_товара')
btn_delete_types_product = KeyboardButton('/Удалить_тип_товара')

kb_view_types_product = ReplyKeyboardMarkup(resize_keyboard=True)
kb_view_types_product.add(btn_add_types_product).add(btn_delete_types_product).add(btn_types)

btn_add_types_service = KeyboardButton('/Добавить_тип_услуг')
btn_delete_types_service = KeyboardButton('/Удалить_тип_услуг')

kb_view_types_service = ReplyKeyboardMarkup(resize_keyboard=True)
kb_view_types_service.add(btn_add_types_service).add(btn_delete_types_service).add(btn_types)

btn_add_types_course = KeyboardButton('/Добавить_тип_курса')
btn_delete_types_course = KeyboardButton('/Удалить_тип_курса')

kb_view_types_course = ReplyKeyboardMarkup(resize_keyboard=True)
kb_view_types_course.add(btn_add_types_course).add(btn_delete_types_course).add(btn_types)

btn_courses_record = KeyboardButton('/Курсы_запись')
btn_services_record = KeyboardButton('/Услуги_запись')
btn_products_record = KeyboardButton('/Товары_заказы')
btn_tours_record = KeyboardButton('/Ретриты_запись')

kb_mentor = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mentor.add(btn_courses_record).add(btn_services_record).add(btn_products_record).add(btn_tours_record).add(btn_Main_Menu)

btn_courses_record_delete = KeyboardButton('/Курсы_удалить_запись')
btn_services_record_delete = KeyboardButton('/Услуги_удалить_запись')
btn_products_record_delete = KeyboardButton('/Товары_удалить_заказ')
btn_tours_record_delete = KeyboardButton('/Ретриты_удалить_запись')
btn_mentor_Menu = KeyboardButton('/Назад')

kb_mentor_delete_courses = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mentor_delete_courses .add(btn_courses_record_delete).add(btn_mentor_Menu).add(btn_Main_Menu)

kb_mentor_delete_services = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mentor_delete_services .add(btn_services_record_delete).add(btn_mentor_Menu).add(btn_Main_Menu)

kb_mentor_delete_products = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mentor_delete_products .add(btn_products_record_delete).add(btn_mentor_Menu).add(btn_Main_Menu)

kb_mentor_delete_tours = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mentor_delete_tours .add(btn_tours_record_delete).add(btn_mentor_Menu).add(btn_Main_Menu)