from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response

from firebase_admin import credentials, initialize_app, storage

def handle_request():

    cred = credentials.Certificate("Z:\School\CSUSM\Fall_2021\CIS 444\cis444-finalproject-firebase-adminsdk-6ttdv-9a1722ca1f.json")
    myapp = initialize_app(cred, {'storageBucket': 'cis444-finalproject.appspot.com'})


    #logger.debug("Test Handle Request")

    #cursor = g.db.cursor()
    #cursor.execute("SELECT * FROM restaurants")
    #record = cursor.fetchall()

    #columns  = cursor.description
    #restaurantlist = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]
    #cursor.close()


    #return json_response( token = create_token( g.jwt_data), restaurants = restaurantlist)