from logging import log
from tools.logging import logger
from tools.token_tools import create_token
from flask import request, g
from flask_json import json_response
from psycopg2 import sql

import jwt

def handle_request():
    logger.debug("Get Friends Request")

    #Take in user token and friend username, query db for username, 
    #and get edges 

    print(g.graph.Edges())

    tempSet = set()
    
    currentuser = g.jwt_data['sub']
    print(currentuser)

    cursor = g.db.cursor()
    cursor.execute(sql.SQL("SELECT * FROM users WHERE username = %s;"), (currentuser, ))

    for idx, pair in enumerate(g.graph.Edges()):
        if currentuser in pair:
            for idx, edge in enumerate(pair):
                print(edge)
                tempSet.add(edge)

    logger.debug(tempSet)

    tempSet.remove(currentuser)

    logger.debug(tempSet)

    return json_response(friends = tempSet)



