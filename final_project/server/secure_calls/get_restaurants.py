from werkzeug.utils import redirect
from tools.logging import logger
from tools.token_tools import create_token
from flask import json, request, g
from flask_json import json_response


def handle_request():
    logger.debug("Get Restaurants Handle Request")

    name, url = ''

    imgs = [
        {
            name: "BJ's Restaurant and Brewhouse",
            url:  "https://idunno-images.s3.amazonaws.com/idunno_restaurants/BJsRestaurant_450x450.jpeg"
        },
        {
            name: 'Chick-fil-A',
            url: "https://idunno-images.s3.amazonaws.com/idunno_restaurants/Chick_fil_A_450x450.jpg"
        },
        {
            name: "Denny's",
            url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/Dennys_450x450.jpg'
        },
        {
            name: 'Jack in the Box',
            url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/JackintheBox_450x450.jpg'
        },
        {
            name: "McDonalds",
            url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/McDonalds_450x450.jpg'
        },
        {
            name: "P.F. Changs",
            url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/P.F._Chang_450x450.jpg'
        },
        {
            name: 'Panda Express',
            url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/Panda_Express_450x450.png'
        },
        {
            name: 'Red Lobster',
            url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/RedLobster_450x450.jpg'
        },
        {
            name: 'The Cheesecake Factory',
            url: 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/TheCheesecakeFactory_450x450.jpg'
        },
        {
            name: "Wendy's",
            url:  'https://idunno-images.s3.amazonaws.com/idunno_restaurants/Wendys_450x450.jpg'
        }

    ]

    return json_response(restaurants = imgs)

    #test_url = 'https://idunno-images.s3.amazonaws.com/idunno_restaurants/'

    #return test_url

    #logger.debug("Test Handle Request")

    #cursor = g.db.cursor()
    #cursor.execute("SELECT * FROM restaurants")
    #record = cursor.fetchall()

    #columns  = cursor.description
    #restaurantlist = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]
    #cursor.close()


    #return json_response( token = create_token( g.jwt_data), restaurants = restaurantlist)