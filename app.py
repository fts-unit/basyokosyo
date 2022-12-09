from flask import Flask
from flask import render_template
from flask import redirect,request
from flask import session
import sqlite3
import datetime

app = Flask(__name__)

# トップページ（ひろせ担当）
@app.route('/')
def test_index():
    return render_template('index.html')

# 投稿機能（sasaさん担当）
@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add",methods=["POST"])
def add_post():
    
    py_space = request.form.get("space")
    py_date = request.form.get("date")
    py_start_time = request.form.get("start_time")
    py_end_time = request.form.get("end_time")
    py_capacity = request.form.get("capacity")
    py_price = request.form.get("price")
    py_memo = request.form.get("memo")
    
    

    conn =sqlite3.connect("bk.db")

    c=conn.cursor()
    c.execute("INSERT INTO space_list values(null,?,?,?,?,?,?,?,0,null)",(py_space,py_date,py_start_time,py_end_time,py_capacity,py_price,py_memo))
    createAt1= datetime.date.today()
    createAt="{0:%y/%m/%d}".format(createAt1)
    conn.commit()
  

    c.close()
    return redirect("/index")


# 一覧・検索機能（Takkaさん担当）
# @app.route("/list/")
# def bk_list():
    #データベースつくってそこにアクセスする。


# メモ編集機能（あとむさん担当）
#tesut1


# エラーの表示（４０４エラー）
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

# サーバー立ち上げ
if __name__ == '__main__':
    app.debug = True
    app.run()