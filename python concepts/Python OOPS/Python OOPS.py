# From Basics create class instance object
import datetime


class Employee():
	raise_amt = 1.04

	def __init__(self, name, pay):
		self.name = name
		self.pay = pay

	def email(self):
		'''Instance method which uses self'''
		return f'{self.name}@company.com'

	def apply_raise(self):
		# This line is for class attr being used as instance which is created
		self.pay = int(self.pay*self.raise_amt)
# 		self.pay = int(self.pay*Employee.raise_amt)	# This line is for class attr being used

# Usually the above two lines does the same job in front end but in back
# 	first line will create an new instance attribute
# 	second line will use the common class attribute
# Once changing the first line will change the value of instance attributes
# Once changing the second line will change the value of class attributes

	@classmethod
	def create_employee(cls, emp_str):
		'''Class method which uses cls'''
		name, pay = emp_str.split('-')
		return cls(name, pay)

	@staticmethod
	def is_workday(day):
		'''Static method given with attributes explicitly'''
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	def __len__(self):
        return len(self.name)

    def __repr__(self):
	    return f'Employee({self.name}, {self.pay})'
        
	def __str__(self):
	    return self.name
	    
	def __add__(self, other):
	    '''custom add method for employee
	    add two employee pay'''
	    return self.pay + other.pay
	    
	def __sub__(self, other):
	    '''custom sub method for employee
	    sub two employee pay'''
	    if self.pay < other.pay:
	        return other.pay - self.pay
	    else:
	        return self.pay - other.pay
        
    
    
emp1 = Employee('akhshy', 50000)

print(emp1.email())
print(emp1.pay)
emp1.apply_raise()
print(emp1.raise_amt)
print(emp1.pay)
emp1.raise_amt = 1.05 # Create instance attr
emp1.apply_raise()
print(emp1.pay)
print(emp1.raise_amt)
print(Employee.raise_amt)

print("Returns the str value")
print(emp1)
print("Return repr magic function")
print(repr(emp1))
print("Can also be called by __repr__")
print(emp1.__repr__())
print("Return str magic function")
print(str(emp1))
print("Can also be called by __str__")
print(emp1.__str__())

print("Adding two emp pay")

emp2 = Employee.create_employee("ashwin-50000") # Which will create new object instance
print(emp2.email())
emp3 = Employee("bala", 50000)
print("Adding two emp pay")
print(emp1+emp3)

print("Sub two emp pay")
print(emp3-emp1)

print("Use the custom len")
print(len(emp1))

print(Employee.is_workday(datetime.date(2021,8,20))) # This is static method called using the class name

class Developer(Employee):
	'''Simple class Inheritance'''
	raise_amt = 1.10

	def __init__(self, name, pay, prog_lang):
		''' Inherit the INIT function to use super '''
# 		super().__init__(name, pay)
		Employee.__init__(self, name, pay) # Both lines are similar but this is mostly used when multi-inheritance is done
		self.prog_lang = prog_lang

dev1 = Developer('ashwin', 50000, 'JAVA')

print(dev1.email())
print(dev1.raise_amt)
print(dev1.prog_lang)
dev1.apply_raise() # Here the raise_amt inside this subclass is used

print(dev1.pay)

class Manager(Employee):
    def __init__(self, name, pay, employees=None):
        super().__init__(name, pay)
        if employees is None:
            employees = [] # This is done becuase we shouldnt give an mutable datatype as attribute
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print(emp.email())
            
mngr1= Manager('balakannan', 90000, [emp1])
# mngr1= Manager('balakannan', 90000)
# mngr1.add_emp(emp1)
print(mngr1.pay)
mngr1.print_emp()
print('After Adding')
mngr1.add_emp(emp2)
mngr1.print_emp()
print('After Removing')
mngr1.remove_emp(emp1)
mngr1.print_emp()

print(isinstance(emp1, Employee)) # True
print(isinstance(emp1, Manager)) # False
print(issubclass(Manager, Employee)) # True
print(issubclass(Developer, Employee)) # True
print(issubclass(Developer, Manager)) # False



'''
OUTPUT

akhshy@company.com
50000
1.04
52000
54600
1.05
1.04
Returns the str value
akhshy
Return repr magic function
Employee(akhshy, 54600)
Can also be called by __repr__
Employee(akhshy, 54600)
Return str magic function
akhshy
Can also be called by __str__
akhshy
Adding two emp pay
ashwin@company.com
Adding two emp pay
104600
Sub two emp pay
4600
True
ashwin@company.com
1.1
JAVA
55000
90000
akhshy@company.com
After Adding
akhshy@company.com
ashwin@company.com
After Removing
ashwin@company.com
True
False
True
True
False
'''


# Property Decorator
class Student():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first+ '.'+last+'@gmail.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

std = Student("akhshy","balakannan")
print(std.email)
print(std.fullname())

class Student():
    id_no = 1
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self._student_id = Student.id_no
        Student.id_no += 1
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @property
    def student_id(self):
        return self._student_id
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Just to know - Deleting")
        self.first = None
        self.last = None

std = Student("akhshy","balakannan")
print(std.email)
print(std.fullname)

std.fullname = "Akhshy Balakannan"
print(std.first)
print(std.last)

del std.fullname
print(std.first)
print(std.last)

print("This student_id is protected attr which written using leading _ ")
print(std.student_id)
print(Student.id_no)

'''
OUTPUT 

akhshy.balakannan@gmail.com
akhshy balakannan
akhshy.balakannan@gmail.com
akhshy balakannan
Akhshy
Balakannan
Just to know - Deleting
None
None
This student_id is protected attr which written using leading _
1
2
'''
