

import mysql.connector

conn = mysql.connector.connect(
    # host='localhost',
    host = "127.0.0.1",
    user='root',
    passwd='060600',
    )

cur = conn.cursor()

cur.execute('CREATE DATABASE if not exists elice_library') 
cur.execute("SHOW DATABASES")
for db in cur:
    print(db)

