'''This is the main module where the application starts'''
from user import User
import logging
import database_operation

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('user_step_up.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def transaction(user_name):
    pass


def start_up():
    try:
        account = int(input('ALREADY USER OR SIGN UP (1/2): '))
        if(account == 2):
            print('Lets start... ')
            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            password = input('Password: ')
            # amount = input('Amount: ')
            user_obj = User(first_name, last_name, password)
            logger.info(
                f'Created Employee: {user_obj.full_name()} - {user_obj.user_id()}')
            database_operation.insert_user(
                user_obj.user_id(), user_obj.first_name, user_obj.last_name, user_obj.password, user_obj.amount)
            logger.info("Account has been added to the database ",
                        user_obj.full_name(), user_obj.user_id())
            # deposit_withdraw = input(
            #     "Want to deposit or withdraw amount (D/W): ").upper()
            # if(deposit_withdraw == 'D'):
            #     amount = int(
            #         input("Please enter the amount to be depositied: "))
            #     database_operation.deposit_amount(user_obj.user_id(), amount)

            # else:
            #     pass

        else:
            user_name = input('Please enter your user name: ')
            password = input('Please enter your password: ')
            user = database_operation.get_user_detail(user_name)
            # deposit_withdraw = input(
            #     "Want to deposit or withdraw amount (D/W): ").upper()
            # if(deposit_withdraw == 'D'):
            #     amount = int(
            #         input("Please enter the amount to be depositied: "))
            #     database_operation.deposit_amount(user_name, amount)

        delete_account = input(
            "Do you want to delete your account (Y/N): ").upper()
        if delete_account == 'Y':
            database_operation.delete_user_data(user_obj.user_id())

    except Exception as e:
        logger.exception(f'\n{e}')

    finally:
        print('Thank you')


start_up()
