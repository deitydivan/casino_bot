from email import message_from_string
from random import random
from telegram import InputFile
from config import dp, bot
from keyboards import inline_key as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
import sqlite3 as sq
import random
from data_base import sqlite_db_cards

last_card = '8D'


class FSMHL(StatesGroup):
    bid = State()
    ChoicePredict = State()


class FSMCards(StatesGroup):
    foto = State()
    name = State()


# @dp.callback_query_handler(lambda c: c.data == 'hl')
async def hl_button(callback_query: types.CallbackQuery, state=None):
    await bot.answer_callback_query(callback_query.id)
    global ID
    global Ybalance

    ID = callback_query.from_user.id
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    Bid = 0
    await FSMHL.bid.set()
    await bot.send_message(callback_query.from_user.id, 'напишите размер ставки от 1 до ' + str(Ybalance))

# @dp.message_handler(state=FSMHL.bid)


async def take_bid_hl(message: types.Message, state=FSMHL.bid):
    global Bid
    Bid = message.text
    if int(Bid) >= Ybalance:
        await bot.send_message(message.from_user.id, 'На вашем балансе недостаточно средств')
        await state.finish()
    else:
        photo = open('D:/myprog/casino/img/2h.png')
        await bot.send_message(message.from_user.id, 'Выберите на что хотите поставить', reply_markup=kb.inline_kb_hl)
        await bot.send_photo(message.from_user.id, photo)
        await state.finish()

# @dp.message_handler(commands=['test'], state = none)


async def test(message: types.Message):
    photo = open('D:/myprog/casino/img/2c.png', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


# @dp.message_handler(commands=['foto'], state = none)
async def start_foto(message: types.Message, state: FSMCards):
    await FSMCards.foto.set()
    await bot.send_message(message.from_user.id, 'your Foto')


# @dp.message_handler( state = FSMCards.name)
async def foto(message: types.Message, state: FSMCards):
    async with state.proxy() as data:
        data['foto'] = message.document.file_id
    await FSMCards.next()
    await bot.send_message(message.from_user.id, 'card name')


# @dp.message_handler( state = FSMCards.name)
async def foto_name(message: types.Message, state: FSMCards):
    async with state.proxy() as data:
        data['name'] = message.text
    print(state)
    await sqlite_db_cards.sql_add_command_card(data['name'], data['foto'])
    await state.finish()


def register_handlers_client_hl(dp: Dispatcher):
    dp.register_message_handler(take_bid_hl, state=FSMHL.bid)
    dp.register_message_handler(
        start_foto, commands=['foto'],  state=None)
    dp.register_message_handler(test, commands=['test'])
    dp.register_message_handler(
        foto, content_types=['document'],  state=FSMCards.foto)
    dp.register_message_handler(foto_name, state=FSMCards.name)
    dp.register_callback_query_handler(
        hl_button, lambda c: c.data == 'hl')
