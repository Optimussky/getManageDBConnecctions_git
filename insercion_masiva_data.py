# insercion_masiva_data.py
from mysql.connector import Error
import mysql.connector
from random_data import data


#print([data for x in data])
#print(data)

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'D354rr0ll0f4t1g4',
        db = 'python_inserciones_masivas'
    )


    if connection.is_connected():
        cursor = connection.cursor()
        data = data[0]
        cursor.executemany("""INSERT INTO person (id, name, company, job, email, phone, mac_address) 
                                VALUES(%s, %s, %s, %s, %s, %s, %s)""", data)
        if (len(data) == cursor.rowcount):
            connection.commit()
            print("{} rows inserted.".format(len(data)))
        else:
            connection.rollback()
except Error as ex:
    print("Error during connection: {}".format(ex))
finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed.")