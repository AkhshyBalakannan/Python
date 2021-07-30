# THIS IS THE MODERN WAY OF TELLING A FUNCTION TO TAKE A FUNCTION AS ARGUMENT

# THIS DECORATOR IS WRITTEN WITH AN @ SYMBOL BEFORE AND THIS MEANS CALLING THE FUNCTION AND
# PASSING SOME FUNCTION AS ARGUMENT BY SIMPLY CALLING THE FUNCTION NAME ITSELF

# TYPING DECORATOR FUNCTION IS SIMPLY DECLARING A FUNCTION AND RETURNING THE FUNCTION UPON CALL
# USUALLY THE INNER FUNCTION REMAINS THE SAME NAME AS THE OUTTER FUNCTION NAME WITH WRAPPER_

import time
import functools


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

# THE ABOVE FUNCTION IS THE BASIC CONCEPT OF HOW A DECORATOR WORKS
# THE DECORATOR FUNCTION IS DEFINED ABOVE AND THE FUNCTION WE WANT IS DEFINED BELOW
# TO SEND THE FUNCTION AS AN ARGUMENT WE NEED TO CALL THE DECORATOR FUNCTION NAME AND
# PASS THE FUNCTION NAME AS ARG


# BELOW CODE IS THE SIMPLEST WAY TO WRITE THE SAME PROG FLOW
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


# THE ABOVE CODE MEANS CALLING THE DECORATION FUNCTION WITH AN ARGUMENT OF SAY_WHEE FUNCTION


# HOW EVER WHEN WE USE DECORATOR IF THE FUNCTION WE TYPE WANTS TO RETURN SOMETHING OUR DECORATOR SHOULD
# BE WRITTEN IN SUCH A WAY THAT ITS WRAPPER FUNCTION WILL RETURN THE FUNC WE SEND INSIDE IT

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        # THIS IS THE LINE I AM TALKING ABOUT RETURNING THE FUNCTION
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# WE ALSO USE FUNCTOOL TO AVOID THE INTROSPECTOR TO TELL OUT
# THE DECORATION FUNCTION INSTEAD OF FUNCTION WE CALL


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

# Now say_whee() is still itself after decoration.


# TIME SLEEP


# import time
# import functools

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
