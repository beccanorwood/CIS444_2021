from tools.logging import logger
from tools.token_tools import create_token
from flask import json, request, g
from flask_json import json_response
from psycopg2 import sql

from random import seed
from random import randint 

from DAO import User

def handle_request():
    logger.debug("Join Room Request")

    #Receive friend selected info and create room code 
    #for both users, 

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

        cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (currentUser, ))
        curr_user = cursor.fetchone()
    
        curr_user_id = curr_user[0]
        friend_record_id = friend_record[0]

        logger.debug(friend_record)
        logger.debug(curr_user)

        value = randint(0, 50)

        print(value)

        cursor.execute(sql.SQL("UPDATE users SET room_code = %s WHERE id = %s;"), (value, curr_user_id, ))
        cursor.execute(sql.SQL("UPDATE users SET room_code = %s WHERE id = %s;"), (value, friend_record_id, ))

        cursor.execute(sql.SQL("UPDATE users SET invited = %s WHERE id = %s;"), ('TRUE', friend_record_id, ))

        g.db.commit()
        cursor.close()

        return json_response(status_=200, valid = True, message = "Creating private room")
    
