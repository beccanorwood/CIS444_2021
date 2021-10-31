from flask import Flask, render_template, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
import json
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
            "DEV2": "/static/media",
            "DEV_A3": "/static/media/HPBooks"
            }

CUR_ENV = "PRD"
MY_MEDIA = "DEV2" #media files for assignment #2
BOOKSTORE_MEDIA = "DEV_A3"

JWT_SECRET = "who cares?"

global_db_con = get_db() #global database connection


with open("secret", "r") as f:
    JWT_SECRET = f.read()

#entry point for login/signup page
@app.route('/') #endpoint
def index():
    return render_template('index.html', media = IMGS_URL[BOOKSTORE_MEDIA])

#endpoint that will receive user input to sign in and will validate credentials by checking database 
@app.route('/signup', methods=['POST'])
def signup():
    
    username = request.form['username']
    password = request.form['password']

    cursor = global_db_con.cursor()

    print(username)
    print(password)


    cursor.execute("SELECT * FROM users WHERE username = %s", (username,)) #to check if username is available 
    salted_password = bcrypt.hashpw( bytes(password, 'utf-8'), bcrypt.gensalt(10)) #encrypt password 
    newuser = cursor.fetchone()

    if newuser is None:
        cursor.execute("INSERT into users (username, password) VALUES (%s, %s);", (username, salted_password.decode('utf-8'),)) #insert new user with encrypted password to db
        global_db_con.commit() #update db
        cursor.close() 
        #jwt with an expiration time of 30 minutes 
        #user_jwt = jwt.encode({"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, JWT_SECRET, algorithm="HS256")
        user_jwt = jwt.encode({'user': username}, JWT_SECRET, algorithm="HS256")
        return jsonify({'validJWT': True, 'message': user_jwt})
    else:
        cursor.close()
        return jsonify({'validJWT': False, 'message': 'Username is already taken'})
   


@app.route('/login', methods=['GET'])
def login():
    #only validate JWT for user when they login since they will have valid one when they sign in?
    #save username & password from frontend and user those to retrieve token
    
    #decode jwt and compare to username and password in db
    cursor = global_db_con.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    record = cursor.fetchone()

    if record is None:
        return jsonify({'message': 'User not found'})
    else:
        #compare salted password from database from user's password 
        salted_password = record[1]
        #compare password from form with decoded password
        if (bcrypt.checkpw( bytes(password, 'utf-8'), salted_password.encode() )): 
            return jsonify({'message': 'valid pasword'})
        else:
            return jsonify({'message': 'invalid password'})




#enpoint that will be a POST to receive jwt for validation
#if valid, return json response from '/getBooks' endpoint
@app.route('/validToken', methods=['GET'])
def validToken():

    token = request.args.get('jwt')
    #json_data = request.json
    #token = json_data['jwt']
    
    print(token)

    if not jwt.decode(token, JWT_SECRET, algorithms=["HS256"]): #user has valid token
        return jsonify({'validToken': False})
    else:
        return jsonify({'validToken': True})



@app.route('/populateBookList', methods=['GET'])
def populateBookList():
    
    #query search in database and return all books
    #send to frontend without displaying them 
    #until user provides valid login information
    #and jwt token access

    cursor = global_db_con.cursor()
    cursor.execute("SELECT * FROM books")
    record = cursor.fetchall()

    columns = cursor.description #returns list of tuples where [0] for each is the column header
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]

    print(result)

    return jsonify({'Books': result})


#@app.route('/getBooks', methods=['GET'])
def getBooks():
    #method that requires valid jwt
    #compare decoded jwt with decoded password matching
    #send json object with username, password, and jwt
    #compare decoded with user's name
    #then compare user's password and if it's the same as the decoded password using bcrypt 

    cursor = global_db_con.cursor()

    return json_response(result = jwt.decode(user_jwt, JWT_SECRET, algorithms=['HS256']))

     #check database to confirm username from database matches password and decoded token matches username
    cursor.execute("SELECT * FROM users WHERE username = %", (username,))
    record = cursor.fetchone()
        
    username_db = record[0]

    if (username_db == token_username): #check for valid token
        return ({'message': "You may view the bookstore"})
    else:
        return ({'message': "Invalid JWT"});

    


app.run(host='0.0.0.0', port=80)

