from flask import Flask,request
from flask import render_template
from flask import redirect
from flask import session
import sqlite3
import datetime

app = Flask(__name__)

# トップページ（ひろせ担当）
@app.route('/')
def test_index():
    return render_template('index.html')

# 投稿機能（sasaさん担当）
@app.route("index.html")


# 一覧・検索機能（Takkaさん担当）
@app.route("/list/")
def bk_list():
    conn= sqlite3.connect("bk.db")
    c= conn.cursor()
    c.execute("SELECT * FROM space_list")
    bk_list_py= []
    for row in c.fetchall():
        bk_list_py.append({'ID':row[0],'name':row[1],'space_date':row[2],'start_time':row[3],'end_time':row[4],'capacity':row[5],'price':row[6],'memo':row[7],'reserved':row[8],'createAt':row[9]})
    c.close()
    # print(bk_list_py)
    return render_template("list.html",data= bk_list_py)

@app.route("/list/" ,methods= ["POST"])
def seek():
    book_date= request.form.get("date")
    book_time= request.form.get("time")
    conn= sqlite3.connect("bk.db")
    c= conn.cursor()
    c.execute("SELECT * FROM space_list WHERE space_date= ? AND start_time= ?",(book_date,book_time))
    seek_date= c.fetchall()
    conn.close()
    return render_template("list.html",date= seek_date)


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