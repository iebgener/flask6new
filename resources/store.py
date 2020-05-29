from flask_restful import Resource
from models.store import StoreModel
from flask_jwt import jwt_required

class Store(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        print(store)
        if store:
            return store.json()
        else:
            return {'mesage': 'Store not found'}, 404

    @jwt_required()
    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'mesage': 'Store already exists'}, 400
        else:
            store = Store(name)
            try:
                store.save_to_db()
                return store.json()
            except:
                return {'mesage': 'DB error'}, 500

    @jwt_required()
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
                return {'mesage': 'Store deleted'}
            except:
                return {'mesage': 'DB error'}, 500
        else:
            return {'mesage': 'Store not found'}, 404

class Stores(Resource):
    @jwt_required()
    def get(self):
        return {'stores': [store.json() for store in StoreModel.get_all()]}
