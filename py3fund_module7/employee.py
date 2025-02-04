class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    # get weekly salary from annual salary in prop
    def calculate_paycheck(self):
        return self.salary / 52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    # get weekly salary from hourly rate and hours worked
    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate
    
class CommissionedEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales, commission_rate):
        super().__init__(fname, lname, salary)
        self.sales = sales
        self.commission_rate = commission_rate

    # get weekly salary from sales and commission rate
    def calculate_paycheck(self):
        regular_paycheck =  super().calculate_paycheck() 
        commission = self.sales * self.commission_rate
        return regular_paycheck + commission