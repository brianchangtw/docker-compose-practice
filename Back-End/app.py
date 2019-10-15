from flask import Flask
from flask_cors import CORS

from normal.auth import auth_api

# Create a flask app
app = Flask(__name__)

# Regist flask blueprint
app.register_blueprint(auth_api, url_prefix='/auth')

@app.route('/')
def index():
	return 'Hi?'

CORS(app)
