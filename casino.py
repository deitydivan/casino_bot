from turtle import delay
import random
from unicodedata import name
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import inline_keyboard as kb
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import logging
from keyboards import inline_key as kb
import time
from config import dp, bot
from data_base import sqlite_db
from data_base import sqlite_db_cards

from handlers import client, admin, other, client_roulette, client_hl


async def on_startup(_):
    print('bot online')
    sqlite_db.sql_start()
    sqlite_db_cards.sql_start_cards()

client.register_handlers_client(dp)
client_roulette.register_handlers_client_roulette(dp)
client_hl.register_handlers_client_hl(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
