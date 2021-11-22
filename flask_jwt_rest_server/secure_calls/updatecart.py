import json
import re
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
import datetime
from tools.token_tools import create_token
from tools.logging import logger
from psycopg2 import sql 

def handle_request():
    logger.debug("Update Cart Request")

    username = request.args.get('username')

    cursor = g.db.cursor()

    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (username, ))
    userid = cursor.fetchone()[0]

    cursor.execute(sql.SQL("DELETE FROM shoppingcart WHERE user_id = %s;"), (userid, ))
    g.db.commit()
    cursor.close()

    return json_response(message = "Your shopping cart has been cleared!")
