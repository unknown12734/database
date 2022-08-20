#import sqlite3 as sql

#connect to SQLite
#con = sql.connect('db_web.db')

import psycopg2
import os


if 'RDS_DB_NAME' in os.environ:
    username=os.environ['RDS_USERNAME'],
    password=os.environ['RDS_PASSWORD'],
    host=os.environ['RDS_HOSTNAME'],
    port=os.environ['RDS_PORT'],
    database=os.environ['RDS_DB_NAME']
    con = psycopg2.connect(database=database, user=username ,password=password, host=host, port= port)
else:
    username='postgres',
    password='postgres',
    host='localhost',
    port='5432',
    database='priyanka'
    con = psycopg2.connect(database=database, user=str(username[0]), password=str(password[0]), host=str(host[0]), port= str(port[0]))

# #establishing the connection
# con = psycopg2.connect(database=database, user=username ,password=password, host=str(host[0]), port= str(port[0]))

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

