import sqlite3
from models.user import UserModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field can't be "
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field can't be "
    )
    @jwt_required()
    def post(self):
        # extract info from request
        data = UserRegister.parser.parse_args()

        if UserModel.findByUsername(data['username']):
            return {'message': 'User already exists'}, 409
        # open database
        print(data)
        UserModel(data['username'], data['password']).save_to_db()
