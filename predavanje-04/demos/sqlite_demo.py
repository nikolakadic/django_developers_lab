# https://docs.python.org/3/library/sqlite3.html
# PL SQL, TRANSACT SQL
# Security
# SQL injection

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')

# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,100.0)")

t = (50.0,100.0,)

c.execute('SELECT * FROM stocks WHERE price>? and qty=?', t)

print(c.fetchone())

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

conn.commit()

conn.close()
