#!/usr/bin/python


from flask import Flask, render_template, jsonify, Response
import sqlite3
import json

app = Flask(__name__)

# get most recent temp
@app.route("/")
def index():
    db = sqlite3.connect('./log/logPeople.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM logPeople")
    result = cursor.fetchone()
    print(result[2])
    return render_template('index.html')


# get the temp data from database
@app.route("/catch")
def data():
    db = sqlite3.connect('./log/logPeople.db')
    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("SELECT * FROM logPeople LIMIT 10") # Display last 10 results

    entry = cursor.fetchall()
    data = []
    for row in entry:
        data.append(list(row))

    return Response(json.dumps(data),  mimetype='application/json')

#Number of database results/entries
@app.route("/count")
def dbcount():
    db = sqlite3.connect('./log/logPeople.db')
    cursor = db.cursor()
    cursor.execute("SELECT count(*) from logPeople")
    count = cursor.fetchall()
    return Response(json.dumps({"data" : count[0][0]}), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
