#import sqlite3 as sql

#connect to SQLite
#con = sql.connect('db_web.db')

import psycopg2

#establishing the connection
con = psycopg2.connect(
   database="priyanka", user='postgres', password='postgres', host='3.108.220.38', port= '5432'
)

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ='''CREATE TABLE users (
	UID	SERIAL PRIMARY KEY,
	UNAME	TEXT NOT NULL,
	CONTACT	TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()
