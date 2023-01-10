# setup virtual environment
# python -m venv lessons

# activate virtual environment
#lessons/scripts/activate

import mysql.connector 

# create connection
conn = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='lessons')
# print('Connected...')


# # create database
# conn._execute_query('CREATE DATABASE lessons')
# print('Database created successfully...')

# # create table
# conn._execute_query('CREATE TABLE users(id int primary key auto_increment, name varchar(200), email varchar(200), password varchar(200))')
# print('Table created successfully...')


# # insert data
# cursor = conn.cursor()
# cursor.execute("INSERT INTO users(id, name, email, password) VALUES(1, 'Badrudin', 'badrudin@gmail.com', '1234')")
# conn.commit()

# # update data
# cursor = conn.cursor()
# cursor.execute("update users set name='Badrudin Mohamed Ali' where id=1")
# conn.commit()

# delete data
cursor = conn.cursor()
cursor.execute("DELETE from users where id=1")
conn.commit()
print(cursor)


