# first install mysql-connector-python package
import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

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