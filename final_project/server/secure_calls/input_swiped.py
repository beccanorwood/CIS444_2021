from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response
from psycopg2 import sql

def handle_request():
    logger.debug("Check Match Request")

    receivedData = request.get_json()

    direction = receivedData['direction']
    print("Direction: ", direction)

    restaurantname = receivedData['restaurantname']
    print("Restaurant Name: ", restaurantname)

    print("Token: ", g.jwt_data['sub'])
    currentuser = g.jwt_data['sub']

    #Insert current user's swipe direction, then check corresponding user's directions
    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (currentuser, ))
    
    record = cursor.fetchone()
    curruser_id = record[0]
    selected = ''


    if direction == 'left': 
        selected = 'no'
    else: 
        selected = 'yes'


    cursor.execute(sql.SQL("INSERT into swiped_restaurants (user_id, restaurant_name, selected) VALUES (%s, %s, %s);"), (curruser_id, restaurantname, selected, ))
    g.db.commit()
    cursor.close()

    return json_response(status_= 200, valid = True, message = "Success")