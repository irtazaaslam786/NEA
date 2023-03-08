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

    def addHoliday(self, employeeID, startDate, endDate):
        return self.DBcontroller.createHoliday(employeeID, startDate, endDate)

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

    def deleteEmployee(self, firstName, surname, department):
        query = """SELECT EmployeeID 
        FROM Employees 
        WHERE firstName = \"{0}\" AND surname = \"{1}\" AND department = \"{2}\""""
        query = query.format(firstName, surname, department)
        employeeID = self.DBcontroller.executeSelectQuery(query)[0][0]

        query = "DELETE FROM Employees WHERE EmployeeID = " + str(employeeID)
        return self.DBcontroller.executeQuery(query)

    def deleteShift(self, firstName, lastName, startTime, endTime):
        query = """SELECT Shifts.ShiftID 
        FROM Shifts JOIN Employees ON Employees.EmployeeID = Shifts.ShiftID 
        WHERE Employees.firstName = \"{0}\" AND Employees.surname = \"{1}\" AND Shifts.startTime = \"{2}\" AND Shifts.endTime = \"{3}\""""
        query = query.format(firstName, lastName, startTime, endTime)
        shiftID = self.DBcontroller.executeSelectQuery(query)[0][0]

        query = "DELETE FROM Shifts WHERE ShiftID = " + str(shiftID)
        return self.DBcontroller.executeQuery(query)

    def deleteHoliday(self, firstName, surname, startDate):
        query = """SELECT Holidays.HolidayID 
        FROM Employees JOIN Holidays ON Employees.EmployeeID = Holidays.EmployeeID 
        WHERE Employees.firstName = \"{0}\" AND Employees.surname = \"{1}\" AND Holidays.startDate = \"{2}\""""
        query = query.format(firstName, surname, startDate)
        holidayID = self.DBcontroller.executeSelectQuery(query)[0][0]

        query = "DELETE FROM Holidays WHERE HolidayID = " + str(holidayID)
        return self.DBcontroller.executeQuery(query)
