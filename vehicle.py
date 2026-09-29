#define a class to perform database operations on vehicle table create a class named VehicleListCreateRetrieveUpdateDelete
#with methods()  list() create() retrieve() delete() update()
import mysql.connector



class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='aiswarya',host='localhost',database='vehicle_db')
        self.c=self.con.cursor()

    def list(self):
        query='select * from vehicle'
        self.c.execute(query)
        record=self.c.fetchall()
        if record:
            for row in record:
                print(row)
        else:
            print('no record found')

    def create(self,brand,model,type,price,year):
        query='insert into vehicle (brand,model,type,price,year) values(%s,%s,%s,%s,%s)'
        data=(brand,model,type,price,year)
        self.c.execute(query,data)
        self.con.commit()
        print('data inserted successfully')

    def retrieve(self,id):
        query='select * from vehicle where id=%s'
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            print(record)
        else:
            print('no record found')

    def delete(self,id):
        query='delete from vehicle where id=%s'
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print('data deleted')
        else:
            print('no record found')

    def update(self,brand,model,type,price,year,id):
        query='update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s'
        data=(brand,model,type,price,year,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print('data updated')
        else:
            print('no record found')

vehicle_db=VehicleListCreateRetrieveUpdateDelete()
vehicle_db.list()
vehicle_db.create('Toyota','RAV4','SUV','35-42Lakh','2025')
vehicle_db.retrieve(2)
vehicle_db.delete(1)
vehicle_db.update('ghj','lko','thy','15-17 Lakh',2026,2)