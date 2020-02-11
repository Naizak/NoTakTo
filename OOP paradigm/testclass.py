# this was shown first as to explain why we use classes
"""

# instance of class / creating objects
emp_1 = Employee()
emp_2 = Employee()


# 2 different objects at memory
# <__main__.Employee object at 0x0000028CF868FDA0>
# <__main__.Employee object at 0x0000028CF868F978>
print(emp_1)
print(emp_2)

# instances of a class have unique attributes
# instance 1
emp_1.first = "John"
emp_1.last = "Doe"
emp_1.email = "john.doe@company.com"
emp_1.pay = 50000

# instance 2
emp_2.first = "Jane"
emp_2.last = "Doe"
emp_2.email = "jane.doe@company.com"
emp_2.pay = 60000

# calling each instances emails variable returns the respective email
# john.doe@company.com
# jane.doe@company.com
print(emp_1.email)
print(emp_2.email)

# doing things this way is unnecessary and prone to mistakes
# using the class Employee will help with this significantly
"""
import datetime


class Employee:

    # class variable
    raise_amount = 1.04
    num_of_employees = 0

    # this is the constructor
    # the parameters being passed in are the attributes we need to create an instance of the class
    def __init__(self, first_name, last_name, pay):
        self.fn = first_name
        self.ln = last_name
        self.pay = pay
        self.email = first_name.lower() + '.' + last_name.lower() + "@company.com"

        Employee.num_of_employees += 1

    # creating a method that will display full name of the given instance
    def full_name(self):
        return '{} {}'.format(self.fn, self.ln)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # changes the class variable raise_amount
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternate constructor
    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)

    # A give away that a method should be static is
    # if you don't access the instance(self) or class(cls) anywhere in the method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, programing_language):
        super().__init__(first_name, last_name, pay)
        self.pg = programing_language


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employee(self):
        for employee in self.employees:
            print('--->', employee.full_name())


# instance of class / creating objects
emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jane", "Doe", 60000)
dev_1 = Developer("Steve", "Smith", 90000, "Java")
mgr_1 = Manager("April", "May", 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.print_employee()
# print()
# mgr_1.add_employee(emp_2)
# mgr_1.print_employee()
# print()
# mgr_1.remove_employee(dev_1)
# mgr_1.print_employee()

# print(dev_1.email)
# print(dev_1.pg)

# Employee.set_raise_amount(1.05)

# emp_str_1 = "Steve-Smith-30000"
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)


# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))

# any function that is __[name]__() is called a Dunder for Double Underscore
