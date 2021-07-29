# EXCEPTION HANDLING

# two distinguishable kinds of errors: syntax errors and exceptions

# Clean-up action is name given to the finally block

# exception EnvironmentError
# exception IOError
# exception WindowsError
# Only available on Windows.

# SAME CONCEPT OF TRY CATCH BLOCK IS FOLLOWED BUT THE DIFFERENCE HERE IS IT USES EXCEPT

from os import system


a = 5
b = 0

try:
    div = a / b

except Exception as e:
    print("'You Know I know' We are in ERROR")

# MOST BASIC CONCEPT OF EXCEPTIONAL ERROR
# WE ALSO HAVE NAME FOR EVERY ERROR WE GET AND WE CAN MATCH THOSE NAMES

a = 5
b = 5

try:
    div = a / b
    integer = int(input("I know! Enter an letter to goto except block: "))

except ZeroDivisionError as z:
    print("'You know I know' ZERO DIVISION ERROR")

except ValueError as v:
    print("'You know I know' VALUE ERROR")

except Exception as e:
    print("'You Know I know' We are in ERROR")

# FINALLY BLOCK WHICH RUNS FOR ALL EVEN IF WE FACE ERROR OR EVEN IF WE DONT FACE ERROR

a = 5
b = 1

try:
    div = a/b
    int(input("ENTER: "))

except:
    print("error")

finally:
    print("THIS IS FINALLY")

# TO RAISE AN ERROR WE USE RAISE

# We also have else statement which helps in reducing the code in try
# this is used when we know else block code wont produce error but try would
for arg in system.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# we also have __str__ for teh exception which is triggered

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

# <class 'Exception' >
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs

# If we need to re raise an exception even if its caught in except we do

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise # this has to be uncommented

# An exception flew by!
# Traceback(most recent call last):
#   File "<stdin>", line 2, in <module >
# NameError: HiThere

print(10 * (1/0))
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# ZeroDivisionError: division by zero

print(4 + spam*3)
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# NameError: name 'spam' is not defined

print('2' + 2)
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# TypeError: Can't convert 'int' object to str implicitly

# List of Builtin Exceptions

# exception LookupError
# exception BufferError
# exception ArithmeticError


# USER DEDFINED ERROR


class UserDefinedError(Exception):
    def __init__(self, message):
        self.message = message


try:
    raise UserDefinedError("HEY I AM THE ERROR MESSAGE")

except UserDefinedError as u:
    print(u.message)

finally:
    print("I think your clear with User Defined Error")


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# Predefined Clean-up action

# the problem with below code is it leaves the code open
for line in open("myfile.txt"):
    print(line, end="")

# instead of manually giving close file for each open we can use with
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
