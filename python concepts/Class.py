# CLASS IS DEF WITH CLASS AND CLASS NAME IN CAPITIAL LETTER
# CLASS NAME ARE USUALLY WRITTEN IN CAMELCASE LETTER

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

print("Hello there!", end='')


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


# In the MyClass example,
# this will return the string 'hello world'.
# However, it is not necessary to call a method right away:
# x.f is a method object, and can be stored away and called at a later time.
x = MyClass()
xf = x.f
# while True:
print(xf())


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs
# ['roll over', 'play dead']


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

# To not share the variable with all the instance we need to give it in const func


# Function defined outside the class
# This below example is just to confuse the reader normally we dont write code like this
def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


# the best way to name is to use the self keyword inside the class
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


class Planet:
    def __init__(self):  # CONSTRUCT TYPE INIT
        self.name = 'earth'
        self.radius = 20000
        self.system = 'Hoth system'

    def orbit(self):  # METHOD CREATED
        return f'{self.name} is orbiting in the {self.system}'


Pluto = Planet()
print(f'Name is: {Pluto.name}')
print(f'Radius is: {Pluto.radius }')
print(Pluto.orbit())

# THIS ABOVE EXAMPLE IS THE BASIC LEVEL OF CREATING CLASS WITH THE INSTANCES
# GIVEN WITH DEFAULT NAME WHICH IS NOT CORRECT BECAUSE THIS WILL NOT BE
# DYNAMIC WITH THE PRPGRAM AND SO WE TYPE THE CLASS INIT WITH ARG
# GIVEN THAT MATCHES THE SELF NAME AND EACH TIME A CLASS IS CALLED NEW DEFAULT
# VALUES ARE GIVEN TO THE CLASS SO IT BECOMES DYNAMIC


class Planet:
    def __init__(self, name, radius, system):  # ARG ARE GIVEN FOR DYNAMIC PURP
        self.name = name
        self.radius = radius
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


Pluto = Planet('earth', 2000, 'Hoth system')
print(f'Name is: {Pluto.name}')
print(f'Radius is: {Pluto.radius }')
print(Pluto.orbit())


# Class and Instance Variables

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs
e.kind                  # shared by all dogs
d.name                  # unique to d
e.name                  # unique to e

# CLASS VARIABLE || INSTANCE VARIABLE
# CLASS METHOD || INSTANCE METHOD
# STATIC METHOD || INSTANCE METHOD


class Planet:

    shape = 'round'  # CLASS VARIABLE ( BOTH )

    def __init__(self, name, radius, system):  # INSTANCE
        self.name = name        # INSTANCE VARIABLE
        self.radius = radius    # INSTANCE VARIABLE
        self.system = system    # INSTANCE VARIABLE

    def orbit(self):            # INSTANCE METHOD ( ONLY INST )
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def common(cls):            # CLASS METHOD ( BOTH )
        return f'All are {cls.shape}'  # USES THE CLASS VAR

    @staticmethod
    def spin(speed='really fast'):  # CANNOT TAKE COMMON VAR ONLY SHOULD TAKE PARAMETERS
        return f'Speed will be {speed}'  # NO ACCESS TO SHAPE


earth = Planet('earth', '2000', 'solar')
print(earth.orbit())    # instance method
# print(Planet.orbit())   # false if we call because it requires one arg
print(Planet.shape)
print(earth.shape)
print(Planet.common())
print(earth.common())
print(Planet.spin("dont know sorry"))
print(earth.spin("dont know sorry"))


# INHERITANCE

# INHERITANCE USING CLASS NAME

class A:    # CLASS A WITH METHODS
    def func1():
        print("from class A func 1")

    def func2():
        print("from class A func 2")


A.func1()   # CALLING CLASS A METHODS
A.func2()  # CALLING CLASS A METHODS


class B(A):    # CLASS B METHOD ALSO HAS A
    def func3():
        print("from class B func 3")

    def func4():
        print("from class B func 4")


B.func1()  # CALLING CLASS A METHODS
B.func2()  # CALLING CLASS A METHODS
B.func3()  # CALLING CLASS B METHODS
B.func4()  # CALLING CLASS B METHODS


class C:
    def func5():
        print("from class C func 5")

    def func6():
        print("from class C func 6")


class D(C, B):
    def func7():
        print("from class D func 7")

    def func8():
        print("from class D func 8")


D.func1()
D.func2()
D.func3()
D.func4()
D.func5()
D.func6()
D.func7()
D.func8()

# Private Variables
# We dont have any special notations to note a private and public Key
# And so we give it as underscore which will be read as non-public key


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# In class we have an instance method which can be found using
# m.__self__ as the instance method m() and m.__func is the
# function object corresponding to the method

# Special Attributes

# object.__dict__
    # A dictionary or other mapping object used to store an object’s(writable) attributes.

# instance.__class__
# The class to which a class instance belongs.

# class.__bases__
# The tuple of base classes of a class object.

# definition.__name__
# The name of the class, function, method, descriptor, or generator instance.

# definition.__qualname__
# The qualified name of the class, function, method, descriptor, or generator instance.

# class.__mro__
# This attribute is a tuple of classes that are considered when looking
# for base classes during method resolution.

# class.mro()
# This method can be overridden by a metaclass to customize the method
# resolution order for its instances. It is called at class instantiation,
# and its result is stored in __mro__.

# class.__subclasses__()
# Each class keeps a list of weak references to its immediate subclasses.
# This method returns a list of all those references still alive. Example:

# int.__subclasses__()
# [ < class 'bool' > ]
