import mysql.connector

myconn=mysql.connector.connect(host='localhost', user='root', passwd='Siva@9866$')

print(myconn)

mycursor=myconn.cursor()

mycursor.execute("show databases")
# data is stored in cursor object.
for i in mycursor:
    print(i)

