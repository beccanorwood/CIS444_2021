from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql

from tools.logging import logger

import bcrypt

def login_request(username, password):
    logger.debug("Login Handle Request")
    
    password_from_user_form = password
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

        if (bcrypt.checkpw( bytes(password_from_user_form, 'utf-8'), salted_password.encode() )):
            return json_response( token = create_token(token) , authenticated = True)
        else:
            return json_response( status_ = 401, message = "Invalid password", authenticated = False)