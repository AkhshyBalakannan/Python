# IMPORTING PACKAGES ARE SIMPLE AS TYPING IMPORT

import builtins
import math as m

from Functions import speak

speak()

print(dir(m))


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# This below line checks for the execution CWD if its same than will run the code
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# the below lines of code are given for reloading
# the interpreter if we make chnages to our module

# importlib.reload(), e.g. import importlib
# importlib.reload(modulename).

# Standard Modules:
# the winreg module is only provided on Windows systems.
# One particular module deserves some attention: sys,
# which is built into every Python interpreter.
# The variables sys.ps1 and sys.ps2 define the
# strings used as primary and secondary prompts

# >>> import sys
# >>> sys.ps1
# '>>> '
# >>> sys.ps2
# '... '
# >>> sys.ps1 = 'C> '
# C > print('Yuck!')
# Yuck!
# C >

# the above lines are present in the intrepreter

# The variable sys.path is a list of strings that determines the interpreter’s search path for modules.


# FUNCTION

# Build in function most common are
dir(module_name)
# Which will return us the exact method present inside
# dir() does not list the names of built-in functions and variables.
# If you want a list of those, they are defined in the standard module builtins:

# import builtins
dir(builtins)

#  WE ALSO INSTALL MODULES FROM PYTHON MANAGER THAT IS PIP
# PIP INSTALL PACKAGE_NAME

# VIRTUAL ENVIRONMENT IS HAVING SEPARATE INSTALLATION FILE TO INSTALL THE NEW MODULES INIT
# TO START AN VIRTUAL ENVIRONMENT WE TYPE                   PYTHON -M VENV VENV_NAME
# TO ACTIVATE IT WE TYPE                                    venv/Scripts/activate.bat
# WE ALSO CAN CREATE A REQUIREMENT TEXT BY                  PIP FREEZE > REQUIREMENTS.TXT
# TO INSTALL THE REQUIREMENT WE TYPE                        PIP INSTALL -R REQUIREMENTS.TXT
