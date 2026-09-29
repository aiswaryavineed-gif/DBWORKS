import mysql.connector
#establish connection between mysql server and python code

# con=mysql.connector.connect(user='root',password='aiswarya',host='localhost')
# #it returns connection object
# print(con)
#
# #cursor object to execute queries
# c=con.cursor()

# query="create database school_db"
# c.execute(query)
# print("Database file created")
# c.close()
# con.close()

con=mysql.connector.connect(user='root',
                             password='aiswarya',
                             host='localhost',
                             database='school_db')
# c=con.cursor()
#
# create table
# query="""create table student(
#         roll_no  int not null primary key,
#         name varchar(20),
#         age int,
#         place varchar(20),
#         phone varchar(20),
#         total_mark int)""";
# c.execute(query)
# print("table created")

#create new record/insert data
c=con.cursor()
query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
data=(101,'arun',12,'ekm','7023456788',150)

c.execute(query,data)
con.commit()             # to save the data permanently in db as chances for insertion,updation or deletion occurs
print('inserted data successfully')
c.close()
con.close()


