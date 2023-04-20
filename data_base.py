import psycopg2
import os
from config import host, user, password, db_name
from create_bot import bot

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


# async def db_unloader(identifier):
#     try:
#         connection = psycopg2.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=db_name
#         )
#
#         with connection.cursor() as c:
#             c.execute(f"SELECT * FROM product WHERE id_product={identifier}")
#             card = c.fetchone()
#             bot.send_message(text=str(card))
#
#
#         connection.commit()
#
#     except Exception as e:
#       print(e)
#
#     finally:
#         c.close()
