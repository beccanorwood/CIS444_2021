from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from psycopg2 import sql

from tools.logging import logger

def handle_request():
    logger.debug("Get Books Handle Request")

    cursor = g.db.cursor()
    cursor.execute("SELECT * FROM books")
    record = cursor.fetchall()

    columns  = cursor.description
    booklist = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]
    cursor.close()


    return json_response( token = create_token(  g.jwt_data ) , book = booklist)

