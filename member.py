import sqlite3

conn = sqlite3.connect('member.db')
print ("Opened database successfully")
sql="CREATE TABLE member (id INTEGER PRIMARY KEY AUTOINCREMENT, userid varchar(15),password varchar(15), name varchar(30));"

conn.execute(sql)
print ("Table created successfully")
conn.close()
