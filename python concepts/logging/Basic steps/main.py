# This logging is simpley used instead of print statements where the
# print statements cannot be caught and is left in air at that time
# to store the data we use logging which is library included in python

import logging


# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='main.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(num1, num2):
    """Add Function"""
    return num1 + num2


def divide(num1, num2):
    """Divide Function"""
    return num1/num2


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug(f'Add: {num_1} + {num_1} = {add_result}')

div_result = divide(num_1, num_2)
logging.debug(f'Div: {num_1} / {num_2} = {div_result}')
