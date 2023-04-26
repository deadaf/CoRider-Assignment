from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from decouple import config

app = Flask(__name__)

# Set up the database connection
client = MongoClient(config("MONGO_URI"))
db = client["CoRider"]
users = db["users"]


# Routes for CRUD operations
@app.route("/users", methods=["GET"])
def get_all_users():
    users_list = [user for user in users.find()]
    users_list = [
        user.update({"_id": str(user["_id"])}) or user for user in users_list
    ]  # convert ObjectId to string
    return jsonify({"users": users_list})


@app.route("/users/<id>", methods=["GET"])
def get_user_by_id(id):
    print(id)
    user = users.find_one({"_id": ObjectId(id)})
    if user:
        user = user.update({"_id": str(user["_id"])}) or user
        return jsonify({"user": user})

    else:
        return jsonify({"error": "User not found"})


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
    }
    result = users.insert_one(new_user)
    return jsonify({"id": str(result.inserted_id)})


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    updated_user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
    }
    result = users.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
    if result.modified_count == 1:
        return jsonify({"message": "User updated"})
    else:
        return jsonify({"error": "User not found"})


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"error": "User not found"})


# Run the application
if __name__ == "__main__":
    app.run(debug=True, port=8001)
