from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response
from psycopg2 import sql
from random import seed
from random import randint 

import jwt 


def handle_request():
    logger.debug("Add Friend Request")

    #Receive username input and query database checking if that user exists
    #If so, send user a valid response, and add room code to both users in respective column of db

    receivedinfo = request.get_json()

    friend_username = receivedinfo['friendusername']
    print("Friend Username:", friend_username)

    logger.debug("Token: ", g.jwt_data['sub'])
    currentUser = g.jwt_data['sub']

    print("Current User: ", currentUser)

    #Query datbase and check if user is valid
    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (friend_username, ))
    friend_record = cursor.fetchone()

    if not friend_record: 
        logger.debug("User not in database")
        return json_response(status_=401, valid = False, message = "Invalid Username")
    else:

        g.graph.addEdge({currentUser, friend_username})

        return json_response(status_= 200, valid = True, message = "Friend Successfully Added!")
    



