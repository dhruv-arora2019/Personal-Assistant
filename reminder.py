#from virtual import speak
import mysql.connector
import os

def reminder ():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234")