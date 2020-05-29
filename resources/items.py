from models.items import ItemModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This filed cannot be blank"
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every items needs astore id"
    )
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        else:
            return {'message': 'item not found'}, 404

    @jwt_required()
    def post(self, name):
        # check if item exists
        item = ItemModel.find_by_name(name)
        if item:
            return {"message": "Item already exists"}, 401

        data = Item.parser.parse_args()

        if not data:
            return {"message": "Input not JSON format"}, 400

        item = ItemModel(name, data['price'], data['store_id'])
        item.save_to_db()
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {'message': 'Item not found'}, 404
        item.delete_from_db()
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        item.save_to_db()


class Items(Resource):
    @jwt_required()
    def get(self):
        items = ItemModel.get_all()
        return {"items": list(map(lambda x: x.json(), items))}
        return {"items": [item.json() for item in items]}
