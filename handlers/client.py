from random import random
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

# состояния
# состояния регистрации


class FSMReg(StatesGroup):
    name = State()
    userID = State()
    balance = State()
    last_card = State()

# состояния смены имени


class FSMName(StatesGroup):
    awaitName = State()
    userID = State()

# состояние для eagle or tails


class FSMEagle(StatesGroup):
    bid = State()
    ChoiceSide = State()


# состояние для kmz


class FSMKmz(StatesGroup):
    bid = State()
    ChoiceSide = State()



# хендлер для /start
# @dp.message_handler(commands=['start'], state = None)


async def start_command(message: types.Message, state=None):
    global ID
    global auf
    auf = False
    ID = message.from_user.id
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            auf = True
            await state.finish()
            await bot.send_message(message.from_user.id, "hello :one:" + row[0], reply_markup=kb.inline_kb_start)
            break

    if auf == False:
        await FSMReg.name.set()
        await bot.send_message(message.from_user.id, "привет, как тебя зовут?")


# @dp.message_handler(state=FSMReg.name)
async def get_name_id(message: types.Message, state=FSMReg.name):
    async with state.proxy() as data:
        data['name'] = message.text
        data['userID'] = message.from_user.id
        data['balance'] = 500
        data['last_card'] = '8D'
    await sqlite_db.sql_add_command(state)
    await state.finish()
    await bot.send_message(message.from_user.id, "Hello: " + data['name'], reply_markup=kb.inline_kb_start)


# callback для профиля
# @dp.callback_query_handler(lambda c: c.data == 'profile')
async def profile_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Профиль', reply_markup=kb.inline_kb_profile)


# callback для смены имени
# @dp.callback_query_handler(lambda c: c.data == 'name')


async def change_name(callback_query: types.CallbackQuery, state=None):
    await bot.send_message(callback_query.from_user.id, "Введите новое имя: ")

    @dp.message_handler()
    async def change_name(message: types.Message, state=FSMName.awaitName):
        async with state.proxy() as data:
            data['awaitName'] = message.text
            data['userID'] = message.from_user.id
        await sqlite_db.sql_update_name(data['awaitName'], data['userID'])
        await bot.send_message(message.from_user.id, "Ваше новое имя: " + data['awaitName'], reply_markup=kb.inline_kb_start)

# callback для показа баланса
# @dp.callback_query_handler(lambda c: c.data == 'balance')


async def balance_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    global ID
    ID = callback_query.from_user.id
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            await bot.send_message(callback_query.from_user.id, "your balance: " + str(row[2]))
            break


# callback для игр
# @dp.callback_query_handler(lambda c: c.data == 'games')


async def games_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'игры', reply_markup=kb.inline_kb_games)




# игра в stone paper
# @dp.callback_query_handler(lambda c: c.data == 'kmz')


async def kmz_button(callback_query: types.CallbackQuery, state=None):
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
    await FSMKmz.bid.set()
    await bot.send_message(callback_query.from_user.id, 'напишите размер ставки от 1 до ' + str(Ybalance))


# @dp.message_handler(state=FSMEagle.bid)
async def take_bid_kmz(message: types.Message, state=FSMKmz.bid):
    global Bid
    Bid = message.text
    if int(Bid) >= Ybalance:
        await bot.send_message(message.from_user.id, 'На вашем балансе недостаточно средств')
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'Выберите сторону на которую поставите', reply_markup=kb.inline_kb_kmz)
        await state.finish()


# @dp.callback_query_handler(lambda c: c.data == 'rock')
async def rock_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = random.choice(['r', 's', 'p'])
        if side == 's':
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'поздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        elif side == 'r':
            await bot.send_message(callback_query.from_user.id, 'Ничья, у обоих кмень\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'к сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')

# @dp.callback_query_handler(lambda c: c.data == 'paper')


async def paper_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = random.choice(['r', 's', 'p'])
        if side == 'r':
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'поздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        elif side == 'p':
            await bot.send_message(callback_query.from_user.id, 'Ничья, у обоих бумага\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'к сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')

# @dp.callback_query_handler(lambda c: c.data == 'rock')


async def scissors_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = random.choice(['r', 's', 'p'])
        if side == 'p':
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'поздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        elif side == 'r':
            await bot.send_message(callback_query.from_user.id, 'Ничья, у обоих ножницы\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'к сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')


# игра в орел и решка
# @dp.callback_query_handler(lambda c: c.data == 'eagleOrtails')


async def eagle_buttonOr(callback_query: types.CallbackQuery, state=None):
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
    await FSMEagle.bid.set()
    await bot.send_message(callback_query.from_user.id, 'напишите размер ставки от 1 до ' + str(Ybalance))


# @dp.message_handler(state=FSMEagle.bid)
async def take_bid_eagle(message: types.Message, state=FSMEagle.bid):
    global Bid
    Bid = message.text
    if int(Bid) >= Ybalance:
        await bot.send_message(message.from_user.id, 'На вашем балансе недостаточно средств')
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'Выберите сторону на которую поставите', reply_markup=kb.inline_kb_egle_tails)
        await state.finish()
# @dp.callback_query_handler(lambda c: c.data == 'eagle')


async def eagle_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = random.choice(['e', 't'])
        if side == 'e':
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'поздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'к сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')


# @dp.callback_query_handler(lambda c: c.data == 'tails')


async def tails_button(callback_query: types.CallbackQuery, state=FSMEagle.ChoiceSide):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = random.choice(['e', 't'])
        if side == 't':
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'поздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'к сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')


# GAMES ROULETTE


# регистрация всех хендлеров
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'], state=None)
    dp.register_message_handler(get_name_id, state=FSMReg.name)
    dp.register_message_handler(change_name, state=FSMName.awaitName)
    dp.register_message_handler(take_bid_eagle, state=FSMEagle.bid)
    dp.register_message_handler(take_bid_kmz, state=FSMKmz.bid)
    
    dp.register_callback_query_handler(
        profile_button, lambda c: c.data == 'profile')
    dp.register_callback_query_handler(
        games_button, lambda c: c.data == 'games')
    dp.register_callback_query_handler(
        change_name, lambda c: c.data == 'name')
    dp.register_callback_query_handler(
        balance_button, lambda c: c.data == 'balance')
    dp.register_callback_query_handler(
        eagle_buttonOr, lambda c: c.data == 'eagleOr')
    dp.register_callback_query_handler(
        eagle_button, lambda c: c.data == 'eagle', state=None)
    dp.register_callback_query_handler(
        tails_button, lambda c: c.data == 'tails')
    dp.register_callback_query_handler(
        kmz_button, lambda c: c.data == 'kmz')
    dp.register_callback_query_handler(
        rock_button, lambda c: c.data == 'rock')
    dp.register_callback_query_handler(
        paper_button, lambda c: c.data == 'paper')
    dp.register_callback_query_handler(
        scissors_button, lambda c: c.data == 'scissors')

