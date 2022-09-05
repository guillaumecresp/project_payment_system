import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE test(User, age, inscription_date)")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)
cur.execute("""
    INSERT INTO test VALUES
        ('Gerard Alvès', 45, '01-01-2014'),
        ('Cristiano Ronaldo', 25, '01-01-2014')
""")
con.commit()
res = cur.execute("SELECT inscription_date FROM test")
print(res.fetchall())
data = [
    ("Monty Burns", 54, '7-01-2014'),
    ("Homer Simpson", 35, '7-02-2014'),
    ("Dark Vador", 45, '7-03-2014'),
]

cur.execute("CREATE TABLE payment(payment_method, id, amount, date)")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)
cur.execute("""
    INSERT INTO payment VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()
res = cur.execute("SELECT score FROM payment")
print(res.fetchall())
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO test VALUES(?, ?, ?)", data)
cur.executemany("INSERT INTO test VALUES(?, ?, ?)", data)
con.commit()