from psycopg2 import connect
from config import *


def db_create():
    if db_exist():
        print(f'DB {DB_NAME} already exist...')
        return
    try:
        connection = connect(user=DB_USER, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f'CREATE DATABASE {DB_NAME}')
        cursor.close()
        connection.close()
        print(f'DB {DB_NAME} created...')
    except Exception as error:
        print(f'! {error}')

def db_exist():
    result = False
    try:
        conn = connect(database=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT)
        result = True
        conn.close()    
    except:
        result = False
    return result

if __name__ == "__main__":
    db_create()
