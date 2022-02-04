from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/new')
def new_student():
   return render_template('member.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      print("POST")
      try:
         name = request.form['name']
         userid = request.form['userid']
         password = request.form['password']

         print(name,userid, password)
         sql='INSERT INTO members (name,userid,password) VALUES ("{}" , "{}", "{}");'.format(name,userid,password)
         print(sql)
         with sqlite3.connect("members.db") as con:
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
            msg = "Record  added " +sql
      except:
         con.rollback()
         msg = "error in insert " + sql
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sqlite3.connect("members.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from members;")
   
   rows = cur.fetchall();
   print(rows)
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
  app.secret_key = 'secRET4566'
  app.run(host='0.0.0.0',port=8000)
