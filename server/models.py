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

    
    
    
   