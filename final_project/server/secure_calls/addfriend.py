from werkzeug.utils import redirect
from hello_flask.lecture_app import IMGS_URL
from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response
from psycopg2 import sql

import random

def handle_request():
    logger.debug("Add Friend Request")

    #Receive username input and query database checking if that user exists
    #If so, send user a valid response, and add room code to both users in respective column of db

    receivedinfo = request.get_json()

    friend_username = receivedinfo['friendusername']

    #Query datbase and check if user is valid

    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (friend_username, ))
    record = cursor.fetchone()

    if not record: 
        logger.debug("User not in database")
        return json_response(status_=401, valid = False, message = "Invalid Username")
    else:
        randomCode = random.randrange(1,50)
        cursor.execute(sql.SQL("INSERT into users(room_code) VALUES (%d);", (randomCode, )))
        g.db.commit()


        return json_response(status_= 200, valid = True, message = "Creating private room")
    



