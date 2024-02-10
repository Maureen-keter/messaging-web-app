from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    _tablename_ = 'users'