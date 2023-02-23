import sqlite3

CHECK_IF_EMPLOYEES_EXISTS = "SELECT name FROM sqlite_master WHERE type='table' AND name='Employees'"
CHECK_IF_SHIFTS_EXISTS = "SELECT name FROM sqlite_master WHERE type='table' AND name='Shifts'"
CHECK_IF_HOLIDAYS_EXISTS = "SELECT name FROM sqlite_master WHERE type='table' AND name='Holidays'"

class DatabaseController():
    
    def __init__(self, filePath):
        try:
            self.connection = sqlite3.connect(filePath)
            print("Database initialised")
            cursor = self.connection.cursor()
            
            cursor.execute(CHECK_IF_EMPLOYEES_EXISTS)
            if cursor.fetchall() == []:  #Employees table does not exist
                self.createEmployeesTable()
                print("Employees table successfully created")

            cursor.execute(CHECK_IF_SHIFTS_EXISTS)
            if cursor.fetchall() == []:  #Shifts table does not exist
                self.createShiftsTable()
                print("Shifts table successfully created")
                
            cursor.execute(CHECK_IF_HOLIDAYS_EXISTS)
            if cursor.fetchall() == []:  #Shifts table does not exist
                self.createHolidaysTable()
                print("Holidays table successfully created")

            cursor.close()
        except sqlite3.Error as error:
            print("Error initialising database")
            print(error)
            
    def executeSelectQuery(self, query):
        cursor = self.connection.cursor()
        results = cursor.execute(query)
        resultSet = []
        for row in results:
            resultSet.append(row)
            #each row is a tuple
        cursor.close()
        return resultSet
        
    def executeQuery(self, query):
        success = True
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as error:
            print(error)
            success = False
        finally:
            cursor.close()
            return success

    def closeDatabase(self):
        self.connection.close()
        print("Database closed")

    def createEmployeesTable(self):
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
        return self.executeQuery(query)

    def getColumnNames(self, query):
        cursor = self.connection.execute(query)
        return [data[0] for data in cursor.description]

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
        query += str(employeeID) + ", \"" + startTime + "\", \"" + endTime + "\", \"" + date + "\", \"" +breakTime+ "\");"
        return self.executeQuery(query)
        
    def createHolidaysTable(self):
        try:
            self.connection.execute("""CREATE TABLE Holidays(
                                    HolidayID integer primary key, 
                                    EmployeeID integer NOT NULL,
                                    startDate varchar(10) NOT NULL, 
                                    endDate varchar(10) NOT NULL 
                                    )""")
        except sqlite3.Error as error:
             print(error)
             self.closeDatabase()
    
    def createHoliday(self, employeeID, startDate, endDate):
        query = "INSERT INTO Holidays (HolidayID, EmployeeID, startDate, endDate) VALUES ("
        query += str(employeeID) + ", \"" + startDate + "\", \"" + endDate + "\");"
        return self.executeQuery(query)

