import os
import mysql.connector

def isDirectory(path):
    return os.path.isdir(path)

def isFile(path):
    return os.path.isfile(path)

def getDirContent(path, paths):
    if(not path.endswith("/")): path = path + "/"
    if(paths == None): paths = []

    directory = os.listdir(path)
    for item in directory:
        full_path = path + item
        if(isDirectory(full_path)): 
            getDirContent(full_path, paths) 
        else: 
            paths.append(full_path)
    return paths

def executeSQLFiles(path):
    files = getDirContent(path, None)

    database = mysql.connector.connect(
            host="localhost",
            user="phpmyadmin",
            password="_Mementomori112",
            database="python_sql"
    )

    cursor = database.cursor()

    for item in files:
        if(item.endswith(".sql") and isFile(item)):
            sql_open = open(item, "r")
            sql_file = sql_open.read()

            if(not sql_file == ""):
                cursor.execute(sql_file)
                database.commit()
                print(item + ": Completed")

            sql_open.close()

    database.close()
    print("database closed")

path = input("enter the source directory: ")
executeSQLFiles(path)
