import mysql.connector
con=mysql.connector.connect(user='root',
                             password='aiswarya',
                             host='localhost',
                             database='school_db')
print(con)
c=con.cursor()
query='update student set place=%s where roll_no=%s'
data=('tvm',101)
c.execute(query,data)
con.commit()

if c.rowcount>0:
    print('data is updated')
else:
    print('no record found')
c.close()
con.close()
