import json
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql

from tools.logging import logger

def handle_request():
    logger.debug("View Cart Handle Request")

    username = request.args.get('username')

    cursor = g.db.cursor()

    cursor.execute(sql.SQL("SELECT books.book_name, books.book_price " +
                           "FROM users, books, shoppingcart " +
                           "WHERE users.user_id = shoppingcart.user_id " +
                           "AND books.book_id = shoppingcart.book_id " +
                           "AND users.username = %s;"), (username,))

    record = cursor.fetchall()

    if record is not None:
        columns = cursor.description
        booklist = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]
        cursor.close()
        return json_response(token = create_token( g.jwt_data ), usercart = True)
    
    return json_response(token = create_token( g.jwt_data), usercart = False) #return false if user has not books in cart