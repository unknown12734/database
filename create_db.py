#import sqlite3 as sql

#connect to SQLite
#con = sql.connect('db_web.db')

import psycopg2
import os

#establishing the connection
con = psycopg2.connect(
   database=os.environ['database'], 
   user=os.environ['user'], 
   password=os.environ['password'], 
   host=os.environ['host'], 
   port= os.environ['port']
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
