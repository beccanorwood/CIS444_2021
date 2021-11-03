from flask import Flask, render_template, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
import json
import datetime
import bcrypt
import re
import simplejson as json


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
BOOKSTORE_MEDIA = "DEV_A3" #A3 media files

JWT_SECRET = "Jesus saves, everyone else takes 2D12 damage"


global_db_con = get_db() #global database connection
listofBooksAdded = []

with open("secret", "r") as f:
    JWT_SECRET = f.read()


###################################################################################################
                                #Entry point of CIS444_A3
###################################################################################################

#entry point for 
@app.route('/') #endpoint
def index():
    return render_template('index.html', media = IMGS_URL[BOOKSTORE_MEDIA])

###################################################################################################
                                    #End of entry point#
###################################################################################################

###################################################################################################
                #Method to check users' state and either get info from signup or login
###################################################################################################
@app.route('/userState', methods=['POST'])
def checkCreds():

    user_state = request.form['state']
    username = request.form['username']
    password = request.form['password']
    
    if user_state == 'newuser':
        return signup(username, password)
    else:
        return login(username, password)

###################################################################################################
            #Signup endpoint to verify user input to DB & create JWT on success
###################################################################################################

@app.route('/signup', methods=['POST'])
def signup(name, pwd):
    
    cursor = global_db_con.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (name,)) #to check if username is available 
    salted_password = bcrypt.hashpw( bytes(pwd, 'utf-8'), bcrypt.gensalt(10)) #encrypt password 
    newuser = cursor.fetchone()

    if newuser is None:
        cursor.execute("INSERT into users (username, password) VALUES (%s, %s);", (name, salted_password.decode('utf-8'),)) 
        global_db_con.commit() #update db changes
        cursor.close() 
        user_jwt = JWT(name, pwd)
        return jsonify({'validJWT': True, 'message': user_jwt})
    else:
        cursor.close()
        return jsonify({'validJWT': False, 'message': 'Signup Error'})
   
###################################################################################################
                                    #End of signup endpoint
###################################################################################################

###################################################################################################
                    #Login endpoint to verify user credentials with DB
###################################################################################################

@app.route('/login', methods=['POST'])
def login(name, pwd):
    
    cursor = global_db_con.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (name,))
    record = cursor.fetchone()

    if record is None:
        cursor.close()
        return jsonify({'validJWT': False, 'message': 'Login Error'})
    else:
        #compare salted password from database from user's password 
        salted_password = record[2]
        cursor.close()
        
        #compare password from form with decoded password
        if (bcrypt.checkpw( bytes(pwd, 'utf-8'), salted_password.encode() )): 
            user_jwt = JWT(name, pwd)
            return jsonify({'validJWT': True, 'message': user_jwt})
        else:
            return jsonify({'validJWT': False, 'message': 'Login Error'})

###################################################################################################
                                    #Method that creates JWT
###################################################################################################

@app.route('/createToken', methods=['GET'])
def JWT(username, password):
    
    return jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, JWT_SECRET, algorithm="HS256")

###################################################################################################
                                    #End of JWT method
###################################################################################################

###################################################################################################
                                    #Verifies user JWT
###################################################################################################  

@app.route('/validToken', methods=['GET'])
def validToken():

    token = request.args.get('jwt')

    if not jwt.decode(token, JWT_SECRET, algorithms=["HS256"]): #user has valid token
        return jsonify({'validToken': False})
    else:
        return jsonify({'validToken': True})

###################################################################################################
                                    #Returns books from DB
###################################################################################################

@app.route('/populateBookList', methods=['GET'])
def populateBookList():
    
    cursor = global_db_con.cursor()
    cursor.execute("SELECT * FROM books")
    record = cursor.fetchall()

    columns = cursor.description #returns list of tuples where [0] for each is the column header
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in record]
    cursor.close()

    return jsonify({'Books': result})

###################################################################################################
                                    #End of populateBookList 
###################################################################################################

###################################################################################################

@app.route('/addtoCart', methods=['POST'])
def addtoCart():
    
    bookAdded = request.form['book']  
    token = request.form['jwt']
    bookAdded = re.sub(r"[\n\t]", "", bookAdded.strip())

    print("Book Added: " + bookAdded)


    if jwt.decode(token, JWT_SECRET, algorithms=["HS256"]):
        listofBooksAdded.append(bookAdded)
        print(listofBooksAdded)
        return ({'validJWT': True})
    else:
        return ({'validJWT': False});


###################################################################################################
                                #End of addtoCart endpoint
###################################################################################################

@app.route('/viewTotal', methods = ['GET'])
def viewTotal():
    
    bookPrices = []
    cursor = global_db_con.cursor()

    for book in listofBooksAdded:
        print(book)
        cursor.execute("SELECT * FROM books WHERE name = %s", (book,))

        bookInfo = cursor.fetchone()
        bookPrice = bookInfo[2]

        bookPrices.append(bookPrice)

    return jsonify({'total': sum(bookPrices)})

###################################################################################################
    #Method that verifies user JWT and updates DB if token is valid otherwise, returns False
###################################################################################################

@app.route('/purchaseBooks', methods=['GET'])
def getBooks():

    token = request.args.get('jwt')
    selectedBook = request.args.get('book')

    cursor = global_db_con.cursor()

    isTokenValid = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    username = isTokenValid['user']

    if (isTokenValid):
        #query username and password in database and select book to purchase 
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))

        userInfo = cursor.fetchone()
        userid = userInfo[0]

        cursor.execute("INSERT into purchased_books (user_id, book_id, purchase_time) VALUES (%s, %s, %s);", (userid, selectedBook, datetime.datetime.now(),))
        global_db_con.commit()
        cursor.close()
        return jsonify({'Book_Purchased': True})
    else:
        return jsonify({'Book_Purchased': False})

###################################################################################################
                                    #End of getBooks endpoint
###################################################################################################

###################################################################################################
                                    #Start of Contact endpoint
###################################################################################################

@app.route('/contact', methods=['POST'])
def contact():
    
    userFeedback= request.form['request']

    return jsonify({'message': "Thank you, we will get back to soon!"});
    

###################################################################################################
                                    #End of contact endpoint
###################################################################################################


###################################################################################################
                                    #End of Assignment 3
###################################################################################################

app.run(host='0.0.0.0', port=80)

