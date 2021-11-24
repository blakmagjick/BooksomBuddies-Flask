from flask import Flask, jsonify

import models
from resources.users import users

from flask_login import LoginManager

import os
from dotenv import load_dotenv 
load_dotenv()

DEBUG=True
PORT=8000 

app = Flask(__name__) 

app.secret_key = os.environ.get('FLASK_APP_SECRET')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        user = models.User.get_by_id(user_id)
        return user
    except models.DoesNotExist:
        return None

app.register_blueprint(users, url_prefix='/users')

@app.route('/')
def test():
    return 'Server connected'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
