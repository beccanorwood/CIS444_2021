from werkzeug.utils import redirect
from hello_flask.lecture_app import IMGS_URL
from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response

def handle_request():

    test_url = 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/'

    return test_url

    #logger.debug("Test Handle Request")

    #cursor = g.db.cursor()
    #cursor.execute("SELECT * FROM restaurants")
    #record = cursor.fetchall()

    #columns  = cursor.description
    #restaurantlist = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]
    #cursor.close()


    #return json_response( token = create_token( g.jwt_data), restaurants = restaurantlist)