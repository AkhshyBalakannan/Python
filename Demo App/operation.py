from bank_details import bank_acc
from game_details import Details
import os


class NotHumanError(Exception):
    '''THIS IS USER DEFINED ERROR GENERATED WHEN CAPTCHA IF BLOCK IS FAILED
     This is not human class user defined error class with custome message'''

    def __init__(self, message="NOT A HUMAN BYE"):
        self.message = message

# print(not_human.__doc__)


def check_run_config_create(to_acc, work_dir):
    '''THIS FUNCTION IS TO CHECK WHETHER USER CREATES BANK ACC OR GAME ACC '''
    run = True

    while run:
        if to_acc == '1':
            run = False
            bank_acc(work_dir)
        elif to_acc == '2':
            run = False
            Details.game_acc(work_dir)
        else:
            to_acc = input('Enter 1 OR 2 : ')


def change_dir():
    create_dir = input('Please enter correct file dir (IMPORTANT) : ')
    os.chdir(create_dir)


def create_folder(work_dir):
    change = input("Change of dir? (Y/N)").upper()
    if change == 'Y':
        change_dir()
    folder_name = input("Enter the name of the folder:  ")
    os.mkdir(folder_name)
    mkfile = input("Want a file here: (y/n)").lower()
    storeNewDir = os.getcwd()
    newdir = f'{storeNewDir}/{folder_name}'

    if mkfile == 'y':
        os.chdir(newdir)
        create_file(work_dir)
    os.chdir(work_dir)


def create_file(work_dir):
    change = input("Change of dir? (Y/N)").upper()
    if change == 'Y':
        change_dir()
    file_name = input('Whats your file name:  ')
    content = input('File Open... \nInner content? :  ')
    with open(file_name, 'w') as f:
        f.write(content)
    os.chdir(work_dir)
