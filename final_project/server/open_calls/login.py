from flask import request, g
import flask
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql

from tools.logging import logger

import bcrypt

def handle_request():
    logger.debug("Login Handle Request")

    test = request.get_json()

    username = test['username']
    password = test['password']


    print("Username: ", username)
    print("Password: ", password)

    token = {
           "sub": username
           }

    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (token['sub'],))
    record = cursor.fetchone()

    #Case for if user is not in database 
    if not record: 
        logger.debug("Username was not found in database")
        return json_response( status_ = 401, message = "Invalid Credentials", authenticated = False)

    else:
        salted_password = record[2]
        cursor.close()

        if (bcrypt.checkpw( bytes(password, 'utf-8'), salted_password.encode() )):

            invited = record[7]
            print(invited)

            if invited == True:
                return json_response( token = create_token(token), invited = True, authenticated = True)
            else:
                return json_response( token = create_token(token) , invited = False, authenticated = True)
        else:
            return json_response( status_ = 401, message = "Invalid password", authenticated = False)