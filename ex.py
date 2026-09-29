import mysql.connector
con=mysql.connector.connect(user='root',password='aiswarya',host='localhost',database='market')
c=con.cursor()
print('connection successful')
#read data
# query='select * from customer'
# c.execute(query)
# record=c.fetchall()
# if record:
#     for row in record:
#         print(row)
# else:
#         print('no record found')

   #update
# query='update customer set place= %s where customer_id=%s'
# data=('pta',1)
# c.execute(query,data)
# con.commit()
# if c.rowcount>0:
#     print('record updated')
# else:
#     print('no records found')

  #delete
# query='delete from customer where customer_id=%s'
# data=(3,)
# c.execute(query,data)
# con.commit()
# if c.rowcount>0:
#     print('record deleted')
# else:
#     print('no record found')

   #retrieve
query='select * from customer '
c.execute(query)
record=c.fetchone()
if record:
    print(record)
else:
    print('no record found')
