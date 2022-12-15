from flask import Flask,request
from flask import render_template
from flask import request # 追加忘れ、要Merge時追加
from flask import redirect
from flask import session
import sqlite3
import datetime

app = Flask(__name__)

# トップページ（ひろせ担当）
@app.route('/')
def test_index():
    dt_now = datetime.datetime.now()
    str_today = dt_now.strftime("%Y/%m/%d")
    # print(str_today)
    conn = sqlite3.connect('bk.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM space_list WHERE space_date = ?;", (str_today,))
    spaces = cur.fetchall()
    conn.close()
    # print(spaces)
    return render_template('index.html', spaces=spaces)

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

    createAt=datetime.date.today().strftime("%Y/%m/%d")

    conn =sqlite3.connect("bk.db")

    c=conn.cursor()
    c.execute("INSERT INTO space_list values(null,?,?,?,?,?,?,?,0,?)",(py_space,py_date,py_start_time,py_end_time,py_capacity,py_price,py_memo,createAt))
    conn.commit()
    c.close()
    return redirect("/index")


# 一覧・検索機能（Takkaさん担当）
<<<<<<< HEAD
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
=======
@app.route('/search')
def search():
    dt_now = datetime.datetime.now()
    str_today = dt_now.strftime("%Y/%m/%d")
    str_date = request.args.get("date", default=str_today, type=str)
    int_time = request.args.get("time", default=10, type=int)
    conn = sqlite3.connect('bk.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM space_list WHERE space_date = ? AND start_time <= ? AND end_time > ?;", (str_date,int_time,int_time))
    spaces = cur.fetchall()
    conn.close()
    # print(spaces)
    return render_template('search.html', spaces=spaces, date=str_date, time=int_time)
>>>>>>> 6e8f1f942fb13bccbccea06978c1c9ac9738d592


# メモ編集機能（あとむさん担当）
@app.route('/detail/<id>')
def detail_get(id):
    conn = sqlite3.connect('bk.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM space_list WHERE ID = ?;", (id,))
    space = cur.fetchone()
    conn.close()
    return render_template('detail.html', space=space)

@app.route('/detail/<id>', methods = ['POST'])
def detail_post(id):
    str_memo = request.form.get('memo')
    check = request.form.get('done')
    int_check = 0
    if check != None:
        int_check = 1
    conn = sqlite3.connect('bk.db')
    cur = conn.cursor()
    cur.execute("UPDATE space_list SET memo = ?, reserved = ? WHERE id = ?;", (str_memo, int_check, id))
    conn.commit()
    conn.close()
    return redirect('/search')

# エラーの表示（４０４エラー）
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

# サーバー立ち上げ
if __name__ == '__main__':
    app.debug = True
    app.run()