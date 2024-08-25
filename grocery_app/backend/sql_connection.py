import mysql.connector
__cnx=None

def get_sql_connection():
    global __cnx
    __cnx=mysql.connector.connect(
        user="root", host="localhost",password="1234",database="gs"
    )
    return __cnx