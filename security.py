from models.user import UserModel


def authenticate(username, password):
    user = UserModel.findByUsername(username)
    if user and user.password == password:
        return user


def identity(payload):
    print(payload)
    user_id = payload["identity"]
    return UserModel.findByID(user_id)
