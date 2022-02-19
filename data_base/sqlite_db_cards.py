import sqlite3 as sq


def sql_start_cards():
    global base, cur
    base = sq.connect('cards.db')
    cur = base.cursor()
    if base:
        print('data base cards connect Ok!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS cards(card TEXT, img TEXT)')
    base.commit()


async def sql_add_command_card(name, foto):
    data = (name, foto)
    cur.execute('INSERT INTO cards VALUES (?,?)', data)
    base.commit()


