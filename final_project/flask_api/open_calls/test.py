from tools.logging import logger
from flask import request, g
from flask_json import json_response

def handle_request():
    logger.debug("Test Handle Request")

    cursor = g.db.cursor()
    cursor.execute("SELECT * FROM books")
    record = cursor.fetchall()

    columns  = cursor.description
    booklist = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]
    cursor.close()


    return json_response( book = booklist)