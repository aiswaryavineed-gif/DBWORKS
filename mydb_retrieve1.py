  # to retrieve a record
import mysql.connector
con=mysql.connector.connect(user='root',
                             password='aiswarya',
                             host='localhost',
                             database='school_db')
print(con)
c=con.cursor()
query='select * from student where roll_no = %s'       # read specific data from db table
data=(101,)
c.execute(query,data)

records=c.fetchone()
if records:  #data
    print(records)
else:
    print('no records found')

c.close()
con.close()