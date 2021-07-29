# FILE HANDLING METHODS ARE DONE HERE
# TO OPEN A FILE WE SIMPLY GIVE IT AS OPEN()
# THIS OPEN HAS TWO PARAMETERS OPEN("LOCATION", "MODE")
# MODES ARE "R" "W" "A"     "A" FOR APPEND WITH EXISTING  "W" FOR WRITTING OR TO CREATE FILE "R" DEFAULT READ

# TO READ THE FILE WE GIVE OBJECT_NAME.READ()

import filecmp
import sys
from stat import *
import re
import fnmatch
import shutil
import os
import tempfile
file = open("ToRead.txt")

print(file.read())

file.close()

# WE CAN ALSO READ CONTENT WITH LENGTH BY SIMPLY GIVING VARIABLE INSIDE THE ()

file = open("ToRead.txt")

print(file.read(21))

file.close()

# WE NEED TO WRAP ALL THESE IN TRY FINALLY BLOCK BECAUSE IT MAY CAUSE ERROR ANYTIME

try:
    file = open("ToRead.txt")
    print(file.read())
finally:
    file.close()

# BUT TO HAVE ALL THE CONTENT IN TRY FINALLY BLOCK WILL BE HARD AND SO WE USE WITH....AS

with open("ToRead.txt", "r") as file:
    file.read()

# THIS WILL AUTOMATICALLY CLOSE THE FILE

# TO WRITE INSIDE THE FILE WE GIVE ITS NAME AND MODE AS W

with open("ToWrite.txt", "w") as file:
    file.write("Hey This is written from the code \nI love python")

# TO REMEMBER IF WE TRY OPENING A EXISTING FILE WITH W ITS CONTENT WILL BE OVERWRITTEN

# TO DYNAMICALLY SAVE YOUR DATA

username = input("Enter the name of file")
details = input("Enter the details to be saved")
with open(f'{username}.txt', "w") as file:
    file.write(f'{details}')

# WE CAN USE THE APPEND MODE TO ADD CONTENT TO FILE WHICH ARE ALREADY PRESENT

with open("ToWrite.txt", "a") as file:
    file.write("\nHey I am the new content from append")

# READLINES METHOD IS USED TO SPLIT LINES IN THE FILES INTO LIST WHICH CAN BE ITERATED

with open("ToWrite.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line)
    # print(set(lines))   # TO CHANGE IT INTO SET


# WE CAN ALSO WRITE AN LIST TO THE FILE BY CALLING THE NAME W

with open("create.txt", "w") as file:
    content = ["I am first", "\nI am second", "\nI am third"]
    file.writelines(content)


# TO CHANGE WORKING DIR OR TO MAKE FOLDERS WE USE OS MODULE


c_dir = os.getcwd()
print(c_dir)

os.chdir("D:\Python\os_try")

os.mkdir("Hello")

with open("test1.txt", "w") as file:
    file.write("Hello I am from another dir")

os.mkdir("delete me")

print(os.listdir())

os.rmdir("delete me")

print(os.listdir())

os.remove("test1.txt")

print(os.listdir())

os.rename("Hello", "Hello_changed")

print(os.listdir())

os.rmdir("Hello_changed")

# OS CAN BE USED TO MKDIR RMDIR REMOVE CHDIR LISTDIR RENAME

# SHUTIL IS USED TO MOVE FILES AND FOLDERS

src = " "
dst = " "

# COPY ALL FILES AND FOLDER

shutil.copytree(src, dst)   # DST FOLDER SHOULD NOT BE PRESENT

# SHUTIL COPY WILL COPY ALL WITH PERMISSION BITS

shutil.copy(src + "FILE NAME", dst)   # COPIES ONLY FILE

# WE ALSO HAVE COPYFILE WHICH WILL ASK FOR BOTH NAME IN SRC AND DST

shutil.copyfile(src + "file name", dst + "file name")

# TO MOVE THE FILE OR FOLDER WE USE MOVE

shutil.move(src + "file name", dst)


# fnmatch — Unix filename pattern matching

# import fnmatch
# import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)

# * matches everything

# ? matches any single character

# [seq] matches any character in seq

# [!seq] matches any character not in seq


regex = fnmatch.translate('*.txt')
print(regex)
# '(?s:.*\\.txt)\\Z'
reobj = re.compile(regex)
print(reobj.match('foobar.txt'))
# <re.Match object; span=(0, 10), match='foobar.txt'>


# stat
# Normally, you would use the os.path.is*() functions
# for testing the type of a file; the functions here are useful
# when you are doing multiple tests of the same file and wish to
# avoid the overhead of the stat() system call for each test.
# These are also useful when checking for information about a
# file that isn’t handled by os.path, like the tests for block
# and character devices.

# filecmp
filecmp.cmp(f1, f2, shallow=True)
#   Compare the files named f1 and f2, returning True if they seem equal, False otherwise.

filecmp.cmpfiles(dir1, dir2, common, shallow=True)
#   Compare the files in the two directories dir1 and dir2 whose names are given by common.


# The dircmp class

class filecmp.dircmp(a, b, ignore=None, hide=None)
# Construct a new directory comparison object, to compare the directories a and b.


# tempfile — Generate temporary files and directories

# import tempfile
tempfile.TemporaryFile(mode='w+b', buffering=-1, encoding=None,
                       newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

tempfile.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None,
                            newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None)

tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)
# This function securely creates a temporary directory using the same rules as mkdtemp().

tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)
# Creates a temporary file in the most secure manner possible

tempfile.mkdtemp(suffix=None, prefix=None, dir=None)
# Creates a temporary directory in the most secure manner possible.


tempfile.gettempdir()¶
# Return the name of the directory used for temporary files.

tempfile.gettempdirb()
# Same as gettempdir() but the return value is in bytes.


# import tempfile

# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
fp.read()
b'Hello world!'
# close the file, it will be removed
fp.close()

# create a temporary file using a context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()
b'Hello world!'
# file is now closed and removed

# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)

# directory and contents have been removed
