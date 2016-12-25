import sqlite3

def init_table_info():

    conn = sqlite3.connect('holdings.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE holdings
                   (code text, exchange text, volume real, price real)''')

    conn.commit()
    conn.close()

def insert_dummy_data():
    dummy_data = [
        ('CBA', 'ASX', 100, 80),
        ('WOW', 'ASX', 200, 20),
        ('IRE', 'ASX', 300, 10),
    ]

    conn = sqlite3.connect('holdings.db')
    cur = conn.cursor()

    cur.executemany('''INSERT INTO holdings VALUES (?,?,?,?)''', dummy_data)

    conn.commit()
    conn.close()


def get_table_info():
    table = {
        'title': 'Holding details',
    }

    conn = sqlite3.connect('holdings.db')
    cur = conn.cursor()

    data = []
    rows = cur.execute('''SELECT * FROM holdings''')
    conn.commit()
    conn.close()

    for row in rows:
        data.append(dict(zip(('code', 'exchange', 'volume', 'price'), *row)))

    table['data'] = data
    return table