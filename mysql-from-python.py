import os
import datetime
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
        row = ("Bob", 21, "1990-02-06 23:25:02")
        sql = "SELECT * FROM Genre;" 
        cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
        connection.commit()
        
finally:
    connection.close()
