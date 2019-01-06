from flask import Flask, jsonify, abort, make_response, request
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def index():
    return "Hello world !"

@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all_users():
    conn = sqlite3.connect('../data/data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    users = cur.execute('SELECT * FROM Users;').fetchall()

    return jsonify(users)

@app.route('/api/v1/resources/goods/all', methods=['GET'])
def api_all_goods():
    conn = sqlite3.connect('../data/data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    users = cur.execute('SELECT * FROM Goods;').fetchall()

    return jsonify(users)

app.run()
#s