from flask import Flask
from models import db
from flask_migrate import Migrate

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///messaging.db'
db.init_app(app)
migrate=Migrate(app, db)


if __name__=="__main__":
    app.run(debug=True)
