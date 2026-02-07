class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.performance = 0

    def rate(self, score):
        self.performance = score

    def bonus(self):
        return self.salary * (self.performance / 100)


class Department:
    def __init__(self, name):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def payroll(self):
        total = 0
        for e in self.employees:
            total += e.salary + e.bonus()
        return total


class Company:
    def __init__(self):
        self.departments = []

    def add_department(self, d):
        self.departments.append(d)

    def financial_report(self):
        total = sum(d.payroll() for d in self.departments)
        print("Umumiy ish haqi:", total)


it = Department("IT")
it.add_employee(Employee("Jahongir", 5000000))
it.employees[0].rate(20)

company = Company()
company.add_department(it)
company.financial_report()
