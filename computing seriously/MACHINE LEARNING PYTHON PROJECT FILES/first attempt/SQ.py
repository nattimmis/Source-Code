import sqlite3
conn = sqlite3.connect("testing.db")

c = conn.cursor()
c.execute("DROP TABLE item")
c.execute("""CREATE TABLE item (id int PRIMARY KEY NOT NULL, name test)""")
conn.commit()

conn.close()