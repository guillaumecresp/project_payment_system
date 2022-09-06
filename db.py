import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE test(User_id, lastname, firstname, service, amount)")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)
cur.execute("""
    INSERT INTO test VALUES
        ('1', "poutine", 'vald', 'reparer isolation', '50€'),
        ('2', "poutine", 'kashimir', 'reparer gaz', '130€')
""")
con.commit()
res = cur.execute("SELECT amount FROM test")
print(res.fetchall())
data = [
    ("3", "simpson", 'homer', 'reparer maison', '10€'),
    ("4", "simpson", 'lisa', 'reparer voiture', '20€'),
    ("5", "simpson", 'bart', 'reparer ordinateur', '30€'),
]
cur.executemany("INSERT INTO test VALUES(?, ?, ?, ?, ?)", data)
con.commit()