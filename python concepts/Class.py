# CLASS IS DEF WITH CLASS AND CLASS NAME IN CAPITIAL LETTER
# CLASS NAME ARE USUALLY WRITTEN IN CAMELCASE LETTER

print("Hello there!", end='')


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
