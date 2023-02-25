import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="root")

mycursor=con.cursor()

mycursor.execute("use college")

qry="select * from student"

mycursor.execute(qry)

mydata=mycursor.fetchall()

for i in mydata:
    print(i)

con.close()

