# #  ITERATOR IS FOR LOOP WHICH IS RUN BEHIND THE SCENE
# WE USE THIS ITERATOR TO ITER OVER STR
# ITER IS CALLED BY USING NEXT FUNCTION KEYWORD AND ONCE NO NEXT ITERATE IS PRESENT THAN
# THIS IS RAISE AN STOP ITERATION WHICH WILL THROW AN ERROR

from random import randint
s = 'abc'
it = iter(s)
print(it)
# <iterator object at 0x00A1DB50 >
print(next(it))
# 'a'
print(next(it))
# 'b'
print(next(it))
# 'c'
print(next(it))
# Traceback(most recent call last):
# File "<stdin>", line 1, in <module >
print(next(it))
# StopIteration

#   ONCE THIS ITER IS CALLED WE NEED TO RUN A FUNCTION NEXT( NAME_CALLED WITH ITER )


class Random:
    """Iterator for looping to generate jumbled char"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.rand = self.index
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        n = randint(0, self.rand)
        return self.data[n]


value = input('Enter the term to be jumbled:  ')
ran = Random(value)
val = ''
for char in ran:
    val += char
print(val)

# This same example code can be used to produce the reverse of given data
# the only step to change is the return statement of the __next__ function
# we need to return the self.index in the self.data and line above return is not needed
# return self.data[self.index]


# generator
# this generator are simple and powerfull tools used to
# create an iterator. Here this is written like usual
# but to return value we use the yeild key

data = 'golf'
value = list(data[i] for i in range(len(data)-1, -1, -1))
print(value)
# This is generator which will return us a list that is reversed because of -1 -1

sum(i*i for i in range(10))                 # sum of squares
# the output for the above code will 285
# as you can see that is simply looks as list comprehension
# the only difference is () instead of []
