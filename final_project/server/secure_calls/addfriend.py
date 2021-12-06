from werkzeug.utils import redirect
from hello_flask.lecture_app import IMGS_URL
from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response


def handle_request():
    logger.debug("Add Friend Request")

    #Receive username input and query database checking if that user exists
    #If so, send user a valid response, and add room code to both users in respective column of db


