
import mysql.connector

# Create Connection
mydb = mysql.connector.connect(host="92.205.1.135", user="cabqari-admin", password="r(l&ksAFnn+f", database="cabqari_db")


# # create database
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE pydb")

# Display all databases
mycursor = mydb.cursor()

mycursor.execute('SHOW DATABASES')
print(type(mycursor))
for db in mycursor:
    print(db)

# print(mydb)