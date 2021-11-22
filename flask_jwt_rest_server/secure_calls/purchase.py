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
    logger.debug("Purchase Handle Request")

    username = request.args.get('username')

    #Query shopping cart table in db with user's id
    cursor = g.db.cursor()

    cursor.execute(sql.SQL("SELECT users.user_id , books.book_id " +
                           "FROM users, books, shoppingcart " +
                           "WHERE users.user_id = shoppingcart.user_id " +
                           "AND books.book_id = shoppingcart.book_id " +
                           "AND users.username = %s;"), (username,))

    record = cursor.fetchall()
    logger.debug(record)

    columns = cursor.description
    books = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]

    for book in books:
        userid = book['user_id']
        bookid = book['book_id']

        userboughtbook = purchasedBooks(userid, bookid)

        if userboughtbook:
            return json_response( token = create_token ( g.jwt_data ), purchased = False)
        else:
            cursor.execute(sql.SQL("INSERT into purchases (user_id, book_id, purchase_time) VALUES (%s, %s, %s);"), (userid, bookid, datetime.datetime.now(), ))
        
        g.db.commit()

    cursor.close()

    return json_response( token = create_token ( g.jwt_data ), purchased = True)


def purchasedBooks(userid, bookid):

    cursor = g.db.cursor()

    cursor.execute(sql.SQL("SELECT * FROM purchases WHERE user_id  = %s;"), (userid,))
    record = cursor.fetchall()

    for book in record:
        logger.debug(book)
        if bookid in book:
            logger.debug(bookid)
            logger.debug(book)
            return True

    return False

