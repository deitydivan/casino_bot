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


# состояние для roulette
class FSMRoulette(StatesGroup):
    bid = State()
    ChoiceSide = State()

#variable touple
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
red = (1,3,5,7,9,12,14,16,18,19,21,23,25,30,32,34,36)
green = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)


# игра в roulette
# @dp.callback_query_handler(lambda c: c.data == 'roulette')
async def roulette_button(callback_query: types.CallbackQuery, state=None):
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
    await FSMRoulette.bid.set()
    await bot.send_message(callback_query.from_user.id, 'напишите размер ставки от 1 до ' + str(Ybalance))


# @dp.message_handler(state=FSMEagle.bid)
async def take_bid_roullete(message: types.Message, state=FSMRoulette.bid):
    global Bid
    Bid = message.text
    if int(Bid) >= Ybalance:
        await bot.send_message(message.from_user.id, 'На вашем балансе недостаточно средств')
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'Выберите на что хотите поставить', reply_markup=kb.inline_kb_roulette_play)
        await state.finish()


# @dp.callback_query_handler(lambda c: c.data == 'zero')
async def zero_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 0:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')

# @dp.callback_query_handler(lambda c: c.data == 'one')


async def one_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 1:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def two_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 2:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def three_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 3:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def four_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 4:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def five_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 5:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def six_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 6:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def seven_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 7:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def eight_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 8:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def nine_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 9:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def ten_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 10:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def eleven_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 11:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twelve_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 12:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirteen_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 13:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def fourteen_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 14:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def fiveteen_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 15:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def sixteen_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 16:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def seventeen_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 17:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def eightteen_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 18:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def nineteen_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 19:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 20:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_one_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 21:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_two_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 22:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_three_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 23:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_four_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 24:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_five_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 19:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_six_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 26:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_seven_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 27:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_eight_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 28:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def twenty_nine_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 29:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirty_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 30:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirty_one_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 31:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirty_two_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 32:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirty_three_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 33:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirty_four_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 34:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirty_five_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side == 35:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def thirty_six_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side ==36:
            Ybalance += int(Bid) * 36
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def green_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side in green:
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def red_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side in red:
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def even_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side in even:
            Ybalance += int(Bid) 
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')
async def odd_button(callback_query: types.CallbackQuery):
    global Ybalance
    rec = sqlite_db.cur.execute('SELECT * FROM users').fetchall()
    for row in rec:
        if int(ID) == int(row[1]):
            Ybalance = int(row[2])
            break
    if Ybalance >= 0 and int(Bid) <= Ybalance:
        side = (random.randint(0, 36))
        if side in odd:
            Ybalance += int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nпоздравляю вы выиграли!!!\nВаш баланс: ' + str(Ybalance))
        else:
            Ybalance -= int(Bid)
            await sqlite_db.sql_update_balance(Ybalance, callback_query.from_user.id)
            await bot.send_message(callback_query.from_user.id, 'Выпало число: '+ str(side) + '\nк сожалению вы проиграли\nВаш баланс: ' + str(Ybalance))
    else:
        await bot.send_message(callback_query.from_user.id, 'на вашем балансе недостаточно средств')


def register_handlers_client_roulette(dp: Dispatcher):
    dp.register_message_handler(take_bid_roullete, state=FSMRoulette.bid)
    dp.register_callback_query_handler(
        roulette_button, lambda c: c.data == 'roulette')
    dp.register_callback_query_handler(
        zero_button, lambda c: c.data == 'zero')
    dp.register_callback_query_handler(one_button, lambda c: c.data == 'one')
    dp.register_callback_query_handler(two_button, lambda c: c.data == 'two')
    dp.register_callback_query_handler(three_button, lambda c: c.data == 'three')
    dp.register_callback_query_handler(four_button, lambda c: c.data == 'four')
    dp.register_callback_query_handler(five_button, lambda c: c.data == 'five')
    dp.register_callback_query_handler(six_button, lambda c: c.data == 'six')
    dp.register_callback_query_handler(seven_button, lambda c: c.data == 'seven')
    dp.register_callback_query_handler(eight_button, lambda c: c.data == 'eight')
    dp.register_callback_query_handler(nine_button, lambda c: c.data == 'nine')
    dp.register_callback_query_handler(ten_button, lambda c: c.data == 'ten')
    dp.register_callback_query_handler(eleven_button, lambda c: c.data == 'eleven')
    dp.register_callback_query_handler(twelve_button, lambda c: c.data == 'twelve')
    dp.register_callback_query_handler(thirteen_button, lambda c: c.data == 'thirteen')
    dp.register_callback_query_handler(fourteen_button, lambda c: c.data == 'fourteen')
    dp.register_callback_query_handler(fiveteen_button, lambda c: c.data == 'fiveteen')
    dp.register_callback_query_handler(sixteen_button, lambda c: c.data == 'sixteen')
    dp.register_callback_query_handler(seventeen_button, lambda c: c.data == 'seventeen')
    dp.register_callback_query_handler(eightteen_button, lambda c: c.data == 'eightteen')
    dp.register_callback_query_handler(nineteen_button, lambda c: c.data == 'nineteen')
    dp.register_callback_query_handler(twenty_button, lambda c: c.data == 'twenty')
    dp.register_callback_query_handler(twenty_one_button, lambda c: c.data == 'twenty_one')
    dp.register_callback_query_handler(twenty_two_button, lambda c: c.data == 'twenty_two')
    dp.register_callback_query_handler(twenty_three_button, lambda c: c.data == 'twenty_three')
    dp.register_callback_query_handler(twenty_four_button, lambda c: c.data == 'twenty_four')
    dp.register_callback_query_handler(twenty_five_button, lambda c: c.data == 'twenty_five')
    dp.register_callback_query_handler(twenty_six_button, lambda c: c.data == 'twenty_six')
    dp.register_callback_query_handler(twenty_seven_button, lambda c: c.data == 'twenty_seven')
    dp.register_callback_query_handler(twenty_eight_button, lambda c: c.data == 'twenty_eight')
    dp.register_callback_query_handler(twenty_nine_button, lambda c: c.data == 'twenty_nine')
    dp.register_callback_query_handler(thirty_button, lambda c: c.data == 'thirty')
    dp.register_callback_query_handler(thirty_one_button, lambda c: c.data == 'thirty_one')
    dp.register_callback_query_handler(thirty_two_button, lambda c: c.data == 'thirty_two')
    dp.register_callback_query_handler(thirty_three_button, lambda c: c.data == 'thirty_three')
    dp.register_callback_query_handler(thirty_four_button, lambda c: c.data == 'thirty_four')
    dp.register_callback_query_handler(thirty_five_button, lambda c: c.data == 'thirty_five')
    dp.register_callback_query_handler(thirty_six_button, lambda c: c.data == 'thirty_six')
    dp.register_callback_query_handler(even_button, lambda c: c.data == 'even')
    dp.register_callback_query_handler(odd_button, lambda c: c.data == 'odd')
    dp.register_callback_query_handler(red_button, lambda c: c.data == 'red_btn')
    dp.register_callback_query_handler(green_button, lambda c: c.data == 'green_btn')
