'''Context manager is 
which handles the setup and tear down
for us we call it by saying with keyword'''

# Class Based Context

import os
from contextlib import contextmanager


class OpenFile():
    '''Custom class created for opening file'''

    def __init__(self, filename, mode):
        '''Instance'''
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # starts
        '''functionality'''
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):  # runs like finally
        '''teardown code'''
        self.file.close()


# With is the context manager
with OpenFile('sample.txt', 'w') as f:
    f.write('Class based Context manager')

print(f.closed)  # returns true if properly closed


# Function Based Context

# We get the contextmanager from the context library use as decorator
# from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    '''function based
    context manager try should be
    finally block for tear down'''
    try:
        f = open(file, mode)
        yield f  # Generator return statement
    finally:
        f.close()


# With is the context manager
with open_file('sample.txt', 'w') as f:
    f.write('Function based context manager')

print(f.closed)  # returns true if properly closed


# --------------------------------------------------------------

# cd context manager code

# import os
# from contextlibrary import contextmanager

# decorator makes contextmanager function
@contextmanager
def change_dir(destination):
    '''Destination'''
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield  # Yield nothing because we dont need any object
    finally:
        os.chdir(cwd)


print(os.getcwd())

with change_dir('Folder-One'):  # None return
    print('Changed Dir location - ', os.getcwd())
    print(os.listdir())

with change_dir('Folder-Two'):  # None return
    print('Changed Dir location - ', os.getcwd())
    print(os.listdir())

print(os.getcwd())
