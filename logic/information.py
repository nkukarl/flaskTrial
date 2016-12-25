import sqlite3

def init_table_info():

    conn = sqlite3.connect('holdings.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE stocks
                   (id INTEGER PRIMARY KEY , code TEXT, exchange TEXT, volume REAL, price REAL)''')

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

    cur.executemany('''INSERT INTO stocks VALUES (?, ?, ?, ?)''', dummy_data)

    conn.commit()
    conn.close()


def get_table_info():
    table = {
        'title': 'Holding details',
    }

    conn = sqlite3.connect('holdings.db')
    cur = conn.cursor()

    data = []
    rows = cur.execute('''SELECT * FROM stocks''')

    for row in rows:
        data.append(dict(zip(['id', 'code', 'exchange', 'volume', 'price'], row)))

    conn.close()

    table['data'] = data
    return table

def remove_holding(id):
    conn = sqlite3.connect('holdings.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM stocks where id=?''', (id,))

    conn.commit()
    conn.close()