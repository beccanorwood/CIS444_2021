import psycopg2

#creates connection to the database
def get_db():
    return psycopg2.connect(host="localhost", dbname="books" , user="beccanorwood", password="norwoodforgood")

#specfic to this database instance connection
def get_db_instance():  
    db  = get_db()
    cur  = db.cursor( )

    return db, cur 


