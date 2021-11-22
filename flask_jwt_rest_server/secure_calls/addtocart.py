import json
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
from tools.token_tools import create_token
from tools.logging import logger
from psycopg2 import sql 
import re

def handle_request():
    logger.debug("Add to Cart Handle Request")

    bookAdded = request.args.get('book')
    bookAdded = re.sub(r"[\n\t]", "", bookAdded.strip())
    username = request.args.get('username')

    #Add book and user_id to database 
    logger.debug("Book Added: " + bookAdded)
    logger.debug("Username: " + username)

    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (username,))
    userid = cursor.fetchone()[0]

    cursor.execute(sql.SQL("SELECT * FROM books WHERE book_name = %s;"), (bookAdded,))
    bookid = cursor.fetchone()[0]


    #Don't allow user to add a book they already have into their shopping cart 
    cursor.execute(sql.SQL("SELECT books.book_name " +
                           "FROM users, books, shoppingcart " +
                           "WHERE users.user_id = shoppingcart.user_id " +
                           "AND books.book_id = shoppingcart.book_id " +
                           "AND users.username = %s;"), (username,))

    result = cursor.fetchall()
 
    for book in result:
        if bookAdded in book:
            return json_response( token = create_token( g.jwt_data ), addedtoCart = False)

    cursor.execute(sql.SQL("INSERT INTO shoppingcart (user_id, book_id) VALUES (%s, %s);"), (userid, bookid)) 
    g.db.commit()
    cursor.close()

    return json_response( token = create_token( g.jwt_data ) , addedtoCart = True)
