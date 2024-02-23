from flask import Flask, request, render_template
from flask_mailman import Mail, EmailMessage
from models import db
from flask_migrate import Migrate
from flask_restful import Api
from controllers.users import Users, UserByID

mail=Mail()

app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///messaging.db'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'maureenchelangat955@gmail.com'
app.config['MAIL_PASSWORD'] = 'otvacdbrljoiviir'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db.init_app(app)
migrate=Migrate(app, db)
api=Api(app)

                                  

mail.init_app(app)




@app.route('/')
def index ():
    msg=EmailMessage(
        "Subject",
        "Body of the Email",
        "maureenchelangat955@gmail.com",
        ["maureen.chelangat@student.moringaschool.com"]
    )
    msg.send()
    return "Sent email..."

api.add_resource(Users,'/users')
api.add_resource(UserByID,'/users/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)

