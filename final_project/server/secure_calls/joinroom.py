from werkzeug.utils import redirect
from hello_flask.lecture_app import IMGS_URL
from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response

def handle_request():
    logger.debug("Join Room Request")

    #When user clicks on the join room, they will receive their room code from the column in the db