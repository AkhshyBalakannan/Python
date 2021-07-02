import os
import re
import config_files
from bank_details import bank_acc
from game_details import details


class not_human(Exception):
    '''THIS IS USER DEFINED ERROR GENERATED WHEN CAPTCHA IF BLOCK IS FAILED'''

    def __init__(self, message="NOT A HUMAN BYE"):
        self.message = message

# print(not_human.__doc__)


def check_run_config_create(to_acc):
    '''THIS FUNCTION IS TO CHECK WHETHER USER CREATES BANK ACC OR GAME ACC '''
    run = True

    print("To exit provide 'x'")
    while run:
        if to_acc == 'x':
            break
        if to_acc == '1':
            run = False
            bank_acc(work_dir)
        elif to_acc == '2':
            run = False
            details.game_acc(work_dir)
        else:
            print("PLEASE PROVIDE 1 OR 2 ! ")
            to_acc = input('Enter your choice: ')


def change_dir():
    run = input('Are we suppose to change dir? (y/n) ').lower()
    if run == 'y':
        create_dir = input('Please enter correct file dir (IMPORTANT) : ')
        os.chdir(create_dir)


def create_folder():
    change_dir()
    folder_name = input("Enter the name of the folder:  ")
    os.mkdir(folder_name)
    mkfile = input("Do you want to create a file: (y/n)").lower()
    # newdir = f'{os.getcwd}/{folder_name}'

    if mkfile == 'y':
        # os.chdir(newdir)
        create_file()
    os.chdir(work_dir)


def create_file():
    change_dir()
    run = input('Are you sure you want file ? (y/n): ')
    if bool(run):
        file_name = input('Whats your file name:  ')
        content = input('what the thing you want to write inside:  ')
        with open(file_name, 'w') as f:
            f.write(content)
    os.chdir(work_dir)


work_dir = os.getcwd()

try:
    # raise os.error("hey this is an message for generating error")
    print("FIRST THING IS FIRST !\n")
    print("LETS CHECK IF YOUR HUMAN!\n")
    start = 3
    captcha = input(
        "PLEASE ENTER AN VALUE WITH ONE CAPS LETTER ONE SMALL LETTER ONE NUMBER: ")

    regex = "[A-Z]{1}[a-z]{1}[0-9]{1}"

    while start > 0:
        if(re.match(regex, captcha)):
            break
        else:
            print(f'You have {start} try remaining')
            start -= 1
            captcha = input("Enter here:  ")

    if start == 0:
        raise not_human()

    print('HEY! LETS GET STARTED FEW STEPS\n')
    to_config = input('DO YOU WANT TO SET CONFIG FILES (Y/N): ')
    to_config = to_config.upper()

    if(to_config == 'Y'):
        config_files.createConfig()

    print("Lets get your details: \n")
    print("1 Create an bank account \n")
    print("2 Create an Game account \n")

    to_acc = input('Enter your choice: ')

    check_run_config_create(to_acc)

    to_create = input('WANT TO CREATE Y/N ? ').upper()

    if to_create == 'Y':
        to_create_folder = input(
            "Do you want to create a folder or file: (folder/file) ").lower()
        if to_create_folder == 'folder':
            create_folder()
        else:
            create_file()

except not_human as e:
    print(e.message)

except Exception as e:
    print("we have Encountered an issue please check the code || Message =>  ", e)

finally:
    print("END")
