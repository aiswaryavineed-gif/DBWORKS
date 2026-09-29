import mysql.connector


class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con= mysql.connector.connect(user='root',password='aiswarya',host='localhost',database='library')
        self.c=self.con.cursor()

#this can be done in workbench insertion part
        # self.title=input('enter title')
        # self.author=input('enter author')
        # self.price=int(input('enter price'))
        # self.language=input('enter language')
        # self.pages=int(input('enter pages'))
        #
        # query='insert into book(title,author,price,language,pages) values(%s,%s,%s,%s,%s)'
        # data=(self.title,self.author,self.price,self.language,self.pages)
        # self.c.execute(query,data)
        # self.con.commit()

    def list(self):   #reading all records from table
        query='select * from book'
        self.c.execute(query)
        record= self.c.fetchall()
        if record:
            for row in record:
                print (row)
        else:
            print('no record found')

    def create(self,title,author,price,language,pages): #creating a new record
        query='insert into book ( title,author,price,language,pages) values(%s,%s,%s,%s,%s)'
        data=(title,author,price,language,pages)
        self.c.execute(query,data)
        self.c=self.con.cursor()
        self.con.commit()
        print('insert data successfully')

    def retrieve(self,id):
        query='select * from book where id=%s'
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            print(record)
        else:
            print('no record found')

    def delete(self,id):
        query='delete from book where id=%s'
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print('data deleted')
        else:
            print('no record found')

    def update(self,title,author,price,language,pages,id):
        query='update book set title=%s,author=%s,price=%s,language=%s,pages=%s where id=%s'
        data=(title,author,price,language,pages,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print('updated data successfully')
        else:
            print('no records found')
book_instance=BookListCreateRetrieveUpdateDelete()
book_instance.list()
#book_instance.create('ABC','john',300,'english',550)
book_instance.retrieve(2)
#book_instance.delete(3)
book_instance.update('jk','leiymor',200,'chineese',55,1)