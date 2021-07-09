import os
import re
import config_files
from operation import NotHumanError, check_run_config_create, change_dir, create_file, create_folder

work_dir = os.getcwd()

try:
    # raise os.error("hey this is an message for generating error")
    print("FIRST THING IS FIRST !\n LETS CHECK IF YOUR HUMAN!")
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
        raise NotHumanError()

    to_config = input(
        'HEY! LETS GET STARTED FEW STEPS\n DO YOU WANT TO SET CONFIG FILES (Y/N): ').upper()

    if(to_config == 'Y'):
        config_files.createConfig()

    print("Lets get your details Bank or Game ACC (1/2): \n")
    to_acc = input('Enter your choice: ')

    check_run_config_create(to_acc, work_dir)

    to_create = input('WANT TO CREATE Y/N ? ').upper()

    if to_create == 'Y':
        to_create_folder = input(
            "Do you want to create a folder or file: (folder/file) ").lower()
        if to_create_folder == 'folder':
            create_folder(work_dir)
        else:
            create_file(work_dir)

except NotHumanError as e:
    print(e.message)

except Exception as e:
    print("we have Encountered an issue please check the code || Message =>  ", e)

finally:
    print("END OF PROGRAM")
