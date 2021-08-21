class Employee():
    def __init__(self, name, leave=0, lop=0, status="P"):
        self.name = name
        self.leave = leave
        self.lop = lop
        self.status = status

    def tell_name(self):
        return self.name

    def add_leave(self, leave):
        self.leave = self.leave+leave

    def add_lop(self, lop):
        self.lop = self.lop+lop

    def self_respond_leave(self, res):
        self.status = res


class Manager(Employee):
    def __init__(self, name, leave=0, lop=0, status="P", downline=None):
        super().__init__(name, leave, lop, status)
        if downline is None:
            downline = []
        else:
            self.downline = downline

    @staticmethod
    def respond_leave(emp, res):
        if res == "A":
            emp.status = "A"
            emp.add_leave(1)
            emp.add_lop(1)
        else:
            emp.status = "R"


class Admin(Manager):
    def __init__(self, name, leave=0, lop=0, status="P", downline=None, down_line_manager=None):
        super().__init__(name, leave, lop, status, downline)
        if down_line_manager is None:
            self.down_line_manager = []
        else:
            self.down_line_manager = down_line_manager

    @staticmethod
    def create_emp(m_or_e, name):
        if m_or_e == 'm':
            return Manager(name)
        else:
            return Employee(name)


emp1 = Employee('akhshy')
print("create an instance")
print(emp1.name, emp1.leave, emp1.lop, emp1.status)
print("Adding leaves")
emp1.add_leave(5)
print(emp1.name, emp1.leave, emp1.lop, emp1.status)
print("Adding LOP leave")
emp1.add_lop(1)
print(emp1.name, emp1.leave, emp1.lop, emp1.status)
print("Changing status")
emp1.self_respond_leave('A')
print(emp1.name, emp1.leave, emp1.lop, emp1.status)

mngr1 = Manager('balakannan', downline=[emp1])
print("create an instance")
print(mngr1.name, mngr1.leave, mngr1.lop, mngr1.status, mngr1.downline)
admin = Admin('admin')
emp2 = admin.create_emp('e', 'ananthi')
print(emp2)
print(emp2.tell_name())
mngr1.respond_leave(emp1, "A")
print(emp1.status)
print(emp1.leave)
print(emp1.lop)
mngr1.respond_leave(emp1, "R")
print(emp1.status)
print(emp1.leave)
print(emp1.lop)

'''
create an instance
akhshy 0 0 P
Adding leaves
akhshy 5 0 P
Adding LOP leave
akhshy 5 1 P
Changing status
akhshy 5 1 A
create an instance
balakannan 0 0 P [<__main__.Employee object at 0x7fcfaf22e6a0>]
<__main__.Employee object at 0x7fcfaf22e8e0>
ananthi
A
6
2
R
'''
