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


class User_List(Resource):
    @jwt_required()
    def get(self):
        user_list = []
        for user in User.query.all():
            user_dict = user.to_dict()
            user_list.append(user_dict)

        response = make_response(
            jsonify(user_list),
            200,
        )
        return response
    
class User_by_id(Resource):
    @jwt_required()
    def get(self, id):
        user = User.query.filter_by(id = id).first()
        user_dict = user.to_dict()

        response = make_response(
            jsonify(user_dict),
            200,
        )
        return response
    
class User_Signup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="Firstname is required")
    parser.add_argument('last_name', required=True, help="Last_name is required")
    parser.add_argument('phone_number', required=True, help="Phone number is required")
    parser.add_argument('password', required=True, help="Password is required")

    def post(self):
        # Extract user information from the request
        data = User_Signup.parser.parse_args()
        new_user = User(**data)
        print(new_user.first_name)
        print(new_user.last_name)
        
        # Validate if phone and password are provided
        if not new_user.phone_number or not new_user.password:
            return {'message': 'Both phone and password are required'}, 400

        # Check if the phone number is already registered
        if User.query.filter_by(phone_number = new_user.phone_number).first():
            return {'message': 'Phone number already registered'}, 400

        new_user.password = generate_password_hash(new_user.password).decode('utf-8') 

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201


