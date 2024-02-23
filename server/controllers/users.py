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
    def post(self):
        data=request.get_json()
        existing_user=User.query.filter_by(email=data['email']).first()
        if existing_user:
            abort(409, detail="User already exists")
        user=User(firstname=data['firstname'], lastname=data['lastname'], email=data['email'], password=data['password'], phone_no=data['phone_no'])
        try:
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify({"message":"user created successfully"}), 201)
        except Exception as e:
            return make_response(jsonify({"error":"error creating the user"}), 404)
            
