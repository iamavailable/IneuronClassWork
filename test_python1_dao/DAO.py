import mysql.connector
from mysql.connector import Error
import csv


class DBObject:
    def __init__(self, connUserName, connPassword, host, port, listOfColumns):
        self.conn = None
        try:
            # established DB connection
            self.conn = mysql.connector.connect(user=connUserName, password=connPassword, host=host, port=port)
            self.listOfColumns = listOfColumns
            print("Connection established with DB")
        except Error as e:
            print(e)
        # finally:
        #     if self.conn is not None and self.conn.is_connected():
        #         self.conn.close()

    def checkIfDatabaseExists(self, dbName):
        # cursor() method create a cursor object
        mycursor = self.conn.cursor()
        try:
            mycursor.execute("SHOW databases")  # Execute SQL Query to check all the existing databases
            result = mycursor.fetchall()
            for i in result:
                if dbName.strip() == i[0].strip():
                    print("{} DBname already exists".format(dbName))
                    return True
        except Error as e:
            print(e)
        # finally:
        #     if self.conn is not None and self.conn.is_connected():
        #         self.conn.close()
        return False

    def createDatabase(self, dbName):
        # cursor() method create a cursor object
        mycursor = self.conn.cursor()
        try:
            mycursor.execute(
                "CREATE DATABASE {}".format(dbName))  # Execute SQL Query to check all the existing databases
            print("Created the Database named as {}".format(dbName))
        except Error as e:
            print(e)
        # finally:
        #     if self.conn is not None and self.conn.is_connected():
        #         self.conn.close()

    def checkIfTableExists(self, dbName, tableName):
        # cursor() method create a cursor object
        mycursor = self.conn.cursor()
        try:
            mycursor.execute("USE {}".format(dbName))  # Execute SQL Query to check all the existing databases
            try:
                mycursor.execute("SHOW tables")
                result = mycursor.fetchall()
                for i in result:
                    if tableName.strip() == i[0].strip():
                        print("{} table already exist in the {} database".format(tableName, dbName))
                        return True
            except Error as e:
                print(e)
                return False

        except Error as e:
            print(e)
            return False
        # finally:
        #     if self.conn is not None and self.conn.is_connected():
        #         self.conn.close()

        return False

    def createTable(self, dbName, tableName):
        # cursor() method create a cursor object
        mycursor = self.conn.cursor()
        try:
            mycursor.execute("USE {}".format(dbName))  # Execute SQL Query to check all the existing databases
            try:
                mycursor.execute(
                    'CREATE TABLE ' + tableName + ' ( ' + self.listOfColumns[0] + ' TEXT,' + self.listOfColumns[1] +
                    ' TEXT,' + self.listOfColumns[2] + ' TEXT)')  # Execute SQL Query

                print("Created the table named as {} in {} database".format(tableName, dbName))
                return True
            except Error as e:
                print(e)
                return False
        except Error as e:
            print(e)
            return False
        # finally:
        #     if self.conn is not None and self.conn.is_connected():
        #         self.conn.close()

    # def insertDataInTable(self, dbName, query, records_to_insert):
    #
    #     try:
    #         mycursor = self.conn.cursor()
    #         mycursor.execute("USE {}".format(dbName))  # Execute SQL Query to check all the existing databases
    #         try:
    #             mycursor.executemany(query, records_to_insert)
    #             self.conn.commit()
    #             print("Values Inserted")
    #             return True
    #         except Error as e:
    #             print(e)
    #             return False
    #     except Error as e:
    #         print(e)
    #         return False

    def insertDataInTable(self, dbName, tableName):

        try:
            mycursor = self.conn.cursor()
            mycursor.execute("USE {}".format(dbName))  # Execute SQL Query to check all the existing databases
            try:
                with open('data.txt') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        mycursor.execute("INSERT INTO {} VALUES (%s, %s, %s)".format(tableName), row)

                self.conn.commit()
                print("Values Inserted")
                return True
            except Error as e:
                print(e)
                return False
        except Error as e:
            print(e)
            return False

    def readDataInTable(self, tableName):
        # cursor() method create a cursor object
        mycursor = self.conn.cursor()
        try:
            mycursor.execute("SELECT * FROM {}".format(tableName))  # Execute SQL Query to print data present in table
            result = mycursor.fetchall()
            print("Values Presents in the Table {}".format(tableName))
            for i in result:
                print(i)
            return True
        except Error as e:
            print(e)

    def deleteDataInTable(self, tableName, userinput):
        # cursor() method create a cursor object
        mycursor = self.conn.cursor()
        try:
            mycursor.execute("DELETE FROM {} WHERE Car_Color = '{}'".format(tableName, userinput))  # Execute SQL Query to delete data from Table
            self.conn.commit()
            print("Values Deleted")
            return True
        except Error as e:
            print(e)

    def updateDataInTable(self, tableName, newValue, oldValue):
        # cursor() method create a cursor object
        mycursor = self.conn.cursor()
        try:
            mycursor.execute("UPDATE {} SET Car_Color = '{}' WHERE Car_Color = '{}'". format(tableName, newValue, oldValue))  # Execute SQL Query to update data from Table
            self.conn.commit()
            print("Value Updated")
            return True
        except Error as e:
            print(e)
