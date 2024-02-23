from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db=SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String)
    lastname=db.Column(db.String)
    email=db.Column(db.String)
    password=db.Column(db.String)
    role=db.Column(db.String)
    id_no=db.Column(db.Integer, nullable=False, unique=True)
    phone_no=db.Column(db.Integer, nullable=False, unique=True)

    messages_sent=db.relationship('Message', backref="sender", foreign_keys="Message.sender_id")
    messages_received=db.relationship("Message", backref="receiver", foreign_keys="Message.receiver_id")   

class Message(db.Model, SerializerMixin):
    __tablename__="messages"
    id=db.Column(db.Integer, primary_key=True)
    message=db.Column(db.String)
    urgent=db.Column(db.Boolean)
    sent_at=db.Column(db.TIMESTAMP, default=datetime.utcnow)

    sender_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    receiver_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    
    
   