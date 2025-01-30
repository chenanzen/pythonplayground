class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    # get weekly salary from annual salary in prop
    def calculate_paycheck(self):
        return self.salary / 52