from flask import jsonify, request
from flask_restful import Resource
from models import User


class UserResource(Resource):
    def get(self, id=None):
        if id:
            user = User.get_by_id(id)
            if user:
                return jsonify({"user": user})
            else:
                return jsonify({"error": "User not found"}), 404
        else:
            users_list = User.get_all()
            return jsonify({"users": users_list})

    def post(self):
        data = request.get_json()
        new_user_id = User.create(data)
        return jsonify({"id": new_user_id})

    def put(self, id):
        data = request.get_json()
        result = User.update(id, data)
        if result == 1:
            return jsonify({"message": "User updated"})
        else:
            return jsonify({"error": "User not found"}), 404

    def delete(self, id):
        result = User.delete(id)
        if result == 1:
            return jsonify({"message": "User deleted"})
        else:
            return jsonify({"error": "User not found"}), 404
