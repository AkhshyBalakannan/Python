# FUNCTIONS

# DECLARING FUNCTION

from typing import ContextManager


def speak():
    print('Hello! Can you read me!')


speak()

# DECLARING A FUNCTION WITH ARGUEMENTS


def speak(name):
    print(f'Hello {name}! Can you read me!')


speak("Akhshy")

# USER INTERFACE FUNCTION


def speak(name):
    print(f'Hello {name}! Can you read me!')


name = input('Hey Whats your name: ')
speak(name)

# Default argument values – default arguments to parameters


def speak(name="unknown"):
    print(f'Hello {name}! Can you read me!')


speak()

# RETURN KEYWORD


def sum(num1, num2):
    return num1 + num2


ans = sum(2, 3)
print(ans)

# DEFAULT VALUES CAN BE GIVEN OR INCHANGED VALUES CAN BE GIVEN


def sum(num1, num2):
    return num1 + num2


ans = sum(num2=2, num1=3)
print(ans)

# WE CAN ALSO HAVE MUTABLE OBJECT


def func(a, List=[]):
    List.append(a)
    return List


print(func(1))
print(func(2))
print(func(3))


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


combined_example(1, 2, 3)
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# TypeError: combined_example() takes 2 positional arguments but 3 were given

combined_example(1, 2, kwd_only=3)
# 1 2 3

combined_example(1, standard=2, kwd_only=3)
# 1 2 3

combined_example(pos_only=1, standard=2, kwd_only=3)

# Here we have the position and keywords arg
# Where the position are given by a * in the ending if its seaparated by ,
# If the same type arguments are in args *args takes all the value and stores as tuple
# where as after an *args all becomes an kwargs **kwargs because we cannot access them


def concat(*args, sep="/"):
    return sep.join(args)


concat("earth", "mars", "venus")
# 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'


# Unpacking Argument List:
# The reverse situation occurs when the arguments are already in a list or tuple
list(range(3, 6))            # normal call with separate arguments
# [3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
# [3, 4, 5]


# dictionaries can deliver keyword arguments with the ** -operator:
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !


# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# TypeError: combined_example() got an unexpected keyword argument 'pos_only'


#  ARGUEMENTS UNPACKING TUPLE AND DICTIONARY
# *NAME IS PRESENT, IT RECEIVES A TUPLE
# **NAME IS PRESENT, IT RECEIVES A DICTIONARY

# TUPLE EXAMPLE


def user(name, *usernames):
    print(f'Hello {name}')
    print('User names used !!')
    for username in usernames:
        print(username)


user("AKHSHY", "itme_ak", "akhshy", "akhshyG")

# DICTIONARY EXAMPLE


def user(name, *usernames, **friends):
    print(f'Hello {name}')
    print('User names used !!')
    for username in usernames:
        print(username)
    keys = sorted(friends.keys())
    for key in keys:
        print(key, ":", friends[key])


user("AKHSHY", "itme_ak", "akhshy", "akhshyG",
     bairavan="close", karan="not close", jeffry="close")


# DOCUMENTATION STRING
# THIS IS NORMALLY USED TO DEOCUMENT OR IN OTHER WORDS TO
# KNWO WHAT OUR FUNCTION OR CLASS DO IN THE PARTICULAR CODE
# THIS IS DIFFERENT FROM COMMENT BECAUSE WE CAN GET THIS DOC BY SATING
#   HELP(FUNCTION_NAME) OR PRINT(FUNCTION_NAME._ _ D O C _ _)

def my_function():
    """Do nothing, but document it.
      No, really, it doesn't do anything.
     """
    pass


print(my_function.__doc__)

# Function Annotations

# Function annotations are like docstring which are present in __doc__
# here the annotations are present in __annotations__ where you can
# see the type of arg we give in and the return type
# to define it we do it using the : next to the args and
# -> for the return type.


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
# Annotations: {'ham': < class 'str' > , 'return': < class 'str' > , 'eggs': < class 'str' > }
# Arguments: spam eggs
# 'spam and eggs'
