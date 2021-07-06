# #  ITERATOR IS FOR LOOP WHICH IS RUN BEHIND THE SCENE
# WE USE THIS ITERATOR TO ITER OVER STR
# ITER IS CALLED BY USING NEXT FUNCTION KEYWORD AND ONCE NO NEXT ITERATE IS PRESENT THAN
# THIS IS RAISE AN STOP ITERATION WHICH WILL THROW AN ERROR

# >> > s = 'abc'
# >> > it = iter(s)
# >> > it
# <iterator object at 0x00A1DB50 >
# >> > next(it)
# 'a'
# >> > next(it)
# 'b'
# >> > next(it)
# 'c'
# >> > next(it)
# Traceback(most recent call last):
# File "<stdin>", line 1, in <module >
# #  next(it)
# StopIteration


#   ONCE THIS ITER IS CALLED WE NEED TO RUN A FUNCTION NEXT( NAME_CALLED WITH ITER )


from random import randint


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

# generator

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
