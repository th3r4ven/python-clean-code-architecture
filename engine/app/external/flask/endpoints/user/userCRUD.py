from flask import jsonify, request

from engine.app.external.flask.endpoints import api
from engine.app.core.controllers.user.userController import UserController

user_use_case = UserController()


@api.route('/user', methods=['GET'])
def get_users():
    users = user_use_case.get_all_users()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])


@api.route('/user', methods=['POST'])
def create_user():
    data = request.json
    try:
        user = user_use_case.create_user(data["username"], data["email"], data["password"])
        return jsonify({"message": "User created", "id": user.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api.route('/user/<int:id>', methods=['GET'])
def get_user(user_id):
    user = user_use_case.get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "email": user.email})
    return jsonify({"error": "User not found"}), 404


@api.route('/user/<int:id>', methods=['PUT'])
def update_user(user_id):
    user = user_use_case.get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "email": user.email})
    return jsonify({"error": "User not found"}), 404


@api.route('/user/<int:id>', methods=['DELETE'])
def delete_user(user_id):
    if user_use_case.delete_user(user_id):
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404
