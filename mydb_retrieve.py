# to retrieve one record details

import mysql.connector
con=mysql.connector.connect(user='root',password='aiswarya',host='localhost',database='school_db')
print(con)
c.cursor()