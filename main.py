from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_restful import Api
from controllers.user_controller import ListUsers
from controllers.user_controller import FindUser
from controllers.auth_controller import Login
from controllers.auth_controller import Register
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/entraide"
app.secret_key = 'entraide@2022'
app.config['JWT_TOKEN_LOCATION'] = ['headers']

jwt = JWTManager(app)

api = Api(app)

api.add_resource(Login, '/api/login/')
api.add_resource(Register, '/api/register/')
api.add_resource(ListUsers, '/api/users/')
api.add_resource(FindUser, '/api/user/<string:email>')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':

    app.run(debug=True)
