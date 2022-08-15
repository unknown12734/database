from flask import Flask,render_template,request,redirect,url_for,flash
##import sqlite3 as sql
import psycopg2

app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con = psycopg2.connect(database="postgres", user='postgres',password='password', host='database-1.cwehvtlrigrg.ap-south-1.rds.amazonaws.com', port= '5432')
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
        con = psycopg2.connect(database="postgres", user='postgres', password='password', host='database-1.cwehvtlrigrg.ap-south-1.rds.amazonaws.com', port= '5432')
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
        con = psycopg2.connect(database="postgres", user='postgres', password='password', host='database-1.cwehvtlrigrg.ap-south-1.rds.amazonaws.com', port= '5432')
        cur=con.cursor()
        cur.execute("update users set UNAME=%s,CONTACT=%s where UID=%s",(uname,contact,uid))
        con.commit()
        flash('User Updated',' success')
        return redirect(url_for("index"))
    con = psycopg2.connect(database="postgres", user='postgres', password='password', host='database-1.cwehvtlrigrg.ap-south-1.rds.amazonaws.com', port= '5432')
    ##con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where UID=%s",(uid,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)
    
@app.route("/delete_user/<string:uid>",methods=['GET'])
def delete_user(uid):
    con = psycopg2.connect(database="postgres", user='postgres', password='password', host='database-1.cwehvtlrigrg.ap-south-1.rds.amazonaws.com', port= '5432')
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
    app.run(debug=True)