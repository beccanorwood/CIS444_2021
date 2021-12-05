from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from tools.logging import logger
from psycopg2 import sql
import bcrypt

def signup_request(username, password):
    logger.debug("Signup Handle Request")

    test = request.get_json()

    username = test['username']
    password = test['password']

    print("Sign Up API Username: ", username)
    print("Sign Up API Password: ", password)

    user = {
            "sub": username
            }

    #query database and check that username does not exist already
    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (username,))
    salted_password = bcrypt.hashpw( bytes(password, 'utf-8'), bcrypt.gensalt(10))
    record = cursor.fetchone()

    if record is None:
        cursor.execute(sql.SQL("INSERT into users (username, password) VALUES (%s, %s);"), (username, salted_password.decode('utf-8'), ))
        g.db.commit()
        cursor.close()
        return json_response(token = create_token(user), authenticated = True)
    else:
        cursor.close()
        return json_response(status_ = 401, message = "Invalid Credentials", authenticated = False)