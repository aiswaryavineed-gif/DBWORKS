#to read
import mysql.connector
con=mysql.connector.connect(user='root',
                             password='aiswarya',
                             host='localhost',
                             database='school_db')
print(con)
c=con.cursor()
#read all records from table
query='select * from student'
c.execute(query)

records=c.fetchall()
if records:  #data
    for row in records:
        print(row)
else:
    print('no records found')

c.close()
con.close()