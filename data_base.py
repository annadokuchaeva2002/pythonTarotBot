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
        mentor = data['mentor']
        type_product = data['type_product']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO product (price, product_name, description, product_pic, id_mentor, type_id) VALUES ('{price}', '{name}', '{description}', '{photo}', '{mentor}', '{type_product}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_courses(data):
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
        mentor = data['mentor']
        type_product = data['type_product']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO courses (price, courses_name, description, courses_pic, id_mentor, type_id) VALUES ({price}, '{name}', '{description}', '{photo}', '{mentor}', '{type_product}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_tour(data):
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
        mentor = data['mentor']
        type_product = data['type_product']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO tour (price, tour_name, description, tour_pic, id_mentor, type_id) VALUES ({price}, '{name}', '{description}', '{photo}', '{mentor}', '{type_product}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_services(data):
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
        mentor = data['mentor']
        type_product = data['type_product']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO services (price, services_name, description, services_pic, id_mentor, id_service_type) VALUES ({price}, '{name}', '{description}', '{photo}', '{mentor}', '{type_product}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()


async def db_unloader(identifier, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT courses_name, description, price, courses_pic FROM courses WHERE courses_name= '{identifier}'")
            card = c.fetchall()
            a = card[0]
            await bot.send_photo(chat_id=userID, photo=a[3], caption="<b>" + a[0] + "</b>\n" + a[1] + "\n" + "Цена в рублях: " + str(a[2]) + "\n" + "ID - " + str(identifier), parse_mode="HTML")
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_unloader_service(identifier, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT services_name, description, price, services_pic FROM services WHERE services_name= '{identifier}'")
            card = c.fetchall()
            a = card[0]
            await bot.send_photo(chat_id=userID, photo=a[3], caption="<b>" + a[0] + "</b>\n" + a[1] + "\n" + "Цена в рублях: " + str(a[2]) + "\n" + "ID - " + str(identifier), parse_mode="HTML")
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_unloader_tour(identifier, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT tour_name, description, price, tour_pic FROM tour WHERE tour_name= '{identifier}'")
            card = c.fetchall()
            a = card[0]
            await bot.send_photo(chat_id=userID, photo=a[3], caption="<b>" + a[0] + "</b>\n" + a[1] + "\n" + "Цена в рублях: " + str(a[2]) + "\n" + "ID - " + str(identifier), parse_mode="HTML")
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_unloader_product(identifier, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT product_name, description, price, product_pic FROM product WHERE product_name= '{identifier}'")
            card = c.fetchall()
            a = card[0]
            await bot.send_photo(chat_id=userID, photo=a[3], caption="<b>" + a[0] + "</b>\n" + a[1] + "\n" + "Цена в рублях: " + str(a[2]) + "\n" + "ID - " + str(identifier), parse_mode="HTML")
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_course_student(data):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name = data['name']
        surname = data['surname']
        patronymic = data['patronymic']
        course = data['course']
        contact_account = data['contact_account']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO course_student (second_name, first_name, otchestvo, id_course, contact_account) VALUES ('{surname}', '{name}', '{patronymic}', '{course}', '{contact_account}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_buyer_of_goods(data):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name = data['name']
        surname = data['surname']
        patronymic = data['patronymic']
        product = data['product']
        address = data['address']
        contact_account = data['contact_account']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO buyer_of_goods (second_name, first_name, otchestvo, contact_account, id_product, delivery_address) VALUES ('{surname}', '{name}', '{patronymic}', '{contact_account}', '{product}', '{address}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_service_buyer(data):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name = data['name']
        surname = data['surname']
        patronymic = data['patronymic']
        service = data['service']
        contact_account = data['contact_account']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO service_buyer (second_name, first_name, otchestvo, id_service, contact_account) VALUES ('{surname}', '{name}', '{patronymic}', '{service}', '{contact_account}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_tour_visitor(data):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name = data['name']
        surname = data['surname']
        patronymic = data['patronymic']
        tour = data['tour']
        contact_account = data['contact_account']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO tour_visitor (second_name, first_name, otchestvo, id_tour, contact_account) VALUES ('{surname}', '{name}', '{patronymic}', '{tour}', '{contact_account}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def get_admin_access(user_id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT tg_id_admin FROM admini;")
            results = c.fetchall()
            for result in results:
                if user_id == result[0]:
                    return True
            return False

    finally:
        c.close()

async def db_loader_admin(data):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name = data['name']
        second_name = data['second_name']
        contact_account = data['contact_account']
        tg_id_admin = data['tg_id_admin']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO admini (first_name_admin, second_name_admin, contact_account, tg_id_admin) VALUES ('{name}', '{second_name}', '{contact_account}', '{tg_id_admin}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_loader_mentor(data):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name = data['name']
        second_name = data['second_name']
        contact_account = data['contact_account']
        tg_id_mentor = data['tg_id_mentor']

        with connection.cursor() as c:
            c.execute(f"INSERT INTO mentors (first_name_mentor, second_name_mentor, contact_account_mentor, tg_id_mentor) VALUES ('{name}', '{second_name}', '{contact_account}', '{tg_id_mentor}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_mentor(id_mentor, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT EXISTS("
          f"SELECT 1 FROM tour WHERE id_mentor = '{id_mentor}' "
          f"UNION "
          f"SELECT 1 FROM courses WHERE id_mentor = '{id_mentor}' "
          f"UNION "
          f"SELECT 1 FROM product WHERE id_mentor = '{id_mentor}' "
          f"UNION "
          f"SELECT 1 FROM services WHERE id_mentor = '{id_mentor}'"
          f")")
            has_references = c.fetchone()[0]
            if has_references:
                await bot.send_message(chat_id=userID, text="Нельзя удалить ментора, пока он ведёт деятельность")

            else:
                c.execute(f"DELETE FROM courses WHERE id_course = '{id_mentor}'")
                await bot.send_message(chat_id=userID, text="Ментор удалён")



        with connection.cursor() as c:
            c.execute(f"DELETE FROM mentors WHERE id_mentor = '{id_mentor}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()


async def db_delete_admin(id_admin, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT COUNT(*) FROM admini")
            count = c.fetchone()[0]
            if count == 1:
                await bot.send_message(chat_id=userID, text="Нельзя удалить запись, так как она является единственной")
            else:
                c.execute(f"DELETE FROM admini WHERE id_admin = '{id_admin}'")
                await bot.send_message(chat_id=userID, text="Администратор удалён")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_all_cuses(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT courses_name, id_course FROM courses")
            results = c.fetchall()
            rows = [f"{courses_name} {id_course}" for courses_name, id_course in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_course (id_course, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT EXISTS(SELECT 1 FROM course_student WHERE id_course = '{id_course}')")
            has_references = c.fetchone()[0]
            if has_references:
                await bot.send_message(chat_id=userID, text="Нельзя удалить курс, пока есть студенты, проходящие его")

            else:
                c.execute(f"DELETE FROM courses WHERE id_course = '{id_course}'")
                await bot.send_message(chat_id=userID, text="Курс удалён")


        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_all_product(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT product_name, id_product FROM product")
            results = c.fetchall()
            rows = [f"{product_name} {id_product}" for product_name, id_product in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_product (id_product, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT EXISTS(SELECT 1 FROM buyer_of_goods WHERE id_product = '{id_product}')")
            has_references = c.fetchone()[0]
            if has_references:
                await bot.send_message(chat_id=userID, text="Нельзя удалить товар, пока на него оформлены заказы")

            else:
                c.execute(f"DELETE FROM product WHERE id_product = '{id_product}'")
                await bot.send_message(chat_id=userID, text="Товар удалён")


        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_all_service(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT services_name, id_service FROM services")
            results = c.fetchall()
            rows = [f"{services_name} {id_service}" for services_name, id_service in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_service(id_service, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT EXISTS(SELECT 1 FROM service_buyer WHERE id_service = '{id_service}')")
            has_references = c.fetchone()[0]
            if has_references:
                await bot.send_message(chat_id=userID, text="Нельзя удалить услугу, пока на неё записаны клиенты")

            else:
                c.execute(f"DELETE FROM services WHERE id_service = '{id_service}'")
                await bot.send_message(chat_id=userID, text="Услуга удалена")


        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_all_tour(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT tour_name, id_tour FROM tour")
            results = c.fetchall()
            rows = [f"{tour_name} {id_tour}" for tour_name, id_tour in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_tour(id_tour, userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"SELECT EXISTS(SELECT 1 FROM tour_visitor WHERE id_tour = '{id_tour}')")
            has_references = c.fetchone()[0]
            if has_references:
                await bot.send_message(chat_id=userID, text="Нельзя удалить ретрит, пока на него есть запись")

            else:
                c.execute(f"DELETE FROM tour WHERE id_tour = '{id_tour}'")
                await bot.send_message(chat_id=userID, text="Ретрит удалён")


        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()
async def get_mentor_access(user_id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT tg_id_mentor FROM mentors;")
            results = c.fetchall()
            for result in results:
                if user_id == result[0]:
                    return True
            return False

    finally:
        c.close()

async def db_view_tour(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT contact_account, second_name, first_name, otchestvo, id_tour, id_tour_visitor FROM tour_visitor")
            results = c.fetchall()
            rows = [f"•Пользователь {contact_account} {second_name} {first_name} {otchestvo} записан на тур {id_tour} " \
                    f"id клиента-{id_tour_visitor} " for
                    contact_account, second_name, first_name, otchestvo, id_tour, id_tour_visitor, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_view_product(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT contact_account, second_name, first_name, otchestvo, id_product, delivery_address, "
                      "id_buyer_of_goods FROM buyer_of_goods")
            results = c.fetchall()
            rows = [f"•Пользователь {contact_account} {second_name} {first_name} {otchestvo} оформил заказ на товар '{id_product}' " \
                    f" на адрес {delivery_address} id клиента-{id_buyer_of_goods} " for
                    contact_account, second_name, first_name, otchestvo, id_product, delivery_address, id_buyer_of_goods, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_view_course(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT contact_account, second_name, first_name, otchestvo, id_course, id_course_student FROM course_student")
            results = c.fetchall()
            rows = [f"•Пользователь {contact_account} {second_name} {first_name} {otchestvo} записан на курс {id_course} " \
                    f"id клиента-{id_course_student} " for
                    contact_account, second_name, first_name, otchestvo, id_course, id_course_student, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_view_services(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT contact_account, second_name, first_name, otchestvo, id_service, id_service_buyer FROM service_buyer")
            results = c.fetchall()
            rows = [f"•Пользователь {contact_account} {second_name} {first_name} {otchestvo} записан на {id_service} " \
                    f"id клиента-{id_service_buyer} " for
                    contact_account, second_name, first_name, otchestvo, id_service, id_service_buyer, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_record_tour(id_user_tour):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM tour_visitor WHERE id_tour_visitor = '{id_user_tour}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()


async def db_delete_record_service(id_service_buyer):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM service_buyer WHERE id_service_buyer = '{id_service_buyer}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()


async def db_delete_record_products(id_products_buyer):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM buyer_of_goods WHERE id_buyer_of_goods = '{id_products_buyer}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()


async def db_delete_record_courses(id_course_student):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM course_student WHERE id_course_student = '{id_course_student}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()


async def db_view_types_tour(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT name_of_tour, id_tour_type FROM tour_type")
            results = c.fetchall()
            rows = [f"•Тип тура - {name_of_tour} id {id_tour_type}" for
                    name_of_tour, id_tour_type, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_view_types_product(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT name_of_product, id_product_type FROM product_type")
            results = c.fetchall()
            rows = [f"•Тип товара - {name_of_product} id {id_product_type}" for
                    name_of_product, id_product_type, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()
async def db_view_types_service(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT name_of_service, id_service_type FROM service_type")
            results = c.fetchall()
            rows = [f"•Тип услуги - {name_of_service} id {id_service_type}" for
                    name_of_service, id_service_type, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_view_types_course(userID):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute("SELECT name_of_course, id_course_type FROM course_type")
            results = c.fetchall()
            rows = [f"•Тип курса - {name_of_course} id {id_course_type}" for
                    name_of_course, id_course_type, in results]

            text = "\n".join(rows)

        await bot.send_message(chat_id=userID, text=text)
        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_add_new_type_tour(name_of_course):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name_of_tour = name_of_course


        with connection.cursor() as c:
            c.execute(f"INSERT INTO tour_type (name_of_tour) VALUES ('{name_of_tour}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_add_new_type_product(name_of_product):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name_of_product = name_of_product


        with connection.cursor() as c:
            c.execute(f"INSERT INTO product_type (name_of_product) VALUES ('{name_of_product}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_add_new_type_service(name_of_service):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name_of_service = name_of_service


        with connection.cursor() as c:
            c.execute(f"INSERT INTO service_type (name_of_service) VALUES ('{name_of_service}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_add_new_type_course(name_of_course):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        name_of_course = name_of_course


        with connection.cursor() as c:
            c.execute(f"INSERT INTO course_type (name_of_course) VALUES ('{name_of_course}')")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_type_courses(id_courses_type):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM course_type WHERE id_course_type = '{id_courses_type}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()
async def db_delete_type_product(id_product_type):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM product_type WHERE id_product_type = '{id_product_type}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()
async def db_delete_type_service(id_service_type):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM service_type WHERE id_service_type = '{id_service_type}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()

async def db_delete_type_tour(id_tour_type):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as c:
            c.execute(f"DELETE FROM tour_type WHERE id_tour_type = '{id_tour_type}'")

        connection.commit()

    except Exception as e:
      print(e)

    finally:
        c.close()