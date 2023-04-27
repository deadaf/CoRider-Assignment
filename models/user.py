from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client["CoRider"]
users = db["users"]

__all__ = ("User",)


class User:
    @staticmethod
    def get_all():
        users_list = [user for user in users.find()]
        users_list = [
            user.update({"_id": str(user["_id"])}) or user for user in users_list
        ]  # convert ObjectId to string
        return users_list

    @staticmethod
    def get_by_id(id):
        user = users.find_one({"_id": ObjectId(id)})
        if user:
            user = user.update({"_id": str(user["_id"])}) or user
        return user

    @staticmethod
    def create(data):
        new_user = {
            "name": data["name"],
            "email": data["email"],
            "password": data["password"],
        }
        result = users.insert_one(new_user)
        return str(result.inserted_id)

    @staticmethod
    def update(id, data):
        updated_user = {
            "name": data["name"],
            "email": data["email"],
            "password": data["password"],
        }
        result = users.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
        return result.modified_count

    @staticmethod
    def delete(id):
        result = users.delete_one({"_id": ObjectId(id)})
        return result.deleted_count
