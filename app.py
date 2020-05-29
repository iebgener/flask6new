#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api
from security import authenticate, identity
from flask_jwt import JWT
from resources.user import UserRegister
from resources.items import Item, Items
from resources.store import Store, Stores
from db import db
from models.user import UserModel
from models.items import ItemModel
from models.store import StoreModel

if __name__ == "__main__":
    app = Flask(__name__)
    app.secret_key = "abra kadabra"
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.before_first_request
    def create_table():
        db.create_all()
        db.session.add(StoreModel('BestStore'))
        db.session.add(UserModel("bob","asdf"))
        db.session.add(ItemModel("table","13.02","1"))
        db.session.commit()

    api = Api(app)

    jwt = JWT(app, authenticate, identity)  # /auth

    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(Items, "/items")
    api.add_resource(UserRegister, "/register")
    api.add_resource(Store, "/store/<string:name>")
    api.add_resource(Stores, "/stores")
    db.init_app(app)
    app.run(port=5000, debug=True, host="0.0.0.0")
