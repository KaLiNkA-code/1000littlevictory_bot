from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
""" async: Если в исполнении какой либо функции получился участок времени, когда ничего не используется,
он позволяет в эти промежутки исполнять что то другое"""
storage = MemoryStorage()
# Получение токена
token = os.getenv("TOKEN")

bot = Bot('5344331741:AAGcoV0EKRr4e6kueBXBx0v30utT0vRfolo')
dp = Dispatcher(bot, storage=storage)  # Инициализируем диспачер
