import sqlite3

class DatabaseController():
    
    def __init__(self, filePath):
        try:
            self.connection = sqlite3.connect(filePath)
            self.cursor = self.connection.cursor()
            print("Database initialised")
        except sqlite3.Error as error:
            print("Error initialising database")
            print(error)
            
    def executeSelectQuery(self, query):
        self.cursor = self.connection.cursor()
        results = self.cursor.execute(query)
        resultSet = []
        for row in results:
            resultSet.append(row)
            #each row is a tuple
        self.cursor.close()
        return resultSet
        
    def executeQuery(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as error:
            print(error)
            self.closeDatabase()
        finally:
            self.cursor.close()

    def closeDatabase(self):
        self.connection.close()
        print("Database closed")

    def createEmployeeTable(self):
        try:
            self.connection.execute("""CREATE TABLE Employees(
                                    EmployeeID integer primary key, 
                                    firstName varchar(20) NOT NULL, 
                                    surname varchar(20) NOT NULL, 
                                    age integer NOT NULL, 
                                    department varchar(20) NOT NULL
                                    )""")
        except sqlite3.Error as error:
            print(error)
            self.closeDatabase()

    def createEmployee(self, firstName, surname, age, department):
        query = "INSERT INTO Employees (firstName, surname, age, department) VALUES (\""
        query += firstName + "\", \"" + surname + "\", " + str(age) + ", \"" + department + "\");"
        self.executeQuery(query)


    def createShiftsTable(self):
        try:
            self.connection.execute("""CREATE TABLE Shifts(
                                    ShiftID integer primary key, 
                                    EmployeeID integer NOT NULL,
                                    StartTime varchar(5) NOT NULL, 
                                    endTime varchar(5) NOT NULL, 
                                    date varchar(10) NOT NULL, 
                                    breakTime varchar(5) NOT NULL
                                    )""")
        except sqlite3.Error as error:
             print(error)
             self.closeDatabase()



    # times: "HH:MM" (5 characters)
    # Date : "DD:MM:YYYY" (10 characters)
    def createShift(self, employeeID, startTime, endTime, date, breakTime):
        query = "INSERT INTO Shifts (employeeID, startTime, endTime, date, breakTime) VALUES ("
        query += employeeID + ", \"" + startTime + "\", \"" + endTime + "\", \"" + date + "\", \"" +breakTime+ "\");"
        self.executeQuery(query)

