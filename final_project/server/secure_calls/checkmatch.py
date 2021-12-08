from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response
from psycopg2 import sql

def handle_request():
    logger.debug("Check Match Request")

    receivedData = request.get_json()

    direction = receivedData['direction']
    print("Direction: ", direction)

    return json_response(status_= 200, valid = True, message = "Success")