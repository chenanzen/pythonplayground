from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current employees:")
        for employee in self.employees:
            print(f"{employee.fname} {employee.lname}")
        print("--------------------")

    def pay_employees(self):
        for employee in self.employees:
            print("Paycheck for:", employee.fname, employee.lname);
            print(f"Amount: ${employee.calculate_paycheck():,.2f}")
            print("--------------------")

def main():
    my_company = Company()
    employee1 = Employee("John", "Doe", 50000)
    employee2 = Employee("Jane", "Smith", 60000)
    employee3 = Employee("Joe", "Johnson", 70000)

    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()