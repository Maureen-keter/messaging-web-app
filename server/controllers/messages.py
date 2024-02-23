from flask_restful import Resource, abort
from models import Message, db
from flask import make_response, jsonify, request

class Messages(Resource):
    def get(self):
        messages=[message.to_dict() for message in Message.query.all()]
        if messages:
            return make_response(jsonify(messages), 200)
        return make_response(jsonify({"message":"users not found"}))


                    
