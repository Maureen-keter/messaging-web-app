from flask_restful import Resource, Api, abort
from flask import request, jsonify, make_response
from models import User, db


class Users(Resource):
    def get(self):
        users=User.query.all()
        if users:
            users_list=[user.to_dict() for user in users]
            return make_response(jsonify(users_list), 200)
        return make_response(jsonify({"error":"users not found"}), 404)
    
            


