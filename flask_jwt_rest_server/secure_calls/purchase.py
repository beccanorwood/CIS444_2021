import json
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
from tools.token_tools import create_token
from tools.logging import logger
from psycopg2 import sql 

def handle_request():
    logger.debug("Purchase Handle Request")

    username = request.args.get('username')

    #Query shopping cart table in db with user's id
    cursor = g.db.cursor()
    #cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;", (username,)))

    #userid = cursor.fetchone()[0]

    cursor.execute(sql.SQL("SELECT books.book_id, users.user_id " +
                           "FROM users, books, shoppingcart " +
                           "WHERE users.user_id = shoppingcart.user_id " +
                           "AND books.book_id = shoppingcart.book_id " +
                           "AND users.username = %s;"), (username,))

    record = cursor.fetchall()
    logger.debug(record)

    return json_response(purchasecomplete = True)