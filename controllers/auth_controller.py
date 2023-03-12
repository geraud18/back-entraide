import bcrypt
from models.user import Users
from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
import json
from bson import json_util


headers = dict()


class Register(Resource):
    def post(self):
        if not request.is_json:
            return json.loads(json_util.dumps({"msg": "Missing json in request"})), 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)

        users = Users()
        if users.find_user_by_email(email):
            return json.loads(json_util.dumps({"msg": "A user with that already exist"})), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        users.name = request.json.get('name', None)
        users.firstname = request.json.get('firstname', None)
        users.email = email
        users.password = hashed_password
        users.created = request.json.get('created', None)
        users.active = request.json.get('active', None)
        users.image = request.json.get('image', None)
        users.telephone = request.json.get('telephone', None)
        users.linkedin = request.json.get('linkedin', None)

        # users.save_user()

        return json.loads(json_util.dumps({"id": users.save_user()})), 201


class Login(Resource):
    def post(self):
        if not request.is_json:
            return json.loads(json_util.dumps({"msg": "Missing json in request"})), 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)

        users = Users()
        user_by_email = users.find_user_by_email(email)
        if user_by_email:
            if bcrypt.checkpw(password.encode('utf-8'), user_by_email['password']):
                # create access token
                access_token = create_access_token(identity=email)
                return jsonify(access_token=access_token)
            else:
                return json.loads(json_util.dumps({"msg": "Bad email or password"})), 401
        else:
            return json.loads(json_util.dumps({"msg": "Bad email or password"})), 401

