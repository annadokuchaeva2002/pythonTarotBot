import psycopg2
import os
from config import host, user, password, db_name
from create_bot import bot

import tabulate
from tabulate import tabulate

from aiogram import types, Dispatcher

async def db_loader(data):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        photo = data['photo']
        name = data['name']
        description = data['description']
        price = data['price']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO product (price, product_name, description, product_pic) VALUES ({price}, '{name}', '{description}', '{photo}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()


async def db_unloader(identifier):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT product_name, description, price, product_pic FROM product WHERE id_product={identifier}")
            card = c.fetchall()
            a = card[0]
            await bot.send_photo(chat_id=550517550, photo=a[3], caption="<b>" + a[0] + "</b>\n" + a[1] + "\n" + "Цена в рублях: " + str(a[2]), parse_mode="HTML")
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()
