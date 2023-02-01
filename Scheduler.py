from DatabaseController import *

class Scheduler:
    def __init__(self, filename):
        self.DBcontroller = DatabaseController(filename)

    def getShiftsForDay(self, date):
        query = """SELECT Employees.firstName, Employees.surname, Shifts.startTime, Shifts.endTime, Shifts.breakTime 
        FROM Shifts JOIN Employees 
        ON Shifts.EmployeeID = Employees.EmployeeID 
        WHERE Shifts.date = \"""" + date + "\";"
        return self.DBcontroller.executeSelectQuery(query);

    def addEmployee(self, firstName, surname, age, department):
        self.DBcontroller.createEmployee(firstName, surname, age, department)

    def addShift(self, employeeID, startTime, endTime, date, breakTime):
        self.DBcontroller.createShift(employeeID, startTime, endTime, date, breakTime)

    def closeDatabase(self):
        self.DBcontroller.closeDatabase()

    def getEmployeeData(self, employeeID, firstName, surname, age):
        self.DBcontroller.getEmployeeData(employeeID, firstName, surname, age)

  
