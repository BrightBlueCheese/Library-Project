from flask_sqlalchemy import SQLAlchemy
import mysql.connector

conn = mysql.connector.connect(
    # host= 'localhost',
    host = "127.0.0.1",
    user = "root",
    passwd = "060600",
    db='elice_library'
)

cur = conn.cursor()
db = SQLAlchemy()
