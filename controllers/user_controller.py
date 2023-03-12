from flask_jwt_extended import jwt_required
from models.user import Users
from flask_restful import Resource
from flask import jsonify
import json
from bson import json_util

users = Users()


class ListUsers(Resource):
    @jwt_required()
    def get(self):
        # return jsonify(users.all_user())
        return json.loads(json_util.dumps(users.all_user()))


class FindUser(Resource):
    @jwt_required
    def get(self, email):
        return jsonify(users.find_user_by_email(email))
        # return json.loads(json_util.dumps(users.find_user_by_email(email)))


