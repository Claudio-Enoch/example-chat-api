from flask import jsonify
from flask_restx import Namespace, Resource

from app.models import User as DbUser

users_namespace = Namespace("users", description="*** USER ENDPOINT DESCRIPTION ***")


class Users(Resource):
    def get(self):
        """
        - GET /users
          - {[username:, messages_received:, messages_authored]}
        """
        users = DbUser.query.all()
        return jsonify(users)

    def post(self):
        """
        - POST /users
          - {[username:]}  -> {[username:]}
        """
        return "POST /Users"


class User(Resource):
    def get(self, username):
        user = DbUser.query.filter_by(username=username).first_or_404("user_not_found")
        return jsonify(user)


users_namespace.add_resource(Users, "")
users_namespace.add_resource(User, "/<string:username>")
