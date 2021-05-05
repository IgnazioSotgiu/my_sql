import os
import pymysql

# get username from cloud9
username = os.getenv("C9_USER")

# connect to database

connection = pymysql.connect(host="localhost",
                            user=username,
                            password = "",
                            db = "Chinook")

try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;" 
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
