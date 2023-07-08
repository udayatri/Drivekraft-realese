import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling







def connect():
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='drivekraft',
                                         user='root',
                                         password='root')

    #connection_object = connection_pool.get_connection()
    return connection

def disconnect(connection_object,cursor):
    if(connection_object.is_connected()):
        cursor.close()
        connection_object.close()    