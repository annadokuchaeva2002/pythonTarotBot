from aiogram.utils import executor
from create_bot import dp
import os
import data_base


async def on_startup(_):
    print('Бот онлайн')
    # data_base.sql_start()


import client, admin2, other, admin
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)