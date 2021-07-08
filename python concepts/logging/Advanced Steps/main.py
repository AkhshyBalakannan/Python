# This logging main is little different because we are here importing module
# This employee module has its own logger where datas are logged
# In python when we import something the entire module is run first and so logs data
# And using the common root logger is not good has we cannot separate the log function
# Also using the same logger will not log lower priority things

# NOTE Logger different from logging

import logging
import employee

# User defined logger
logger = logging.getLogger(__name__)
# Setting up Level for logger
logger.setLevel(logging.DEBUG)
# Formatter for logger
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# Telling the handler to create the file with name sample.log
file_handler = logging.FileHandler('sample.log')

# This isto tell the logger at some specific time to log only on error
# file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

# This StreamHandler is to print the data even in console and also to store them in log file
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# The below line will not used because we are not going to use the base root logger
# logging.basicConfig(filename='main.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


def add(num1, num2):
    """Add Function"""
    return num1 + num2


def divide(num1, num2):
    """Divide Function"""
    return num1/num2
# Below code is to be run with the uncomment of line 23 to print error alone
    # try:
    #     result = num1 / num2
    # except ZeroDivisionError:
    #     logger.exception('Tried to divide by zero') # Giving .exception will include error trace back
    # else:
    #     return result


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logger.debug(f'Add: {num_1} + {num_1} = {add_result}')

div_result = divide(num_1, num_2)
logger.debug(f'Div: {num_1} / {num_2} = {div_result}')
