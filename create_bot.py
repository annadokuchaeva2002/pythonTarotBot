from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import const
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token=const.API_TOKEN)
dp = Dispatcher(bot, storage=storage)