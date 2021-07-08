import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info(f'Created Employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        '''This is property function to set the email value'''
        return (f'{self.first}.{self.last}@email.com')

    @property
    def fullname(self):
        '''This is property function to set the fullname'''
        return (f'{self.first} {self.last}')


employee_1 = Employee('Akhshy', 'Balakannan')
employee_2 = Employee('Ashwin', 'Balakannan')
