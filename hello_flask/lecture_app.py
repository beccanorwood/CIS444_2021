from flask import Flask, render_template, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
import datetime

import datetime
import bcrypt


from db_con import get_db_instance, get_db

app = Flask(__name__)
FlaskJSON(app)

USER_PASSWORDS = { "cjardin": "strong password"}

IMGS_URL = {
            "DEV" : "/static",
            "INT" : "https://cis-444-fall-2021.s3.us-west-2.amazonaws.com/images",
            "PRD" : "http://d2cbuxq67vowa3.cloudfront.net/images",
            "DEV2": "/static/media"
            }

CUR_ENV = "PRD"
MY_MEDIA = "DEV2" #media files for assignment #2
JWT_SECRET = "who cares?"

global_db_con = get_db() #global database connection


with open("secret", "r") as f:
    JWT_SECRET = f.read()


@app.route('/') #endpoint
def index():
    return 'Web App with Python Caprice!' + USER_PASSWORDS['cjardin']

@app.route('/buy') #endpoint
def buy():
    return 'Buy'

@app.route('/hello') #endpoint
def hello():
    return render_template('hello.html',img_url=IMGS_URL[CUR_ENV] ) 

@app.route('/back',  methods=['GET']) #endpoint
def back():
    return render_template('backatu.html',input_from_browser=request.args.get('usay', default = "nothing", type = str) )

@app.route('/backp',  methods=['POST']) #endpoint
def backp():
    print(request.form)
    salted = bcrypt.hashpw( bytes(request.form['fname'],  'utf-8' ) , bcrypt.gensalt(10))
    print(salted)

    print(  bcrypt.checkpw(  bytes(request.form['fname'],  'utf-8' )  , salted ))

    return render_template('backatu.html',input_from_browser= str(request.form) )


#this endpoint is being called from 'firstpost.html' 
@app.route('/auth',  methods=['POST']) #endpoint
def auth():
        print(request.form)
        return json_response(data=request.form)



#Assigment 2
@app.route('/ss1') #endpoint
def ss1():
    return render_template('doggos.html', warning = "You asked for this", media = IMGS_URL[MY_MEDIA] );
##End of assignment 2 server side logic 


@app.route('/getTime') #endpoint
def get_time():
    return json_response(data={"password" : request.args.get('password'),
                                "class" : "cis44",
                                "serverTime":str(datetime.datetime.now())
                            }
                )

@app.route('/auth2') #endpoint that is displaying an encoded jwt 
def auth2():
    jwt_str = jwt.encode({"username" : "cary", "age" : "so young"} , JWT_SECRET, algorithm="HS256")
    #print(request.form['username'])
    return json_response(jwt=jwt_str)

@app.route('/exposejwt') #endpoint
def exposejwt():
    jwt_token = request.args.get('jwt')
    print(jwt_token)
    return json_response(output=jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"]))


@app.route('/hellodb') #endpoint
def hellodb():
    cur = global_db_con.cursor()
    cur.execute("select 5+5, 1+1");
    first,second = cur.fetchone()
    return json_response(a=first, b=second) #returns text displaying the query from execute statement by db cursor 

""" Assignment 3 begins 
""" 
""" Fullstack Application using encryption, psql, and jwt 
"""
"""
"""

###Beginning of Assignment 3 -> FullStack Bookstore Appliction 
@app.route('/neitherstone_norwood_books') #entry point of application
def bookstore():
    return render_template('bookstore.html', bookstore_name = "Neitherstone Norwood Books") 


#endpoint that will receive user input to sign in and will validate credentials by checking database 
@app.route('/signup', methods=["POST"])
def signup():
    
    username = request.form['username']
    password = request.form['password']

    cursor = global_db_con.cursor()

    print(username)
    print(password)
    cursor.execute("SELECT * FROM users WHERE name = %s", (username,)) #to check if username is available 
    salted_password = bcrypt.hashpw( bytes(password, 'utf-8'), bcrypt.gensalt(10)) #encrypt password 
    newuser = cursor.fetchone()

    if newuser is None:
        cursor.execute("INSERT into users (name, password) VALUES (%s, %s)", (username, salted_password)) #insert new user with encrypted password to db

    global_db_con.commit() #update db
    
    #jwt with an expiration time of 30 minutes 
    user_jwt = jwt.encode({"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, JWT_SECRET, algorithm="HS256")
    return json_response(jwt = user_jwt)



app.run(host='0.0.0.0', port=80)

