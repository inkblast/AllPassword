import mysql.connector
from mysql.connector import Error
import hashpass
connection = None
try:
    connection = mysql.connector.connect(host='localhost',database='allpass',user='root',password='')
    if connection.is_connected():
        print("connected")

except Error as e:
    print(e)



def insertToDb(password,email,username,url,appname):
    if(connection.is_connected()):

        cursor =connection.cursor()
        query = f"insert into passwords (password,email,username,url,appname) values('{password}','{email}','{username}','{url}','{appname}')"
        try:
            cursor.execute(query)
            connection.commit()
            print(" succesfully Inserted!")
        except Error as e:
            connection.rollback()
            print(e)

        connection.close()


def selectFromDb(c,condition):

    if(connection.is_connected()):
        cursor = connection.cursor()


        if c==2:

            query = f"select url,appname from passwords where email='{condition}'"
            cursor.execute(query)
            records = cursor.fetchall()

            for row in records:
                print(f"Url: {row[0]}\nApp Name: {row[1]}")

        else:
            query = f"select password,email,username from passwords where appname='{condition}'"
            cursor.execute(query)
            records = cursor.fetchall()
            for row in records:
                print(f"Password: {row[0]}\nEmail: {row[1]}\nUser Name: {row[2]}")



        connection.close()



def checkKey(key):
    valid  = False
    if (connection.is_connected()):
        cursor = connection.cursor()

        query = "select password from users"

        cursor.execute(query)
        records = cursor.fetchall()
        print(key,records[0][0])
        if key in records[0]:
            valid = True


    connection.close()

    return valid


def insertKey(key):

    hashed = hashpass.hashPass(key)

    if(connection.is_connected()):
        cursor = connection.cursor()
        query = f"insert into users (password) values('{hashed.hexdigest()}')"

        try:
            cursor.execute(query)
            connection.commit()

        except Exception as e :
            print(e)
            connection.rollback()




    connection.close()