from flask import Flask,make_response ,jsonify
from flask_migrate import Migrate
from flask_restful import Api,Resource ,request, reqparse
from flask_cors import CORS
from flask_bcrypt import Bcrypt , generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import timedelta
from models import db, User
from resources.messages import Message_List, Message_by_id



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///branch.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.json.compact = False

migrations =Migrate(app ,db)

db.init_app(app)

api=Api(app)
CORS(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


