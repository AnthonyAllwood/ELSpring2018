#!/usr/bin/python


from flask import Flask, render_template, jsonify, Response
import sqlite3
import json

app = Flask(__name__)

# get most recent temp
@app.route("/")
def index():
    db = sqlite3.connect('./ELSpring2018/code/03_blinker/log/assignment3.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tempFormat ORDER BY date_time DESC LIMIT 1")
    result = cursor.fetchone()
    print(result[2])
    temp = result[2]
    return render_template('./ELSpring2018/web/index.html', temp = temp)


# get the temp data from database
@app.route("/catch")
def data():
    db = sqlite3.connect('./ELSpring2018/code/03_blinker/log/assignment3.db')
    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("SELECT * FROM tempFormat")

    entry = cursor.fetchall()
    data = []
    for row in entry:
        data.append(list(row))

    return Response(json.dumps(data),  mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
