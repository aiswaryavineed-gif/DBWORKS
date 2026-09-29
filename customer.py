import mysql.connector
class Customer():
     def __init__(self):
         self.con=mysql.connector.connect(user='root',password='aiswarya',host='localhost',database='market')
         self.c= self.con.cursor()
     def create(self,name,age,place):
         query='insert into customer ( name,age,place) values(%S,%s,%s)'
         data=(name,age,place)
         self.c.execute(query,data)
         self.con.commit()
         print('data inserted successfully')
