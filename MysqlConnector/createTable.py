import mysql.connector

myconn=mysql.connector.connect(host="localhost", user="root", passwd="Siva@9866$",database="ordersdb")

print(myconn)

mycursor=myconn.cursor()

mycursor.execute("CREATE TABLE orders (id INT(10) PRIMARY KEY, orderName VARCHAR(32), orderCost VARCHAR(32), orderedBy VARCHAR(32))")

# data is stored in cursor object.
for i in mycursor:
    print(i)

