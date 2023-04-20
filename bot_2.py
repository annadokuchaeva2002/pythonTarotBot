import telebot
from telebot import types
import const
bot = telebot.TeleBot(const.API_TOKEN)
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_courses = types.KeyboardButton('Курсы 👩‍🎓')
btn_services = types.KeyboardButton('Услуги 🤝')
btn_products = types.KeyboardButton('Товары 🛍️')
btn_tours = types.KeyboardButton('Туры 🌍')
markup_menu.add(btn_courses, btn_services, btn_products, btn_tours)

products_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_tarot = types.KeyboardButton('Карты таро 🃏')
btn_oils = types.KeyboardButton('Эфирные масла ☯')
btn_stones = types.KeyboardButton('Камни и минералы 🔮')
btn_candles = types.KeyboardButton('Свечи 🕯')
btn_Main_Menu = types.KeyboardButton('Главное меню')
products_menu.add(btn_tarot, btn_oils, btn_stones, btn_candles, btn_Main_Menu)

tarot_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_tarot_1 = types.KeyboardButton('Колода Уэйта')
btn_tarot_2 = types.KeyboardButton('Колода Манара')
btn_tarot_3 = types.KeyboardButton('Колода Эры водолея')
btn_tarot_4 = types.KeyboardButton('Колода 78 дверей')
btn_Main_Menu = types.KeyboardButton('Главное меню')
tarot_menu.add(btn_tarot_1, btn_tarot_2, btn_tarot_3, btn_tarot_4, btn_Main_Menu)

oils_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_oils_1 = types.KeyboardButton('Иланг-иланг')
btn_oils_2 = types.KeyboardButton('Пачули')
btn_oils_3 = types.KeyboardButton('Мелисса')
btn_oils_4 = types.KeyboardButton('Лаванда')
btn_Main_Menu = types.KeyboardButton('Главное меню')
oils_menu.add(btn_oils_1, btn_oils_2, btn_oils_3, btn_oils_4, btn_Main_Menu)

stones_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_stones_1 = types.KeyboardButton('Розовый кварц')
btn_stones_2 = types.KeyboardButton('Горный хрусталь')
btn_stones_3 = types.KeyboardButton('Красная яшма')
btn_stones_4 = types.KeyboardButton('Аметист')
btn_Main_Menu = types.KeyboardButton('Главное меню')
stones_menu.add(btn_stones_1, btn_stones_2, btn_stones_3, btn_stones_4, btn_Main_Menu)

candles_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_candles_1 = types.KeyboardButton('Любовь')
btn_candles_2 = types.KeyboardButton('Карьера')
btn_candles_3 = types.KeyboardButton('Интуиция')
btn_candles_4 = types.KeyboardButton('От негатива')
btn_Main_Menu = types.KeyboardButton('Главное меню')
candles_menu.add(btn_candles_1, btn_candles_2, btn_candles_3, btn_candles_4, btn_Main_Menu)


product_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_buy = types.KeyboardButton('Купить')
btn_Main_Menu = types.KeyboardButton('Главное меню')
product_menu.add(btn_buy, btn_Main_Menu)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот интернет магазина Tarot shop, какие товары вас интересуют?", reply_markup=markup_menu)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == 'Курсы 👩‍🎓':
		bot.reply_to(message, "Наши актуальные курсы: тра ля ля ", reply_markup=product_menu)
	if message.text == 'Услуги 🤝':
		bot.reply_to(message, "Услуги", reply_markup=product_menu)
	if message.text == 'Товары 🛍️':
		bot.reply_to(message, "Товары ", reply_markup=products_menu)
	if message.text == 'Туры 🌍':
		bot.reply_to(message, "Туры", reply_markup=product_menu)

	if message.text == 'Карты таро 🃏':
		bot.reply_to(message, "Выберите колоду", reply_markup=tarot_menu)
	if message.text == 'Колода Уэйта':
		bot.reply_to(message, "	Колода Уйта (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Колода Манара':
		bot.reply_to(message, "	Колода Манара(Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Колода Эры водолея':
		bot.reply_to(message, "	Эры водолея(Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Колода 78 дверей':
		bot.reply_to(message, "	78 дверей(Описание картинка цена)", reply_markup=product_menu)

	if message.text == 'Эфирные масла ☯':
		bot.reply_to(message, "Выберите эфирное масло", reply_markup=oils_menu)
	if message.text == 'Иланг-иланг':
		bot.reply_to(message, "	Иланг-иланг (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Пачули':
		bot.reply_to(message, "	Пачули (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Мелисса':
		bot.reply_to(message, "	Мелисса(Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Лаванда':
		bot.reply_to(message, "	Лаванда(Описание картинка цена)", reply_markup=product_menu)

	if message.text == 'Камни и минералы 🔮':
		bot.reply_to(message, "Выберите Камень или минерал", reply_markup=stones_menu)
	if message.text == 'Розовый кварц':
		bot.reply_to(message, "Розовый кварц (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Горный хрусталь':
		bot.reply_to(message, "	Горный хрусталь (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Красная яшма':
		bot.reply_to(message, "	Красная яшма (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Аметист':
		bot.reply_to(message, "	Аметист(Описание картинка цена)", reply_markup=product_menu)


	if message.text == 'Свечи 🕯':
		bot.reply_to(message, "Выберите	Свечу", reply_markup=candles_menu)
	if message.text == 'Любовь':
		bot.reply_to(message, "Любовь (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Карьера':
		bot.reply_to(message, "	Карьера (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'Интуиция':
		bot.reply_to(message, "	Интуиция (Описание картинка цена)", reply_markup=product_menu)
	if message.text == 'От негатива':
		bot.reply_to(message, "	От негатива(Описание картинка цена)", reply_markup=product_menu)

	if message.text == 'Главное меню':
		bot.reply_to(message, "Какие товары вас интересуют?", reply_markup=markup_menu)







bot.infinity_polling()