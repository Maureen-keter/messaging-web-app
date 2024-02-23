from flask_restful import Resource, abort
from models import Message, db
from flask import make_response, jsonify, request

class Messages(Resource):
    def get(self):
        messages=[message.to_dict() for message in Message.query.all()]
        if messages:
            return make_response(jsonify(messages), 200)
        return make_response(jsonify({"message":"users not found"}))
    def post(self):
        data=request.get_json()
        message=Message(message=data['message'], sent_at=data['sent_at'])
        try:
            db.session.add(message)
            db.session.commit()
            return make_response(jsonify({"message":"message created successfully"}), 201)
        except Exception as e:
            return make_response(jsonify({"Error":"error creating message"}), 404)
class MessageByID(Resource):
    def get(self, id):
        message=Message.query.filter_by(id=id).first().to_dict()
        if message:
            return make_response(jsonify(message), 200)
        return make_response(jsonify({"message":"message not found"}), 404)
    d