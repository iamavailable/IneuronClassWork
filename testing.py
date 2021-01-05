from test_python1_dao.DAO import DBObject
from test_python1_dao.daoutils import createSqlQuery

listOfColumns = ["Car_Color", "Car_Price", "Car_Model"]


def formCarDetailsDict(carObjlist):
    listOfCarObjDict = []

    try:
        for carObj in carObjlist:
            userDetailsObj = {listOfColumns[0]: carObj.color, listOfColumns[1]: carObj.price,
                              listOfColumns[2]: carObj.carName}
            listOfCarObjDict.append(userDetailsObj)
    except Exception as e:
        print(e)
    return listOfCarObjDict


if __name__ == '__main__':

    class Car:
        def __init__(self, color, price, carName):
            self.color = color
            self.price = price
            self.carName = carName

        def getCarColor(self, carName):
            print("self.carName called for : ", carName)
            if self.carName == carName:
                return self.color, self.price


    carObj1 = Car('Red', '25000$', 'BMWX1')
    carObj2 = Car('Blue', '35000$', 'AUDIQ1')
    carObj3 = Car('Green', '45000$', 'BMWX3')
    carObj4 = Car('White', '55000$', 'AUDIQ2')
    carObj5 = Car('Orange', '65000$', 'BMWXS')
    carObj6 = Car('Mattblack', '75000$', 'AUDIQ3')

    listOfCarObj = [carObj1, carObj2, carObj3, carObj4, carObj5, carObj6]

    host = "localhost"
    port = "3306"
    connUserName = "root"
    connPassword = ""
    dbName = "testDatabase"
    tableName = "carDetails"

    try:
        listOfCarDetailsDict = formCarDetailsDict(listOfCarObj)
        # mysql.connector.connect(user='root', password='', host='localhost', port='3306')
        dao = DBObject(connUserName, connPassword, host, port, listOfColumns)
        # dao.connect()
        if not dao.checkIfDatabaseExists(dbName):
            dao.createDatabase(dbName)
        if not dao.checkIfTableExists(dbName, tableName):
            dao.createTable(dbName, tableName)

        userInput = int(input("Press 1 to Insert,  2 to Read, 3 to Delete and 4 to Update: "))
        if userInput == 1:
            # query, records_to_insert = createSqlQuery(tableName, listOfCarDetailsDict, listOfColumns)
            # dao.insertDataInTable(dbName, query, records_to_insert)
            dao.insertDataInTable(dbName, tableName)
        elif userInput == 2:
            dao.readDataInTable(tableName)
        elif userInput == 3:
            dao.readDataInTable(tableName)
            userinput = input("Enter the Car Color to delete: ")
            dao.deleteDataInTable(tableName, userinput)
        elif userInput == 4:
            dao.readDataInTable(tableName)
            newValue = input("Enter New Car Color: ")
            oldValue = input("Enter Old Car Color: ")
            dao.updateDataInTable(tableName, newValue, oldValue)
        else:
            print("Enter Correct Keyword")

    except Exception as e:
        print(e)
