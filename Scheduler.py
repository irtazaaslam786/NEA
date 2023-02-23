from DatabaseController import *

class Scheduler:
    def __init__(self, filename):
        self.DBcontroller = DatabaseController(filename)

    def getShiftsForDay(self, date):
        query = """SELECT Employees.firstName, Employees.surname, Shifts.startTime, Shifts.endTime, Shifts.breakTime 
        FROM Shifts JOIN Employees 
        ON Shifts.EmployeeID = Employees.EmployeeID 
        WHERE Shifts.date = \"""" + date + "\";"
        return self.DBcontroller.executeSelectQuery(query), self.DBcontroller.getColumnNames(query)

    def addEmployee(self, firstName, surname, age, department):
        if len(firstName) > 20 or len(firstName) == 0:
            return False
        elif len(surname) > 20 or len(surname) == 0:
            return False
        elif age < 17:
            return False
        elif len(department) > 20 or len(department) == 0:
            return False
        return self.DBcontroller.createEmployee(firstName, surname, age, department)

    def addShift(self, employeeID, startTime, endTime, date, breakTime):
        if len(startTime) != 5:
            return False
        elif len(endTime) != 5:
            return False
        elif len(date) != 10:
            return False
        elif len(breakTime) != 5:
            return False
        
        return self.DBcontroller.createShift(employeeID, startTime, endTime, date, breakTime)

    def closeDatabase(self):
        self.DBcontroller.closeDatabase()

    def getEmployeeData(self):
        query = """SELECT * from Employees;"""
        return self.DBcontroller.executeSelectQuery(query), self.DBcontroller.getColumnNames(query)

    def getHolidays(self):
        query = """SELECT Holidays.HolidayID, Employees.firstName, Employees.surname, Holidays.startDate, Holidays.endDate 
        FROM Holidays JOIN Employees
        ON Holidays.EmployeeID = Employees.EmployeeID
        ORDER BY Holidays.startDate ASC;"""
        return self.DBcontroller.executeSelectQuery(query), self.DBcontroller.getColumnNames(query)
