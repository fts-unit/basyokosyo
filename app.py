from flask import Flask
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
@app.route("/create/")
def add_get():
    return render_template("add.html")

@app.route("/add",methods=["POST"])
def add_post():
    py_task = reguest.form.get("html_〇〇〇")
    conn =squlite3.connect(".db")
c=conn.cursor()
c.execute("INSERT INTO task values(null,?)",(py_task,))
conn.commit()
c.close()
return redirect("/index")


# 一覧・検索機能（Takkaさん担当）
@app.route("/list/")
def bk_list():
    #データベースつくってそこにアクセスする。


# メモ編集機能（あとむさん担当）



# エラーの表示（４０４エラー）
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

# サーバー立ち上げ
if __name__ == '__main__':
    app.debug = True
    app.run()