from flask import Flask, jsonify, abort, make_response, request
import sqlite3
import sys


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
    conn = sqlite3.connect('../../data/data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    users = cur.execute('SELECT * FROM User;').fetchall()

    return jsonify(users)

@app.route('/api/v1/resources/goods/all', methods=['GET'])
def api_all_goods():
    conn = sqlite3.connect('../../data/data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    users = cur.execute('SELECT * FROM Good;').fetchall()

    return jsonify(users)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/goods', methods=['GET'])
def api_get_goods_city():
    query_parameters = request.args

    ville = query_parameters.get('ville')

    query = "SELECT * FROM Good WHERE"
    to_filter = []

    if ville:
        query += ' ville=?'
        to_filter.append(ville)
    else:
        return page_not_found(404)

    conn = sqlite3.connect('../../data/data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    conn.close()
    return jsonify(results)

@app.route('/api/v1/resources/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    query_parameters = request.args

    nom = query_parameters.get('nom')
    prenom = query_parameters.get('prenom')
    birth = query_parameters.get('birth')

    conn = sqlite3.connect('../../data/data.db')
    cur = conn.cursor()
    #UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
    query = "UPDATE User SET "
    if nom:
        query += "nom = '" + nom + "',"
    if prenom:
        query += "prenom = '" + prenom + "',"
    if birth:
        query += "birth = '" + birth + "',"

    query = query[:-1] + " WHERE id = " + repr(user_id) + ";"
    print(query)
    cur.execute(query)
    conn.commit()

    user = cur.execute('SELECT * FROM User WHERE id = ' + repr(user_id) + ';').fetchall()
    conn.close()
    return jsonify(user)

@app.route('/api/v1/resources/goods/<int:good_id>', methods=['PUT'])
def update_good(good_id):
    query_parameters = request.args

    carac = query_parameters.get('carac')
    description = query_parameters.get('description')
    kind = query_parameters.get('kind')
    nom = query_parameters.get('nom')
    piece = query_parameters.get('piece')
    proprietaire = query_parameters.get('proprietaire')
    ville = query_parameters.get('ville')
    

    conn = sqlite3.connect('../../data/data.db')
    cur = conn.cursor()
    #UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
    query = "UPDATE Good SET "
    if nom:
        query += "nom = '" + nom + "',"
    if carac:
        query += "carac = '" + carac + "',"
    if description:
        query += "description = '" + description + "',"
    if kind:
        query += "kind = '" + kind + "',"
    if piece:
        query += "piece = '" + piece + "',"
    if proprietaire:
        query += "proprietaire = '" + proprietaire + "',"
    if ville:
        query += "ville = '" + ville + "',"

    query = query[:-1] + " WHERE id = " + repr(good_id) + ";"
    print(query)
    cur.execute(query)
    conn.commit()

    user = cur.execute('SELECT * FROM Good WHERE id = ' + repr(good_id) + ';').fetchall()
    conn.close()
    return jsonify(user)

app.run()