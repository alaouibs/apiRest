from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../../data/data.db')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carac = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(120), unique=False)
    kind = db.Column(db.String(80), unique=False)
    nom = db.Column(db.String(80), unique=False)
    piece = db.Column(db.String(120), unique=False)
    proprietaire = db.Column(db.String(120), unique=False)
    ville = db.Column(db.String(120), unique=False)

    def __init__(self, carac, description, kind, nom, piece, proprietaire, ville):
        self.carac = carac
        self.description = description
        self.kind = kind
        self.nom = nom
        self.piece = piece
        self.proprietaire = proprietaire
        self.ville = ville


class GoodSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('carac', 'description', 'kind', 'nom', 'piece', 'proprietaire', 'ville')


good_schema = GoodSchema()
goods_schema = GoodSchema(many=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), unique=True)
    prenom = db.Column(db.String(120), unique=True)
    birth = db.Column(db.String(120), unique=True)

    def __init__(self, nom, prenom, birth):
        self.prenom = prenom
        self.nom = nom
        self.birth = birth


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('nom', 'prenom', 'birth')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# endpoint to show all users
@app.route("/api/v2/resources/users/all", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

# endpoint to show all users
@app.route("/api/v2/resources/goods/all", methods=["GET"])
def get_good():
    all_goods = Good.query.all()
    result = goods_schema.dump(all_goods)
    return jsonify(result.data)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# endpoint to update user
@app.route("/api/v2/resources/users/<id>", methods=["PUT"])
def user_update(id):
    query_parameters = request.args
    user = User.query.get(id)
    nom = query_parameters.get('nom')
    prenom = query_parameters.get('prenom')
    birth = query_parameters.get('birth')
    app.logger.warning('testing warning log')
    app.logger.info('testing info log')

    if nom:
        user.nom = nom
    if prenom:
        user.prenom = prenom
    if birth:
        user.birth = birth

    db.session.commit()
    return user_schema.jsonify(user)

# endpoint to update good
@app.route("/api/v2/resources/goods/<id>", methods=["PUT"])
def good_update(id):
    query_parameters = request.args
    good = Good.query.get(id)

    carac = query_parameters.get('carac')
    description = query_parameters.get('description')
    kind = query_parameters.get('kind')
    nom = query_parameters.get('nom')
    piece = query_parameters.get('piece')
    proprietaire = query_parameters.get('proprietaire')
    ville = query_parameters.get('ville')

    if carac:
        good.carac = carac
    if description:
        good.description = description
    if kind:
        good.kind = kind
    if nom:
        good.nom = nom
    if piece:
        good.piece = piece
    if proprietaire:
        good.proprietaire = proprietaire
    if ville:
        good.ville = ville

    db.session.commit()
    return good_schema.jsonify(good)

# endpoint to show all users
@app.route("/api/v2/resources/goods/<ville_>", methods=["GET"])
def get_good_city(ville_):
    all_goods = Good.query.filter_by(ville = ville_)
    result = goods_schema.dump(all_goods)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)