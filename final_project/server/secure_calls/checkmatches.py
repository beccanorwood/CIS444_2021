import enum
from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response
from psycopg2 import sql

def handle_request():
    logger.debug("Check Matches Request")

    curruser = g.jwt_data['sub']

    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (curruser, ))

    record = cursor.fetchone()
    curruser_id = record[0]
    room_code = record[5]

    cursor.execute(sql.SQL("SELECT * FROM users WHERE room_code = %s AND username <> %s;"), (room_code, curruser, ))
    friend_record = cursor.fetchone()
    friend_id = friend_record[0]



    cursor.execute(sql.SQL('SELECT * FROM swiped_restaurants WHERE user_id = %s OR user_id = %s;'), (curruser_id, friend_id, ))
    result = cursor.fetchall()

    columns = cursor.description
    possiblematches = [{columns[index][0]:column for index, column in enumerate(value)} for value in result]

    print(possiblematches)


    userchoices = {}

    for idx, value in enumerate(possiblematches):
        print(idx, value)
        for key, val in value.items():
            print(key, val)
            if key == 'selected' and value[key] == True:
                print(value['restaurant_name'])
                if (value['restaurant_name'] not in userchoices): 
                    userchoices[value['restaurant_name']] = [value['user_id']]
                else:
                    userchoices[value['restaurant_name']].append(value['user_id'])
            

    print(userchoices)

    roommatches = []

    for key, value in userchoices.items():
        if len(value) == 2:
            roommatches.append(key)

    
    print(roommatches)


    if len(roommatches): 
        return json_response(token = create_token(g.jwt_data), message = True, matches = roommatches)

    return json_response(message = False)
