from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql

from tools.logging import logger

def handle_request():
    logger.debug("View Cart Handle Request")

    bookprices = []

    booksincart = request.args.get('incartbooks')

    cursor = g.db.cursor()

    for book in booksincart:
        cursor.execute(sql.SQL("SELECT * FROM books WHERE name = %s", (book,)))
        price = cursor.fetchone()[2]

        bookprices.append(price)

    cursor.close()

    return json_response(bookname = booksincart, bookprices = bookprices)
    