from flask import Blueprint

from normal.mongo import User

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    pass


@auth_api.route('/logout', methods=['POST'])
def logout():
    pass
