from flask import abort, jsonify, make_response, request
from flask_restx import Namespace, Resource

from app.models import User as DbUser

users_namespace = Namespace("Users", description="Endpoint to manage users")


class Users(Resource):
    def get(self):
        """Get all USERS"""
        users = DbUser.query.all()
        return jsonify(users)

    @users_namespace.response(200, "success")
    @users_namespace.response(400, "duplicate_user")
    @users_namespace.response(400, "validation_error")
    def post(self):
        """
        Create USER with unique username
        Payload: {"username": "NewUser"}
        """
        payload = request.get_json()
        if not (username := payload.get("username")):
            abort(400, "validation_error")
        if DbUser.query.filter_by(username=username).first():
            abort(400, "duplicate_error")
        user = DbUser(username=username)
        user.create()
        return make_response(jsonify(user), 201)


@users_namespace.response(200, "success")
@users_namespace.response(400, "validation_error")
@users_namespace.response(404, "resource_not_found")
class User(Resource):
    def get(self, user_id):
        """Get USER by id"""
        user = DbUser.query.filter_by(id=user_id).first_or_404("resource_not_found")
        return jsonify(user)


users_namespace.add_resource(Users, "")
users_namespace.add_resource(User, "/<int:user_id>")
