import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('users.db')
    cur = base.cursor()
    if base:
        print('data base connect Ok!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS users(name TEXT, userID TEXT PRIMARY KEY,balance INT,last_card TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()


async def sql_update_name(name, ID):
    data = (name, ID)
    cur.execute('UPDATE users set name = ? where userID = ?', data)
    base.commit()


async def sql_update_balance(balance, ID):
    data = (balance, ID)
    cur.execute('UPDATE users set balance = ? where userID = ?', data)
    base.commit()
