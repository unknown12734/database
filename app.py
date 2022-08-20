from flask import Flask,render_template,request,redirect,url_for,flash
##import sqlite3 as sql
import psycopg2
import os

app=Flask(__name__)

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

@app.route("/index")
def index():
    con = psycopg2.connect(database=database, user=username ,password=password, host=host, port= port)
    cur=con.cursor()
    cur.execute("select * from users")
    data=cur.fetchall()
    print(data)
    return render_template("index.html",datas=data)

@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        con = psycopg2.connect(database=database, user=username, password=password, host=host, port= port)
        cur=con.cursor()
        cur.execute("insert into users(UNAME,CONTACT) values (%s,%s)",(uname,contact))
        con.commit()
        flash('User Added','success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:uid>",methods=['POST','GET'])
def edit_user(uid):
    if request.method=='POST':
        print(uid)
        uname=request.form['uname']
        contact=request.form['contact']
        con = psycopg2.connect(database=database, user=username, password=password, host=host, port= port)
        cur=con.cursor()
        cur.execute("update users set UNAME=%s,CONTACT=%s where UID=%s",(uname,contact,uid))
        con.commit()
        flash('User Updated',' success')
        return redirect(url_for("index"))
    con = psycopg2.connect(database=database, user=username, password=password host=host, port= port)
    ##con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where UID=%s",(uid,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)
    
@app.route("/delete_user/<string:uid>",methods=['GET'])
def delete_user(uid):
    con = psycopg2.connect(database=database, user=username, password=password, host=host, port= port)
    cur=con.cursor()
    print(uid)
    query = f"delete from users where UID = {int(uid)}"
    print(query)
    cur.execute(f"delete from users where UID={uid}")##,(uid,))
    con.commit()
    flash('User Deleted......','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(host="0.0.0.0")

