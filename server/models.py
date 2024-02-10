from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    _tablename_ = 'users'

    serialize_rules = ('-password',)
    
    id = db.Column(db.Integer,primary_key = True)
    first_name =db.Column(db.String,nullable = False)
    last_name  = db.Column (db.String,nullable = False)
    phone_number = db.Column(db.String,nullable = False ,unique=True)
    password = db.Column (db.VARCHAR ,nullable = False)
    profile_photo = db.Column (db.VARCHAR ,nullable = True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

    
    def _repr_(self):
        return {"id": self.id, 
                "first_name": self.first_name, 
                "last_name": self.last_name,
                "phone_number": self.phone_number
                }
    
    def check_password(self,plain_password):
        return check_password_hash(self.password,plain_password)
    
    