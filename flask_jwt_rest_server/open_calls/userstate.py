from logging import log
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from tools.logging import logger
from open_calls.signup import signup_request
from open_calls.login import login_request

def handle_request():
    logger.debug("User State Handle Request")

    user_state = request.form['state']
    username = request.form['username']
    password = request.form['password']

    if user_state == 'newuser':
        return signup_request(username, password)
    else:
        return login_request(username, password)