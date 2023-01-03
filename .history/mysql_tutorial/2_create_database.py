import mysql.connector

mydb = mysql.connector.connect(host="localhost", user='root', password="")

# create database
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS PYDATABASE')